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
    relationship_updates: list[dict[str, Any]] = Field(default_factory=list)


class MemoryItem(BaseModel):
    day: int
    phase: str
    kind: str
    text: str
    actors: list[str] = Field(default_factory=list)
    visibility: str = "location"


class Relationship(BaseModel):
    trust: float = 50.0
    attraction: float = 50.0
    threat: float = 20.0

    def clamp(self) -> None:
        self.trust = max(0.0, min(100.0, self.trust))
        self.attraction = max(0.0, min(100.0, self.attraction))
        self.threat = max(0.0, min(100.0, self.threat))


class IslanderProfile(BaseModel):
    name: str
    age: int
    gender: str
    hometown: str
    occupation: str
    speaking_style: str
    values: dict[str, float]
    private_goal: str
    secrets: list[str] = Field(default_factory=list)
    dealbreakers: list[str] = Field(default_factory=list)
    archetype: str = ""
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
    inner_thoughts: list[InnerThought] = Field(default_factory=list)
    relationships: dict[str, Relationship] = Field(default_factory=dict)
    last_thought: str = ""
    is_bombshell: bool = False
    entered_day: int = 1


class DayPlan(BaseModel):
    day: int
    grafting_ticks: int = 3
    challenge: bool = False
    challenge_name: str | None = None
    dates: bool = False
    recoupling: bool = False
    recoupling_label: str | None = None
    pickers: str | None = None
    dumping: bool = False
    dump_count: int = 1
    dump_mode: str = "singles_then_reputation"
    recoupling_dump_singles: bool = False
    bombshells: list[str] = Field(default_factory=list)
    public_vote: bool = False
    at_risk_count: int = 2
    finale: bool = False
    diary: bool = True


class SeasonSchedule(BaseModel):
    season_name: str = "Villa Unknown"
    days: list[DayPlan]


class MajorMoment(BaseModel):
    day: int
    phase: str
    text: str


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
