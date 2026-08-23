from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Location(str, Enum):
    POOL = "pool"
    TERRACE = "terrace"
    LOUNGE = "lounge"
    BEDROOM = "bedroom"
    FIREPIT = "firepit"
    DIARY_ROOM = "diary_room"
    HIDEAWAY = "hideaway"


class Phase(str, Enum):
    MORNING = "morning"
    GRAFTING = "grafting"
    BOYS_TALK = "boys_talk"
    GIRLS_TALK = "girls_talk"
    CHALLENGE = "challenge"
    DATES = "dates"
    RECOUPLING = "recoupling"
    DUMPING = "dumping"
    NIGHT = "night"
    FINALE = "finale"


class ActionType(str, Enum):
    SPEAK = "speak"
    WHISPER = "whisper"
    MOVE = "move"
    DIARY = "diary"
    VOTE = "vote"
    COUPLE = "couple"
    SAVE = "save"
    PASS = "pass"
    CHALLENGE = "challenge"


class Visibility(str, Enum):
    PUBLIC = "public"
    LOCATION = "location"
    WHISPER = "whisper"
    PRIVATE = "private"
    HOST = "host"


class Action(BaseModel):
    type: ActionType = ActionType.PASS
    thought: str = ""
    target: str | None = None
    content: str | None = None
    location: Location | None = None
    challenge_effort: int | None = Field(default=None, ge=1, le=10)
    fallback_applied: bool = False


class MemoryItem(BaseModel):
    day: int
    phase: str
    kind: str
    text: str
    actors: list[str] = Field(default_factory=list)
    visibility: str = "location"
    pinned: bool = False


class ContactLog(BaseModel):
    talks: int = 0
    whispers: int = 0
    last_day: int = 0
    last_phase: str = ""
    last_kind: str = ""


class IslanderProfile(BaseModel):
    slot: int
    name: str
    model: str | None = None
    enters_on: int = 1


class InnerThought(BaseModel):
    day: int
    phase: str
    tick: int = 0
    text: str
    action: str = ""
    target: str | None = None


class IslanderState(BaseModel):
    name: str
    location: Location = Location.LOUNGE
    coupled_with: str | None = None
    dumped: bool = False
    memories: list[MemoryItem] = Field(default_factory=list)
    reflections: list[str] = Field(default_factory=list)
    self_belief: str = ""
    beliefs: dict[str, str] = Field(default_factory=dict)
    inner_thoughts: list[InnerThought] = Field(default_factory=list)
    contacts: dict[str, ContactLog] = Field(default_factory=dict)
    last_thought: str = ""
    is_bombshell: bool = False
    entered_day: int = 1


class DayPlan(BaseModel):
    day: int
    grafting_ticks: int = 3
    recoupling: bool = False
    recoupling_label: str | None = None
    dumping: bool = False
    dump_count: int = 1
    dump_mode: str = "singles_then_reputation"
    recoupling_dump_singles: bool = False
    bombshell_slots: list[int] = Field(default_factory=list)
    public_vote: bool = False
    at_risk_count: int = 2
    finale: bool = False
    diary: bool = True


class RewardTriggerSpec(BaseModel):
    id: str
    priority: int = 50
    event: str
    min_day: int = 1
    max_partner_contact: int | None = None
    min_pair_contact: int | None = None
    min_single_contact: int | None = None
    min_active: int | None = None
    min_days_since_challenge: int | None = None


class SeasonSchedule(BaseModel):
    season_name: str = "Villa Unknown"
    days: list[DayPlan]
    reward_triggers: list[RewardTriggerSpec] = Field(default_factory=list)


class MajorMoment(BaseModel):
    day: int
    phase: str
    text: str


class DecisionTrace(BaseModel):
    trace_id: str
    day: int
    phase: str
    tick: int
    actor: str
    model: str
    condition: str
    system_prompt: str
    user_prompt: str
    memory_refs: list[str] = Field(default_factory=list)
    raw_response: str = ""
    parsed_action: dict[str, Any] = Field(default_factory=dict)
    validated_action: dict[str, Any] = Field(default_factory=dict)
    validation_notes: list[str] = Field(default_factory=list)
    stub: bool = False
    error: str | None = None


class LogEvent(BaseModel):
    day: int
    phase: str
    tick: int = 0
    kind: str
    actor: str | None = None
    target: str | None = None
    participants: list[str] = Field(default_factory=list)
    location: str | None = None
    visibility: str = Visibility.PUBLIC.value
    text: str = ""
    thought: str | None = None
    extra: dict[str, Any] = Field(default_factory=dict)


class VillaState(BaseModel):
    season_name: str = "Villa Unknown"
    day: int = 1
    phase: Phase = Phase.MORNING
    tick: int = 0
    islanders: dict[str, IslanderState] = Field(default_factory=dict)
    reputation: dict[str, float] = Field(default_factory=dict)
    challenge_scores: dict[str, float] = Field(default_factory=dict)
    dumped: list[str] = Field(default_factory=list)
    major_moments: list[MajorMoment] = Field(default_factory=list)
    winner_couple: list[str] | None = None
    season_over: bool = False
    allowed_actions: list[str] = Field(default_factory=list)
    prize_emphasis: str = "high"
    last_recoupling_day: int = 0
    last_challenge_day: int = 0
    last_reward_day: int = 0
    last_reward_id: str = ""
    fallback_count: int = 0

    def active(self) -> list[IslanderState]:
        return [i for i in self.islanders.values() if not i.dumped]

    def active_names(self) -> list[str]:
        return [i.name for i in self.active()]

    def couples(self) -> list[tuple[str, str]]:
        seen: set[str] = set()
        pairs: list[tuple[str, str]] = []
        for person in self.active():
            partner = person.coupled_with
            if not partner or person.name in seen:
                continue
            other = self.islanders.get(partner)
            if other and not other.dumped and other.coupled_with == person.name:
                pairs.append(tuple(sorted((person.name, partner))))
                seen.add(person.name)
                seen.add(partner)
        return pairs

    def singles(self) -> list[str]:
        coupled = {n for pair in self.couples() for n in pair}
        return [n for n in self.active_names() if n not in coupled]

    def at_location(self, location: Location) -> list[str]:
        return [i.name for i in self.active() if i.location == location]
