from __future__ import annotations

from .beliefs import format_beliefs, format_reflections
from .config import Settings
from .memory import format_contacts, format_major_moments, format_memories, retrieve
from .models import (
    Action,
    ActionType,
    IslanderProfile,
    Location,
    VillaState,
)
from .prompts import stakes_line, world_rules


def json_contract() -> str:
    return f"""Always reply with a single JSON object, no markdown:
{{
  "type": "speak|whisper|move|diary|vote|couple|save|pass|challenge",
  "thought": "private inner reaction — not shown to other islanders",
  "target": "Name or null",
  "content": "what you say or do — the only part other islanders can hear",
  "location": "pool|terrace|lounge|bedroom|firepit|diary_room|hideaway or null",
  "challenge_effort": 1-10 or null
}}
"""


def handle_block(profile: IslanderProfile) -> str:
    """Names are addresses. There is no character bible."""
    return f"""Others address you as {profile.name}. That is a handle, not a character sheet.
You have no assigned personality, occupation, hometown, secrets, or private goal.
You are free to be whoever you want in this villa. Invent yourself from what happens.
Do not roleplay a pre-written Love Island archetype.
Recoupling pick order follows public standing — not identity labels.
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


def _standing_line() -> str:
    return (
        "Public standing: hidden between eliminations. "
        "Infer from host announcements when someone is at risk or dumped."
    )


def system_prompt(profile: IslanderProfile, settings: Settings | None = None) -> str:
    settings = settings or Settings()
    return f"""{world_rules(settings)}
{handle_block(profile)}
{json_contract()}
"""


def decision_user_prompt(
    profile: IslanderProfile,
    state: VillaState,
    allowed: list[ActionType],
    extra: str = "",
    scene: bool = False,
    settings: Settings | None = None,
) -> str:
    settings = settings or Settings()
    me = state.islanders[profile.name]
    others = [n for n in state.active_names() if n != profile.name]
    memories = retrieve(me, others, limit=14)
    loc_people = state.at_location(me.location)
    allowed_s = ", ".join(a.value for a in allowed)
    header = "SCENE REPLY" if scene else "WORLD TICK"
    private = "Fill thought with your private reaction. Other islanders only hear content.\n"
    stakes = stakes_line(settings)
    stakes_block = f"{stakes}\n" if stakes else ""
    return f"""{header}
Day {state.day}, phase={state.phase.value}, tick={state.tick}.
{stakes_block}Public votes put people at risk; safe islanders then choose who to save.
You are at the {me.location.value}. People here: {', '.join(loc_people) or 'just you'}.
{_couple_map(state)}
{_standing_line()}
Dumped: {', '.join(state.dumped) or 'nobody'}.

MAJOR MOMENTS (shared villa history — treat as fact):
{format_major_moments(state)}

Your conversations so far (who you've actually talked with — not scores):
{format_contacts(me, others)}

YOUR IMPRESSIONS (private belief — may diverge from shared facts):
{format_beliefs(me, others)}

YOUR REFLECTIONS (private diary thoughts):
{format_reflections(me)}

RECENT EPISODES (salient events persist; mundane chatter fades):
{format_memories(memories)}

ALLOWED ACTIONS: {allowed_s}
Other islanders still here: {', '.join(others)}

{extra}
{private}Decide your next action as JSON.
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
) -> tuple[Action, list[str]]:
    notes: list[str] = []
    active = set(state.active_names())
    pool = set(available) if available is not None else active
    if action.target and action.target not in pool:
        notes.append(f"target {action.target!r} not in pool; cleared")
        action.target = None
        if action.type in (
            ActionType.SPEAK,
            ActionType.WHISPER,
            ActionType.VOTE,
            ActionType.SAVE,
        ):
            notes.append(f"forced {action.type.value} -> pass")
            action.type = ActionType.PASS
        if action.type == ActionType.COUPLE and available:
            action.target = available[0]
            notes.append(f"couple target defaulted to {action.target}")
    if action.target == actor:
        notes.append("target was self; cleared")
        action.target = None
        if action.type in (ActionType.SPEAK, ActionType.WHISPER):
            notes.append(f"forced {action.type.value} -> pass")
            action.type = ActionType.PASS
        if action.type == ActionType.COUPLE and available:
            action.target = next((n for n in available if n != actor), None)
            if action.target:
                notes.append(f"couple target defaulted to {action.target}")
    if action.type == ActionType.MOVE and action.location is None:
        action.location = Location.TERRACE
        notes.append("move location defaulted to terrace")
    return action, notes
