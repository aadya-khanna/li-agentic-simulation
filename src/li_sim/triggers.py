from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .models import RewardTriggerSpec, VillaState
from .rng import seeded_rng

if TYPE_CHECKING:
    from .config import Settings
    from .host import Host

CHALLENGE_NAMES = ("Hearts on Fire", "Partner Quiz", "Blindfold Kiss", "Villa Challenge")

_INTERACTION_KINDS = frozenset({"speak", "whisper", "date", "pull_aside", "singles_chat"})


def partner_contact(state: VillaState, a: str, b: str, since_day: int) -> int:
    islander = state.islanders.get(a)
    if not islander:
        return 0
    count = 0
    for mem in islander.memories:
        if mem.day < since_day:
            continue
        if b in mem.actors and mem.kind in _INTERACTION_KINDS:
            count += 1
    return count


def pair_contact(state: VillaState, a: str, b: str) -> int:
    total = 0
    for left, right in ((a, b), (b, a)):
        islander = state.islanders.get(left)
        if not islander:
            continue
        log = islander.contacts.get(right)
        if log:
            total += log.talks + log.whispers
    return total


def is_couple(state: VillaState, a: str, b: str) -> bool:
    left = state.islanders.get(a)
    right = state.islanders.get(b)
    if not left or not right:
        return False
    return left.coupled_with == b and right.coupled_with == a


def lowest_contact_couple(state: VillaState, since_day: int) -> tuple[str, str, int] | None:
    pairs = state.couples()
    if not pairs:
        return None
    scored = [
        (partner_contact(state, a, b, since_day), a, b)
        for a, b in pairs
    ]
    scored.sort(key=lambda row: row[0])
    contact, a, b = scored[0]
    return a, b, contact


def best_non_couple_pair(state: VillaState) -> tuple[str, str, int] | None:
    names = state.active_names()
    best: tuple[str, str, int] | None = None
    for i, a in enumerate(names):
        for b in names[i + 1 :]:
            if is_couple(state, a, b):
                continue
            contact = pair_contact(state, a, b)
            if best is None or contact > best[2]:
                best = (a, b, contact)
    return best


def total_outbound_contact(state: VillaState, name: str) -> int:
    islander = state.islanders.get(name)
    if not islander:
        return 0
    return sum(log.talks + log.whispers for log in islander.contacts.values())


def top_contact_partner(state: VillaState, name: str) -> tuple[str, int] | None:
    islander = state.islanders.get(name)
    if not islander or not islander.contacts:
        return None
    best_name = ""
    best_total = -1
    for other, log in islander.contacts.items():
        total = log.talks + log.whispers
        if total > best_total:
            best_total = total
            best_name = other
    if not best_name or best_total <= 0:
        return None
    return best_name, best_total


def top_single_and_contact(state: VillaState) -> tuple[str, str, int] | None:
    singles = state.singles()
    best: tuple[str, str, int] | None = None
    for name in singles:
        total = total_outbound_contact(state, name)
        partner = top_contact_partner(state, name)
        if not partner:
            continue
        other, _ = partner
        if best is None or total > best[2]:
            best = (name, other, total)
    return best


def reputation_spread(state: VillaState) -> float:
    active = state.active_names()
    if len(active) < 2:
        return 0.0
    scores = [state.reputation.get(n, 50.0) for n in active]
    return max(scores) - min(scores)


def _tie_break(settings: Settings, *parts: str | int) -> float:
    rng = seeded_rng(settings.seed, "trigger", *parts)
    return rng.random()


def evaluate_trigger(
    state: VillaState,
    spec: RewardTriggerSpec,
    settings: Settings,
) -> dict[str, Any] | None:
    if state.day < spec.min_day:
        return None

    since = state.last_recoupling_day or 1

    if spec.event == "hideaway":
        if spec.max_partner_contact is None:
            return None
        candidates = [
            (partner_contact(state, a, b, since), a, b)
            for a, b in state.couples()
        ]
        if not candidates:
            return None
        candidates.sort(key=lambda row: (row[0], _tie_break(settings, spec.id, row[1], row[2])))
        contact, a, b = candidates[0]
        if contact > spec.max_partner_contact:
            return None
        return {"targets": [a, b], "metrics": {"partner_contact": contact}}

    if spec.event == "pull_aside":
        if spec.min_pair_contact is None:
            return None
        match = best_non_couple_pair(state)
        if not match:
            return None
        a, b, contact = match
        if contact < spec.min_pair_contact:
            return None
        if _tie_break(settings, spec.id, a) > 0.5:
            a, b = b, a
        return {"targets": [a, b], "metrics": {"pair_contact": contact}}

    if spec.event == "singles_chat":
        if spec.min_single_contact is None:
            return None
        match = top_single_and_contact(state)
        if not match:
            return None
        single, other, total = match
        if total < spec.min_single_contact:
            return None
        return {"targets": [single, other], "metrics": {"single_contact": total}}

    if spec.event == "challenge":
        active = len(state.active_names())
        min_active = spec.min_active or 4
        if active < min_active:
            return None
        min_gap = spec.min_days_since_challenge or 2
        since_challenge = state.day - (state.last_challenge_day or 0)
        if since_challenge < min_gap:
            return None
        rng = seeded_rng(settings.seed, "challenge_name", state.day, spec.id)
        name = CHALLENGE_NAMES[rng.randint(0, len(CHALLENGE_NAMES) - 1)]
        return {"targets": [], "metrics": {"active": active}, "challenge_name": name}

    return None


def pick_trigger(
    state: VillaState,
    triggers: list[RewardTriggerSpec],
    settings: Settings,
) -> tuple[RewardTriggerSpec, dict[str, Any]] | None:
    for spec in sorted(triggers, key=lambda t: t.priority):
        payload = evaluate_trigger(state, spec, settings)
        if payload:
            return spec, payload
    return None


def fire_trigger(
    host: Host,
    state: VillaState,
    spec: RewardTriggerSpec,
    payload: dict[str, Any],
    decide,
    settings: Settings,
) -> None:
    extra = {"trigger_id": spec.id, **payload.get("metrics", {})}

    if spec.event == "hideaway":
        a, b = payload["targets"]
        host.hideaway_for_pair(state, a, b, decide, trigger_id=spec.id, extra=extra)
    elif spec.event == "pull_aside":
        a, b = payload["targets"]
        host.pull_aside(state, a, b, decide, trigger_id=spec.id, extra=extra)
    elif spec.event == "singles_chat":
        single, other = payload["targets"]
        host.singles_chat(state, single, other, decide, trigger_id=spec.id, extra=extra)
    elif spec.event == "challenge":
        name = payload.get("challenge_name", "Villa Challenge")
        host.challenge(state, decide, name, trigger_id=spec.id, extra=extra)
        state.last_challenge_day = state.day

    state.last_reward_day = state.day
    state.last_reward_id = spec.id
