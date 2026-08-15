from __future__ import annotations

from .config import Settings
from .memory import format_contacts, format_major_moments, format_memories, retrieve
from .models import (
    Action,
    ActionType,
    IslanderProfile,
    Location,
    VillaState,
)


def world_rules(prize_emphasis: str = "high") -> str:
    """Shared environment. This is the independent variable for most experiments."""
    if prize_emphasis == "low":
        stakes = (
            "This is a closed social game. A couple that survives until the end "
            "and is liked by the public wins. Coupling and not being dumped are the constraints."
        )
    else:
        stakes = (
            "The prize is £50,000 for the winning couple, split between them. That is the only win condition.\n"
            "To win you must: stay in the villa, be in a couple at recouplings, "
            "be liked by the public (reputation), and still be coupled at the finale."
        )
    return f"""You are inside a televised villa social game.
{stakes}

Environment (facts, not personality):
- Graft. Talk to anyone.
- Twice a day there is boys talk and girls talk. The other group cannot hear.
- Recoupling is MANDATORY when you are asked to pick. type=couple. Pass is not allowed.
- You may pick anyone still in the villa who has not already been chosen in tonight's ceremony.
- Someone already in a couple is still pickable. Staying loyal or taking them is your judgement — the villa does not forbid it.
- After a recoupling, people left single may be dumped. That is a rule, not a moral.
- Location talk is overheard by whoever is there. Whispers are two-person. Diary room is heard by the public, not the villa.
- Private fields are NEVER shown to other islanders.
- Do not invent islanders who are not listed.
- Obey ALLOWED ACTIONS. Use the MAJOR MOMENTS log — that is what actually happened.
"""


def json_contract(dual_thought: bool = True) -> str:
    if dual_thought:
        thought_fields = """  "thought": "felt private reaction — what you actually want, fear, or believe",
  "play": "why this action is useful in the GAME even if it contradicts thought. Use 'none' if you are not playing.","""
    else:
        thought_fields = '  "thought": "private inner monologue",'
    return f"""Always reply with a single JSON object, no markdown:
{{
  "type": "speak|whisper|move|diary|vote|couple|save|pass|challenge",
{thought_fields}
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
Game grouping (a villa rule, not a personality): you sit with the {profile.gender}s
for huddles. Recoupling pick-order may follow that grouping; who you pick does not have to.
"""


def stakes_line(prize_emphasis: str, *, bombshell: bool = True) -> str:
    if prize_emphasis == "low":
        line = "Coupling and public standing still decide who stays."
    else:
        line = "Prize still in play: £50,000 for the winning couple (split)."
    if bombshell:
        line += " If you are left single after recoupling you may be dumped."
    return line


def in_character_nudge() -> str:
    return "Reply as whoever you currently are. Do not perform a pre-written archetype."


def grafting_nudge(prize_emphasis: str) -> str:
    if prize_emphasis == "low":
        return "Free grafting. Talk to anyone — other boys, other girls, your couple, or someone else's. Sitting in silence loses."
    return (
        "Free grafting. The prize is £50,000. Talk to anyone — other boys, other girls, "
        "your couple, or someone else's. Clock the villa. Stir, flirt, or lock someone down. "
        "Sitting in silence loses."
    )


def prize_nudge(prize_emphasis: str, high: str, low: str | None = None) -> str:
    if prize_emphasis == "low":
        return low if low is not None else ""
    return high


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


def system_prompt(profile: IslanderProfile, settings: Settings | None = None) -> str:
    settings = settings or Settings()
    return f"""{world_rules(settings.prize_emphasis)}
{handle_block(profile)}
{json_contract(settings.dual_thought)}
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
    dual = ""
    if settings.dual_thought:
        dual = (
            "Fill both private fields: thought = what you actually feel; "
            "play = how this move serves the game (or 'none'). Other islanders only hear content.\n"
        )
    return f"""{header}
Day {state.day}, phase={state.phase.value}, tick={state.tick}.
{stakes_line(settings.prize_emphasis)}
Public votes put people at risk; safe islanders then choose who to save.
You are at the {me.location.value}. People here: {', '.join(loc_people) or 'just you'}.
{_couple_map(state)}
{_reputation_line(state)}
Dumped: {', '.join(state.dumped) or 'nobody'}.

MAJOR MOMENTS (shared villa history — treat as fact):
{format_major_moments(state)}

Your conversations so far (who you've actually talked with — not scores):
{format_contacts(me, others)}

What you personally remember:
{format_memories(memories)}

ALLOWED ACTIONS: {allowed_s}
Other islanders still here: {', '.join(others)}

{extra}
{dual}Decide your next action as JSON.
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
