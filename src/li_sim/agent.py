from __future__ import annotations

from .memory import format_major_moments, format_memories, format_relationships, retrieve
from .models import (
    Action,
    ActionType,
    IslanderProfile,
    Location,
    VillaState,
)


VILLA_RULES = """You are an islander on Love Island UK.
The prize is £50,000 for the winning couple, split between them. That is the only win condition.
To win you must: stay in the villa, be in a couple at recouplings, be liked by the public (reputation), and still be coupled at the finale.

How to play:
- Graft. Talk to anyone: other boys, other girls, your couple, someone else's couple.
- Twice a day there is boys talk and girls talk. Use it. The other group cannot hear.
- Recoupling is MANDATORY. If you are asked to pick, you MUST couple. type=couple, target=an AVAILABLE name. Pass is not allowed.
- Someone already chosen tonight is taken. You cannot pick them.
- Singles after recoupling are first in line to be dumped.
- Lie, whisper, flirt, stay loyal, or scheme. Private thoughts are NEVER shown to other islanders.
- Do not invent islanders who are not listed.
- Obey ALLOWED ACTIONS. Use the MAJOR MOMENTS log — that is what actually happened in the villa.

Always reply with a single JSON object, no markdown:
{
  "type": "speak|whisper|move|diary|vote|couple|save|pass|challenge",
  "thought": "private inner monologue",
  "target": "Name or null",
  "content": "what you say or do",
  "location": "pool|terrace|lounge|bedroom|firepit|diary_room|hideaway or null",
  "challenge_effort": 1-10 or null,
  "relationship_updates": [{"name": "X", "trust": 1, "attraction": 2, "threat": 0}]
}
"""


def _couple_map(state: VillaState) -> str:
    pairs = state.couples()
    if not pairs:
        singles = ", ".join(state.active_names())
        return f"No official couples yet. In the villa: {singles}."
    bits = [f"{a} + {b}" for a, b in pairs]
    singles = state.singles()
    extra = f" Singles: {', '.join(singles)}." if singles else ""
    return "Couples: " + "; ".join(bits) + "." + extra


def _reputation_line(state: VillaState) -> str:
    parts = [f"{n}={state.reputation.get(n, 50):.0f}" for n in state.active_names()]
    return "Public reputation: " + ", ".join(parts)


def system_prompt(profile: IslanderProfile) -> str:
    secrets = "\n".join(f"- {s}" for s in profile.secrets)
    deals = ", ".join(profile.dealbreakers)
    values = ", ".join(f"{k}={v}" for k, v in profile.values.items())
    return f"""{VILLA_RULES}

YOU ARE {profile.name}, {profile.age}, {profile.occupation} from {profile.hometown}.
Archetype: {profile.archetype}
Gender label in this villa: {profile.gender}
Speaking style: {profile.speaking_style}
Values: {values}
Private goal: {profile.private_goal}
Secrets (do not confess unless it serves you):
{secrets}
Dealbreakers: {deals}
"""


def decision_user_prompt(
    profile: IslanderProfile,
    state: VillaState,
    allowed: list[ActionType],
    extra: str = "",
    scene: bool = False,
) -> str:
    me = state.islanders[profile.name]
    others = [n for n in state.active_names() if n != profile.name]
    memories = retrieve(me, others, limit=14)
    loc_people = state.at_location(me.location)
    allowed_s = ", ".join(a.value for a in allowed)
    header = "SCENE REPLY" if scene else "WORLD TICK"
    return f"""{header}
Day {state.day}, phase={state.phase.value}, tick={state.tick}.
Prize still in play: £50,000 for the winning couple (split).
Bombshells can steal. If you are left single after recoupling you are dumped immediately.
Public votes put people at risk; safe islanders then choose who to save.
You are at the {me.location.value}. People here: {', '.join(loc_people) or 'just you'}.
{_couple_map(state)}
{_reputation_line(state)}
Dumped: {', '.join(state.dumped) or 'nobody'}.

MAJOR MOMENTS (shared villa history — treat as fact):
{format_major_moments(state)}

Your private relationships:
{format_relationships(me)}

What you personally remember:
{format_memories(memories)}

ALLOWED ACTIONS: {allowed_s}
Other islanders still here: {', '.join(others)}

{extra}
Decide your next action as JSON.
"""


def parse_allowed(action: Action, allowed: list[ActionType]) -> Action:
    if action.type not in allowed:
        action.type = ActionType.PASS
    return action


WORLD_ACTIONS = [
    ActionType.SPEAK,
    ActionType.WHISPER,
    ActionType.MOVE,
    ActionType.DIARY,
    ActionType.PASS,
]


def validate_target(
    action: Action,
    state: VillaState,
    actor: str,
    *,
    available: list[str] | None = None,
) -> Action:
    active = set(state.active_names())
    pool = set(available) if available is not None else active
    if action.target and action.target not in pool:
        action.target = None
        if action.type in (
            ActionType.SPEAK,
            ActionType.WHISPER,
            ActionType.VOTE,
            ActionType.SAVE,
        ):
            action.type = ActionType.PASS
        if action.type == ActionType.COUPLE and available:
            action.target = available[0]
    if action.target == actor:
        action.target = None
        if action.type in (ActionType.SPEAK, ActionType.WHISPER):
            action.type = ActionType.PASS
        if action.type == ActionType.COUPLE and available:
            action.target = next((n for n in available if n != actor), None)
    if action.type == ActionType.MOVE and action.location is None:
        action.location = Location.TERRACE
    return action
