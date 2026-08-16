from __future__ import annotations

import random
from pathlib import Path

import yaml

from .agent import (
    WORLD_ACTIONS,
    decision_user_prompt,
    grafting_nudge,
    in_character_nudge,
    parse_allowed,
    prize_nudge,
    system_prompt,
    validate_target,
)
from .brief import print_brief_panel, summarize_events, write_brief_log
from .config import DATA_DIR, LOG_DIR, Settings
from .host import Host
from .llm import LLMClient
from .logging_utils import EventLog, save_checkpoint
from .memory import note_chat, remember, record_moment
from .models import (
    Action,
    ActionType,
    DayPlan,
    InnerThought,
    IslanderProfile,
    IslanderState,
    Location,
    LogEvent,
    Phase,
    SeasonSchedule,
    VillaState,
    Visibility,
)
from .recap import print_day, print_finale, print_open


def load_profiles(path: Path | None = None) -> dict[str, IslanderProfile]:
    raw = yaml.safe_load((path or DATA_DIR / "islanders.yaml").read_text(encoding="utf-8"))
    profiles = [IslanderProfile.model_validate(row) for row in raw["islanders"]]
    return {p.name: p for p in profiles}


def load_schedule(path: Path | None = None) -> SeasonSchedule:
    raw = yaml.safe_load((path or DATA_DIR / "schedule.yaml").read_text(encoding="utf-8"))
    return SeasonSchedule.model_validate(raw)


def new_villa(
    profiles: dict[str, IslanderProfile],
    season_name: str,
    settings: Settings | None = None,
) -> VillaState:
    locations = [Location.LOUNGE, Location.POOL, Location.TERRACE]
    islanders = {}
    reputation = {}
    starters = [p for p in profiles.values() if p.enters_on <= 1]
    for idx, profile in enumerate(starters):
        islanders[profile.name] = IslanderState(
            name=profile.name,
            location=locations[idx % len(locations)],
            entered_day=1,
        )
        reputation[profile.name] = 50.0
    settings = settings or Settings()
    state = VillaState(
        season_name=season_name,
        islanders=islanders,
        reputation=reputation,
        prize_emphasis=settings.prize_emphasis,
        dual_thought=settings.dual_thought,
    )
    return state


class Simulation:
    def __init__(self, settings: Settings | None = None):
        self.settings = settings or Settings()
        self.profiles = load_profiles()
        self.schedule = load_schedule()
        self.llm = LLMClient(self.settings, {n: p for n, p in self.profiles.items()})
        self.log = EventLog(self.settings.log_path)
        self.brief_path = self.settings.log_path.parent / "brief.log"
        self.brief_path.write_text("", encoding="utf-8")
        self.state = new_villa(self.profiles, self.schedule.season_name, self.settings)
        self.host = Host(self.profiles, self.llm, self.log, self.settings)

    def decide(
        self,
        profile: IslanderProfile,
        allowed: list[ActionType],
        extra: str,
        scene: bool,
    ) -> Action:
        system = system_prompt(profile, self.settings)
        user = decision_user_prompt(
            profile, self.state, allowed, extra=extra, scene=scene, settings=self.settings
        )
        action = self.llm.decide_action(profile.name, system, user)
        action = validate_target(parse_allowed(action, allowed), self.state, profile.name)
        self.log_inner_thought(profile.name, action)
        return action

    def log_inner_thought(self, name: str, action: Action) -> None:
        text = (action.thought or "").strip()
        play = (action.play or "").strip()
        if not text and not play:
            return
        state = self.state
        islander = state.islanders[name]
        islander.last_thought = text or play
        islander.inner_thoughts.append(
            InnerThought(
                day=state.day,
                phase=state.phase.value,
                tick=state.tick,
                text=text,
                play=action.play or "",
                action=action.type.value,
                target=action.target,
            )
        )
        event = LogEvent(
            day=state.day,
            phase=state.phase.value,
            tick=state.tick,
            kind="thought",
            actor=name,
            target=action.target,
            location=islander.location.value,
            visibility=Visibility.PRIVATE.value,
            text=text,
            thought=text,
            play=action.play or None,
            extra={"action": action.type.value, "play": action.play or ""},
        )
        self.log.write(event)
        remember(islander, event, limit=self.settings.memory_limit)

    def broadcast(self, event: LogEvent) -> None:
        vis = event.visibility
        if vis == Visibility.PUBLIC.value:
            audience = self.state.active()
        elif vis == Visibility.LOCATION.value:
            loc = Location(event.location) if event.location else None
            audience = [i for i in self.state.active() if loc and i.location == loc]
        elif vis == Visibility.WHISPER.value:
            names = set(event.participants)
            if event.actor:
                names.add(event.actor)
            if event.target:
                names.add(event.target)
            audience = [self.state.islanders[n] for n in names if n in self.state.islanders]
        else:
            audience = []
            if event.actor and event.actor in self.state.islanders:
                audience = [self.state.islanders[event.actor]]
        for person in audience:
            remember(person, event, limit=self.settings.memory_limit)

    def run_scene(self, speaker: str, target: str, opening: Action, whisper: bool) -> None:
        state = self.state
        sp = state.islanders[speaker]
        tg = state.islanders[target]
        if not whisper:
            sp.location = tg.location
        kind = "whisper" if whisper else "speak"
        vis = Visibility.WHISPER.value if whisper else Visibility.LOCATION.value
        turns = [
            (speaker, target, opening.content or f"{speaker} corners {target}.", opening.thought, opening)
        ]
        # Target replies, optional extra beats
        max_turns = max(2, min(self.settings.scene_turns, 4))
        last_line = opening.content or ""
        last_actor = speaker
        for beat in range(1, max_turns):
            actor = target if beat % 2 == 1 else speaker
            other = speaker if actor == target else target
            profile = self.profiles[actor]
            extra = (
                f"SCENE REPLY. {other} just said: {last_line!r}. "
                f"{in_character_nudge()} type=speak, target={other}."
            )
            action = self.decide(
                profile,
                [ActionType.SPEAK, ActionType.WHISPER, ActionType.PASS],
                extra,
                True,
            )
            line = action.content or f"{actor} looks at {other}."
            turns.append((actor, other, line, action.thought, action))
            last_line = line
            last_actor = actor
            if action.type == ActionType.PASS:
                break

        for actor, other, line, thought, action in turns:
            event = LogEvent(
                day=state.day,
                phase=state.phase.value,
                tick=state.tick,
                kind=kind,
                actor=actor,
                target=other,
                participants=[speaker, target],
                location=state.islanders[actor].location.value,
                visibility=vis,
                text=line,
                thought=thought,
                play=action.play or None,
            )
            self.log.write(event)
            self.broadcast(event)
            state.islanders[actor].last_thought = thought or ""
        note_chat(state, speaker, target, kind=kind)
        if not whisper:
            loc = tg.location.value
            record_moment(
                state,
                f"{speaker} and {target} had a public chat at the {loc}.",
            )

    def grafting_tick(self) -> None:
        state = self.state
        state.phase = Phase.GRAFTING
        busy: set[str] = set()
        order = state.active_names()
        random.Random(state.day * 100 + state.tick).shuffle(order)
        for name in order:
            if name in busy or state.islanders[name].dumped:
                continue
            profile = self.profiles[name]
            extra = grafting_nudge(self.settings.prize_emphasis)
            action = self.decide(profile, WORLD_ACTIONS, extra, False)
            me = state.islanders[name]
            me.last_thought = action.thought

            if action.type == ActionType.MOVE and action.location:
                me.location = action.location
                event = LogEvent(
                    day=state.day,
                    phase=state.phase.value,
                    tick=state.tick,
                    kind="move",
                    actor=name,
                    location=me.location.value,
                    visibility=Visibility.LOCATION.value,
                    text=action.content or f"{name} goes to the {me.location.value}.",
                    thought=action.thought,
                    play=action.play or None,
                )
                self.log.write(event)
                self.broadcast(event)
                continue

            if action.type == ActionType.DIARY:
                event = LogEvent(
                    day=state.day,
                    phase=state.phase.value,
                    tick=state.tick,
                    kind="diary",
                    actor=name,
                    location=Location.DIARY_ROOM.value,
                    visibility=Visibility.PRIVATE.value,
                    text=action.content or f"{name} checks in with the camera.",
                    thought=action.thought,
                    play=action.play or None,
                )
                self.log.write(event)
                self.broadcast(event)
                continue

            if action.type in (ActionType.SPEAK, ActionType.WHISPER) and action.target:
                if action.target in busy or action.target not in state.active_names():
                    event = LogEvent(
                        day=state.day,
                        phase=state.phase.value,
                        tick=state.tick,
                        kind="pass",
                        actor=name,
                        visibility=Visibility.PRIVATE.value,
                        text=f"{name} wanted {action.target} but they were busy.",
                        thought=action.thought,
                        play=action.play or None,
                    )
                    self.log.write(event)
                    continue
                busy.add(name)
                busy.add(action.target)
                self.run_scene(name, action.target, action, whisper=action.type == ActionType.WHISPER)
                continue

            event = LogEvent(
                day=state.day,
                phase=state.phase.value,
                tick=state.tick,
                kind="pass",
                actor=name,
                visibility=Visibility.PRIVATE.value,
                text=action.content or f"{name} clocks the room and stays put.",
                thought=action.thought,
                play=action.play or None,
            )
            self.log.write(event)

    def gender_talks(self, when: str) -> None:
        self.run_huddle("boy", "boys", Location.POOL, when)
        self.run_huddle("girl", "girls", Location.TERRACE, when)

    def run_huddle(self, gender: str, label: str, location: Location, when: str) -> None:
        state = self.state
        state.phase = Phase.BOYS_TALK if gender == "boy" else Phase.GIRLS_TALK
        names = [
            i.name
            for i in state.active()
            if self.profiles[i.name].gender == gender
        ]
        for name in names:
            state.islanders[name].location = location
        if len(names) < 2:
            if names:
                self.host.announce(
                    state,
                    f"{when.title()} {label} talk: not enough {label} left in the villa.",
                )
            return
        self.host.announce(
            state,
            f"{when.title()} {label} talk at the {location.value}. "
            f"Only {', '.join(names)} are here. The other group cannot hear this. "
            "Clock the couples, swap intel, plan recoupling"
            + prize_nudge(self.settings.prize_emphasis, " — this is for the £50,000", "")
            + "."
        )
        order = list(names)
        random.Random(state.day * 31 + hash((when, label))).shuffle(order)
        transcript: list[str] = []
        for name in order:
            others = [n for n in names if n != name]
            recent = "\n".join(transcript[-6:]) or "(you're opening the huddle)"
            extra = (
                f"{label.upper()} TALK ({when}). Same-gender huddle. "
                f"Here: {', '.join(names)}. Nobody of the other group can hear.\n"
                f"Huddle so far:\n{recent}\n"
                "Gossip, clock other couples, say who you'd recouple with"
                + prize_nudge(
                    self.settings.prize_emphasis,
                    ", protect your shot at £50,000. ",
                    ". ",
                )
                + f"type=speak, target MUST be one of: {', '.join(others)}."
            )
            profile = self.profiles[name]
            action = self.decide(
                profile,
                [ActionType.SPEAK, ActionType.WHISPER],
                extra,
                True,
            )
            action = validate_target(action, state, name, available=others)
            target = action.target if action.target in others else others[0]
            line = action.content or f"{name} looks at {target}."
            transcript.append(f"{name} → {target}: {line}")
            event = LogEvent(
                day=state.day,
                phase=state.phase.value,
                tick=state.tick,
                kind="huddle",
                actor=name,
                target=target,
                participants=names,
                location=location.value,
                visibility=Visibility.LOCATION.value,
                text=line,
                thought=action.thought,
                play=action.play or None,
            )
            self.log.write(event)
            self.broadcast(event)
            note_chat(state, name, target, kind="huddle")
        record_moment(
            state,
            f"{when.title()} {label} talk at the {location.value}: " + " | ".join(transcript)[:280],
        )

    def run_day(self, plan: DayPlan) -> None:
        state = self.state
        state.day = plan.day
        state.tick = 0
        self.host.morning(state)
        self.gender_talks("morning")
        if plan.bombshells:
            self.host.introduce_bombshells(state, plan.bombshells)
        for tick in range(plan.grafting_ticks):
            state.tick = tick + 1
            self.grafting_tick()
        if plan.challenge:
            self.host.challenge(state, self.decide, plan.challenge_name or "Villa Challenge")
        if plan.dates:
            self.host.dates(state, self.decide)
        self.gender_talks("evening")
        if plan.recoupling:
            pickers = plan.pickers or "girls"
            self.host.recoupling(
                state,
                self.decide,
                plan.recoupling_label or "Recoupling",
                pickers,
                dump_singles=plan.recoupling_dump_singles,
            )
        if plan.public_vote:
            self.host.public_vote_save(state, self.decide, plan.at_risk_count)
        if plan.dumping:
            self.host.dumping(state, self.decide, plan.dump_count, plan.dump_mode)
        if plan.diary and not plan.finale:
            self.host.diary_round(state, self.decide)
        if plan.finale:
            self.host.finale(state)
        print_day(state, self.log)
        brief = summarize_events(self.log.events)
        write_brief_log(brief, self.brief_path)
        print_brief_panel(brief, day=state.day)
        if state.season_over:
            print_finale(state)
        save_checkpoint(state, LOG_DIR / "run-state.json")

    def run(self) -> VillaState:
        print_open(
            self.state,
            self.profiles,
            stub=self.settings.stub,
            model=None if self.settings.stub else self.settings.default_model,
            settings=self.settings,
        )
        days = [d for d in self.schedule.days if d.day <= self.settings.season_days]
        for plan in days:
            self.run_day(plan)
            if self.state.season_over:
                break
        if not self.state.season_over:
            self.host.finale(self.state)
            print_finale(self.state)
            save_checkpoint(self.state, LOG_DIR / "run-state.json")
        return self.state


def run_season(settings: Settings | None = None) -> VillaState:
    return Simulation(settings).run()
