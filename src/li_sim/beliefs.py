"""Private belief-tier updates — subjective impressions distinct from episodic memory."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .memory import format_contacts, format_major_moments, format_memories, memories_since_day
from .models import IslanderProfile, IslanderState, LogEvent, Visibility, VillaState
from .rng import seeded_rng

if TYPE_CHECKING:
    from .config import Settings
    from .llm import LLMClient
    from .logging_utils import EventLog

BELIEF_SYSTEM = """You maintain private impressions for a televised villa social game.
Return a single JSON object only:
{
  "self": "1-3 sentences: your read on your position, who you trust, what you want",
  "others": {"Handle": "one short sentence per active islander (use exact handles from the prompt)"}
}
Beliefs are subjective — they may diverge from shared facts or what others said publicly.
Update from what YOU saw, heard, and privately thought — not from narrator certainty."""


def format_beliefs(islander: IslanderState, others: list[str]) -> str:
    lines: list[str] = []
    if islander.self_belief.strip():
        lines.append(f"- You: {islander.self_belief.strip()}")
    else:
        lines.append("- You: (no settled read yet — still forming impressions)")
    for name in others:
        impression = islander.beliefs.get(name, "").strip()
        if impression:
            lines.append(f"- {name}: {impression}")
        else:
            lines.append(f"- {name}: (no strong impression yet)")
    return "\n".join(lines)


def format_reflections(islander: IslanderState, limit: int = 6) -> str:
    if not islander.reflections:
        return "(none yet)"
    return "\n".join(f"- {line}" for line in islander.reflections[-limit:])


def _belief_user_prompt(
    profile: IslanderProfile,
    state: VillaState,
    islander: IslanderState,
    day: int,
) -> str:
    others = [n for n in state.active_names() if n != profile.name]
    today_memories = memories_since_day(islander, day)
    return f"""End of Day {day} belief update for {profile.name}.

Couples: {', '.join(f'{a}+{b}' for a, b in state.couples()) or 'none'}.
Dumped: {', '.join(state.dumped) or 'nobody'}.

Shared villa history (facts everyone could know):
{format_major_moments(state, limit=12)}

Your conversations (counts, not scores):
{format_contacts(islander, others)}

Today's private reflections:
{format_reflections(islander)}

Today's episodes you personally witnessed:
{format_memories(today_memories) or '(quiet day)'}

Current impressions (update these):
{format_beliefs(islander, others)}

Revise your self-read and per-person impressions based on today. JSON only."""


def _apply_belief_payload(islander: IslanderState, others: list[str], raw: dict[str, Any]) -> None:
    self_text = raw.get("self")
    if isinstance(self_text, str) and self_text.strip():
        islander.self_belief = self_text.strip()[:600]
    others_map = raw.get("others")
    fresh: dict[str, str] = {}
    if isinstance(others_map, dict):
        for name in others:
            val = others_map.get(name)
            if isinstance(val, str) and val.strip():
                fresh[name] = val.strip()[:280]
    islander.beliefs = fresh


def stub_belief_update(
    islander: IslanderState,
    state: VillaState,
    *,
    seed: int,
    name: str,
    day: int,
) -> dict[str, Any]:
    others = [n for n in state.active_names() if n != name]
    rng = seeded_rng(seed, "belief", name, day)
    beliefs: dict[str, str] = {}
    for other in others:
        log = islander.contacts.get(other)
        if log and (log.talks + log.whispers) >= 3:
            beliefs[other] = f"Spoken often ({log.talks + log.whispers}x) — starting to read them."
        elif log and (log.talks + log.whispers) >= 1:
            beliefs[other] = "Some contact; still unclear what they're after."
        elif other not in beliefs:
            beliefs[other] = "Barely interacted."
    partner = islander.coupled_with
    self_bits = []
    if islander.reflections:
        self_bits.append(islander.reflections[-1][:180])
    if partner and partner in state.active_names():
        self_bits.append(f"Coupled with {partner} going into D{day + 1}.")
    elif name in state.singles():
        self_bits.append(f"Single going into D{day + 1} — exposed at recoupling.")
    self_text = " ".join(self_bits) if self_bits else islander.self_belief or "Still finding my feet."
    if rng.random() > 0.7 and others:
        target = rng.choice(others)
        beliefs[target] = f"Watching {target} closely after today."
    return {"self": self_text[:600], "others": beliefs}


def update_beliefs_for_day(
    state: VillaState,
    profiles: dict[str, IslanderProfile],
    llm: LLMClient,
    log: EventLog,
    settings: Settings,
) -> None:
    day = state.day
    for name in state.active_names():
        islander = state.islanders[name]
        profile = profiles[name]
        others = [n for n in state.active_names() if n != name]
        user = _belief_user_prompt(profile, state, islander, day)
        if settings.stub:
            raw = stub_belief_update(islander, state, seed=settings.seed, name=name, day=day)
            model = "stub"
        else:
            raw, _text, model = llm.complete_json(
                name,
                BELIEF_SYSTEM,
                user,
                fallback=stub_belief_update(islander, state, seed=settings.seed, name=name, day=day),
            )
        _apply_belief_payload(islander, others, raw)
        event = LogEvent(
            day=day,
            phase=state.phase.value,
            kind="belief_update",
            actor=name,
            visibility=Visibility.PRIVATE.value,
            text=islander.self_belief[:200],
            extra={"beliefs": dict(islander.beliefs), "model": model},
        )
        log.write(event)
