from __future__ import annotations

import random
from collections.abc import Callable

from .agent import parse_allowed, prize_nudge, validate_target
from .config import Settings
from .llm import LLMClient
from .logging_utils import EventLog
from .memory import note_chat, record_moment, remember
from .models import (
    Action,
    ActionType,
    IslanderProfile,
    IslanderState,
    Location,
    LogEvent,
    Phase,
    VillaState,
    Visibility,
)

DecideFn = Callable[[IslanderProfile, list[ActionType], str, bool], Action]


class Host:
    def __init__(
        self,
        profiles: dict[str, IslanderProfile],
        llm: LLMClient,
        log: EventLog,
        settings: Settings | None = None,
    ):
        self.profiles = profiles
        self.llm = llm
        self.log = log
        self.settings = settings or Settings()

    def announce(
        self,
        state: VillaState,
        text: str,
        *,
        kind: str = "host",
        visibility: Visibility = Visibility.PUBLIC,
        extra: dict | None = None,
    ) -> LogEvent:
        event = LogEvent(
            day=state.day,
            phase=state.phase.value,
            tick=state.tick,
            kind=kind,
            actor="Host",
            text=text,
            visibility=visibility.value,
            extra=extra or {},
        )
        self.log.write(event)
        if visibility in (Visibility.PUBLIC, Visibility.HOST):
            for islander in state.active():
                remember(islander, event)
            if kind in {"host", "dump", "win"}:
                record_moment(state, text)
        return event

    def morning(self, state: VillaState) -> None:
        state.phase = Phase.MORNING
        pairs = ", ".join(f"{a} & {b}" for a, b in state.couples()) or "no official couples"
        singles = ", ".join(state.singles()) or "nobody"
        self.announce(
            state,
            f"Good morning villa. Day {state.day}. Couples: {pairs}. Singles: {singles}. "
            + prize_nudge(
                self.settings.prize_emphasis,
                "£50,000 is still on the table. Graft, clock the other couples, and don't get left single.",
                "Graft, clock the other couples, and don't get left single.",
            ),
        )

    def challenge(self, state: VillaState, decide: DecideFn, name: str) -> None:
        state.phase = Phase.CHALLENGE
        self.announce(state, f"Challenge time: {name}. Give it everything — the public loves a winner.")
        scores: dict[str, float] = {}
        for islander in state.active():
            profile = self.profiles[islander.name]
            action = decide(
                profile,
                [ActionType.CHALLENGE, ActionType.PASS],
                f"You are in the {name} challenge. Set challenge_effort 1-10 and describe your moment.",
                False,
            )
            action = parse_allowed(action, [ActionType.CHALLENGE, ActionType.PASS])
            effort = action.challenge_effort or 6
            jitter = random.Random(state.day * 17 + hash(islander.name)).uniform(-1.0, 1.5)
            score = max(1.0, min(10.0, effort + jitter))
            scores[islander.name] = score
            state.challenge_scores[islander.name] = state.challenge_scores.get(islander.name, 0) + score
            state.reputation[islander.name] = state.reputation.get(islander.name, 50) + score * 0.6
            islander.last_thought = action.thought
            self.log.write(
                LogEvent(
                    day=state.day,
                    phase=state.phase.value,
                    kind="challenge",
                    actor=islander.name,
                    text=action.content or f"{islander.name} scores {score:.1f}.",
                    thought=action.thought,
                    play=action.play or None,
                    visibility=Visibility.PUBLIC.value,
                    extra={"score": score},
                )
            )
            for person in state.active():
                remember(
                    person,
                    LogEvent(
                        day=state.day,
                        phase=state.phase.value,
                        kind="challenge",
                        actor=islander.name,
                        text=f"{islander.name} scored {score:.1f} in {name}.",
                        visibility=Visibility.PUBLIC.value,
                    ),
                )
        winner = max(scores, key=scores.get)
        state.reputation[winner] += 4
        self.announce(state, f"{winner} wins {name}. Public reputation ticks up.")

    def introduce_bombshells(self, state: VillaState, names: list[str]) -> None:
        for name in names:
            if name not in self.profiles:
                continue
            existing = state.islanders.get(name)
            if existing and not existing.dumped:
                continue
            state.islanders[name] = IslanderState(
                name=name,
                location=Location.LOUNGE,
                is_bombshell=True,
                entered_day=state.day,
            )
            state.reputation[name] = 50.0
            self.announce(
                state,
                f"I've got a text! A bombshell is entering the villa. "
                f"They are addressed as {name}. "
                "If you are left single after tonight's recoupling, you may be dumped.",
            )

    def dump_person(self, state: VillaState, name: str, reason: str) -> None:
        if name not in state.islanders or state.islanders[name].dumped:
            return
        if len(state.active_names()) <= 2:
            return
        person = state.islanders[name]
        partner = person.coupled_with
        person.dumped = True
        person.coupled_with = None
        if partner and partner in state.islanders and state.islanders[partner].coupled_with == name:
            state.islanders[partner].coupled_with = None
        if name not in state.dumped:
            state.dumped.append(name)
        self.announce(
            state,
            f"{name}, {reason} Grab your suitcase. You're dumped from the island.",
            kind="dump",
            extra={"dumped": name},
        )

    def dates(self, state: VillaState, decide: DecideFn) -> None:
        state.phase = Phase.DATES
        pairs = state.couples()
        if not pairs:
            self.announce(state, "No couples, no dates. Go graft.")
            return
        self.announce(state, "Date night. Couples head to the hideaway — what is said there stays mostly between you.")
        for a, b in pairs:
            left = state.islanders[a]
            right = state.islanders[b]
            left.location = Location.HIDEAWAY
            right.location = Location.HIDEAWAY
            for speaker_name, listener_name in ((a, b), (b, a)):
                profile = self.profiles[speaker_name]
                action = decide(
                    profile,
                    [ActionType.SPEAK, ActionType.WHISPER, ActionType.PASS],
                    f"Hideaway date with {listener_name}. Be specific. This can deepen or crack the couple.",
                    True,
                )
                line = action.content or f"{speaker_name} looks at {listener_name} and goes quiet."
                event = LogEvent(
                    day=state.day,
                    phase=state.phase.value,
                    kind="date",
                    actor=speaker_name,
                    target=listener_name,
                    participants=[a, b],
                    location=Location.HIDEAWAY.value,
                    visibility=Visibility.WHISPER.value,
                    text=line,
                    thought=action.thought,
                    play=action.play or None,
                )
                self.log.write(event)
                remember(state.islanders[a], event)
                remember(state.islanders[b], event)
            note_chat(state, a, b, kind="date")
            left.location = Location.LOUNGE
            right.location = Location.LOUNGE
        self.announce(state, "Dates are over. The group will smell the vibe even if they didn't hear the words.")
        for a, b in pairs:
            record_moment(state, f"{a} and {b} went on a hideaway date.")

    def recoupling(
        self,
        state: VillaState,
        decide: DecideFn,
        label: str,
        pickers: str,
        dump_singles: bool = False,
    ) -> None:
        state.phase = Phase.RECOUPLING
        for islander in state.active():
            islander.location = Location.FIREPIT
        picker_names = [
            i.name
            for i in state.active()
            if self.profiles[i.name].gender == ("girl" if pickers == "girls" else "boy")
        ]
        bombshells_today = [
            i.name
            for i in state.active()
            if i.is_bombshell and i.entered_day == state.day
        ]
        order = bombshells_today + [n for n in picker_names if n not in bombshells_today]
        if not order:
            order = state.active_names()
        incoming = ", ".join(f"{a} & {b}" for a, b in state.couples()) or "no official couples yet"
        bombshell_note = (
            f" {', '.join(bombshells_today)} just arrived and pick first."
            if bombshells_today
            else ""
        )
        dump_note = (
            " Anyone left single when the last speech is done is dumped from the island immediately."
            if dump_singles
            else ""
        )
        self.announce(
            state,
            f"{label}. One at a time.{bombshell_note} "
            f"You may pick anyone still here who has not already been chosen tonight. "
            f"Walking in as a couple does not lock anyone. Picking order: {', '.join(order)}. "
            f"Couples as of now: {incoming}.{dump_note}"
            + prize_nudge(self.settings.prize_emphasis, " Prize: £50,000.", ""),
        )
        taken: set[str] = set()
        new_pairs: list[tuple[str, str]] = []
        for name in order:
            if name in taken:
                continue
            available = [n for n in state.active_names() if n != name and n not in taken]
            if not available:
                record_moment(state, f"{name} had nobody left to couple with and stayed single.")
                continue
            already = ", ".join(f"{a} & {b}" for a, b in new_pairs) or "nobody yet tonight"
            current = ", ".join(f"{a} & {b}" for a, b in state.couples()) or "none"
            profile = self.profiles[name]
            extra = (
                "FIREPIT RECOUPLING IS MANDATORY. You MUST return type=couple.\n"
                + (
                    f"You just arrived. You pick first.\n"
                    if name in bombshells_today
                    else ""
                )
                + f"You may pick ANYONE still in the villa who is not already chosen tonight: {', '.join(available)}\n"
                f"Already chosen tonight (ceremony bookkeeping — they already have a partner for tonight): {already}.\n"
                f"Couples standing as of this speech: {current}.\n"
                "Someone already in a couple is still pickable. Whether you take them or leave them is your judgement. "
                "The villa does not forbid it and does not require it. Speech as you pick them."
            )
            action = decide(profile, [ActionType.COUPLE], extra, False)
            action = validate_target(
                parse_allowed(action, [ActionType.COUPLE]),
                state,
                name,
                available=available,
            )
            target = action.target if action.target in available else available[0]
            taken.add(name)
            taken.add(target)
            displaced = _couple_up(state, name, target)
            new_pairs.append(tuple(sorted((name, target))))
            speech = action.content or f"{name} chooses {target}."
            event = LogEvent(
                day=state.day,
                phase=state.phase.value,
                kind="couple_choice",
                actor=name,
                target=target,
                participants=state.active_names(),
                location=Location.FIREPIT.value,
                visibility=Visibility.PUBLIC.value,
                text=speech,
                thought=action.thought,
                play=action.play or None,
            )
            self.log.write(event)
            for person in state.active():
                remember(person, event)
            moment = f"{name} picked {target} at recoupling."
            if displaced:
                moment += f" Left single: {', '.join(displaced)}."
            record_moment(state, moment)

        for a, b in new_pairs:
            state.reputation[a] = state.reputation.get(a, 50) + 2
            state.reputation[b] = state.reputation.get(b, 50) + 2
        pair_txt = ", ".join(f"{a} & {b}" for a, b in new_pairs) or "none"
        singles = state.singles()
        self.announce(
            state,
            f"New couples: {pair_txt}. "
            + (f"Left single: {', '.join(singles)}." if singles else "Everyone is coupled."),
            extra={"couples": [list(p) for p in new_pairs], "singles": singles},
        )
        if dump_singles:
            leftover = list(state.singles())
            if leftover:
                self.announce(
                    state,
                    "I've got a text! The islander(s) not picked to be in a couple will be dumped from the island immediately.",
                )
            for name in leftover:
                self.dump_person(
                    state,
                    name,
                    "you weren't picked. That's the recoupling rule.",
                )

    def dumping(self, state: VillaState, decide: DecideFn, dump_count: int, mode: str) -> None:
        state.phase = Phase.DUMPING
        for islander in state.active():
            islander.location = Location.FIREPIT
        self.announce(
            state,
            "Dumping. The villa votes for who they want to SAVE. "
            "Lowest combined safety (votes + reputation, singles first) may leave.",
        )
        votes: dict[str, int] = {n: 0 for n in state.active_names()}
        for islander in state.active():
            profile = self.profiles[islander.name]
            action = decide(
                profile,
                [ActionType.SAVE, ActionType.VOTE, ActionType.PASS],
                "Popularity dump. Vote to SAVE someone (not yourself). type=save or vote, target=name.",
                False,
            )
            action = validate_target(
                parse_allowed(action, [ActionType.SAVE, ActionType.VOTE, ActionType.PASS]),
                state,
                islander.name,
            )
            target = action.target
            if target and target in votes and target != islander.name:
                votes[target] += 1
            event = LogEvent(
                day=state.day,
                phase=state.phase.value,
                kind="vote",
                actor=islander.name,
                target=target,
                participants=state.active_names(),
                location=Location.FIREPIT.value,
                visibility=Visibility.PUBLIC.value,
                text=action.content or f"{islander.name} saves {target}.",
                thought=action.thought,
                play=action.play or None,
                extra={"votes": dict(votes)},
            )
            self.log.write(event)
            for person in state.active():
                remember(person, event)

        leaving = _who_leaves(state, votes, dump_count, mode)
        for name in leaving:
            self.dump_person(state, name, "the villa didn't save you.")

    def public_vote_save(self, state: VillaState, decide: DecideFn, at_risk_count: int = 2) -> None:
        state.phase = Phase.DUMPING
        for islander in state.active():
            islander.location = Location.FIREPIT
        active = state.active_names()
        if len(active) <= 3:
            self.announce(state, "Not enough islanders left for a public vote dumping.")
            return
        at_risk_count = min(max(2, at_risk_count), len(active) - 2)
        ranked = sorted(active, key=lambda n: state.reputation.get(n, 50))
        at_risk = ranked[:at_risk_count]
        safe = [n for n in active if n not in at_risk]
        board = ", ".join(f"{n} ({state.reputation.get(n, 50):.0f})" for n in reversed(ranked))
        self.announce(
            state,
            "I've got a text! The public has voted for their favourite islanders. "
            f"Public standings: {board}. "
            f"At risk: {', '.join(at_risk)}. "
            "The public does not dump you directly — the safe islanders now choose who to SAVE.",
        )
        saves: dict[str, int] = {n: 0 for n in at_risk}
        for name in safe:
            profile = self.profiles[name]
            extra = (
                "PUBLIC VOTE DUMP. You are SAFE. The public put these islanders at risk: "
                f"{', '.join(at_risk)}. You MUST vote to SAVE one of them. "
                f"type=save, target MUST be one of: {', '.join(at_risk)}. "
                "The at-risk islander with the fewest save votes is dumped."
            )
            action = decide(profile, [ActionType.SAVE, ActionType.VOTE], extra, False)
            action = validate_target(
                parse_allowed(action, [ActionType.SAVE, ActionType.VOTE]),
                state,
                name,
                available=at_risk,
            )
            target = action.target if action.target in at_risk else at_risk[0]
            saves[target] += 1
            event = LogEvent(
                day=state.day,
                phase=state.phase.value,
                kind="vote",
                actor=name,
                target=target,
                participants=active,
                location=Location.FIREPIT.value,
                visibility=Visibility.PUBLIC.value,
                text=action.content or f"{name} saves {target}.",
                thought=action.thought,
                play=action.play or None,
                extra={"saves": dict(saves), "at_risk": at_risk},
            )
            self.log.write(event)
            for person in state.active():
                remember(person, event)
        dumped_name = sorted(at_risk, key=lambda n: (saves.get(n, 0), state.reputation.get(n, 50)))[0]
        self.announce(
            state,
            f"Save votes: {', '.join(f'{n}={saves[n]}' for n in at_risk)}. "
            f"{dumped_name} received the fewest saves.",
        )
        self.dump_person(
            state,
            dumped_name,
            "the public put you at risk and the islanders didn't save you.",
        )

    def diary_round(self, state: VillaState, decide: DecideFn) -> None:
        state.phase = Phase.NIGHT
        self.announce(state, "Diary room. Speak to the camera. The public hears this; the villa does not.")
        for islander in state.active():
            original = islander.location
            islander.location = Location.DIARY_ROOM
            profile = self.profiles[islander.name]
            action = decide(
                profile,
                [ActionType.DIARY, ActionType.PASS],
                "Diary room. The public hears this. Talk about your couple, who you're grafting, or how you see the villa. type=diary.",
                False,
            )
            text = action.content or f"{islander.name} shrugs at the camera."
            event = LogEvent(
                day=state.day,
                phase=state.phase.value,
                kind="diary",
                actor=islander.name,
                location=Location.DIARY_ROOM.value,
                visibility=Visibility.PRIVATE.value,
                text=text,
                thought=action.thought,
                play=action.play or None,
            )
            self.log.write(event)
            remember(islander, event)
            islander.last_thought = action.thought
            # Public likes honesty-shaped diary content a little
            bump = 1.2 if any(w in text.lower() for w in ("love", "sorry", "real", "choose")) else 0.4
            if any(w in text.lower() for w in ("game", "win", "public", "final")):
                bump -= 0.2
            state.reputation[islander.name] = state.reputation.get(islander.name, 50) + bump
            islander.location = original
            if action.thought:
                islander.reflections.append(f"D{state.day}: {action.thought}")

    def finale(self, state: VillaState) -> None:
        state.phase = Phase.FINALE
        pairs = state.couples()
        if not pairs:
            remaining = state.active_names()
            if len(remaining) >= 2:
                remaining = sorted(remaining, key=lambda n: state.reputation.get(n, 50), reverse=True)
                pairs = [(remaining[0], remaining[1])]
                state.islanders[remaining[0]].coupled_with = remaining[1]
                state.islanders[remaining[1]].coupled_with = remaining[0]
            else:
                self.announce(state, "Not enough islanders left to crown a couple.")
                state.season_over = True
                return
        scored = []
        for a, b in pairs:
            total = state.reputation.get(a, 50) + state.reputation.get(b, 50)
            scored.append((total, a, b))
        scored.sort(reverse=True)
        _, w1, w2 = scored[0]
        state.winner_couple = [w1, w2]
        state.season_over = True
        ranking = ", ".join(f"{a} & {b} ({tot:.0f})" for tot, a, b in scored)
        self.announce(
            state,
            f"The public has voted. {w1} and {w2} win Love Island and the £50,000. "
            f"Couple scores: {ranking}.",
            kind="win",
            extra={"winners": [w1, w2], "ranking": [[a, b, tot] for tot, a, b in scored]},
        )


def _couple_up(state: VillaState, a: str, b: str) -> list[str]:
    """Pair a and b. Anyone they leave behind becomes single. Returns displaced names."""
    displaced: list[str] = []
    for name in (a, b):
        old = state.islanders[name].coupled_with
        if old and old not in (a, b) and old in state.islanders:
            if state.islanders[old].coupled_with == name:
                state.islanders[old].coupled_with = None
                displaced.append(old)
    state.islanders[a].coupled_with = b
    state.islanders[b].coupled_with = a
    return displaced


def _who_leaves(state: VillaState, votes: dict[str, int], dump_count: int, mode: str) -> list[str]:
    active = state.active_names()
    if len(active) <= 2:
        return []
    dump_count = min(dump_count, len(active) - 2)
    singles = set(state.singles())

    def danger(name: str) -> tuple:
        single_flag = 0 if (mode == "singles_then_reputation" and name in singles) else 1
        # fewer save-votes and lower reputation => more danger
        return (single_flag, votes.get(name, 0), state.reputation.get(name, 50))

    ranked = sorted(active, key=danger)
    return ranked[:dump_count]
