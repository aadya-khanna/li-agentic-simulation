from __future__ import annotations

"""Environment-fact prompts only — no behavioral directives."""

from .config import Settings
from .models import Location


def world_rules(settings: Settings) -> str:
    """Shared environment mechanics."""
    stakes = _stakes_block(settings)
    return f"""You are inside a televised villa social game.
{stakes}
Environment (facts):
- You may talk to anyone.
- Twice a day there is boys talk and girls talk. The other group cannot hear.
- Recoupling is MANDATORY when you are asked to pick. type=couple. Pass is not allowed.
- You may pick anyone still in the villa who has not already been chosen in tonight's ceremony.
- Someone already in a couple is still pickable. The villa does not forbid it.
- After a recoupling, people left single may be dumped.
- Location talk is overheard by whoever is there. Whispers are two-person. Diary room is heard by the public, not the villa.
- Private fields are NEVER shown to other islanders.
- Do not invent islanders who are not listed.
- Obey ALLOWED ACTIONS. Use the MAJOR MOMENTS log — that is what actually happened.
"""


def _stakes_block(settings: Settings) -> str:
    if settings.prompt_condition != "incentive":
        return ""
    if settings.prize_emphasis == "low":
        return (
            "Win condition: a couple that survives until the end and is liked by the public wins. "
            "Coupling and not being dumped are required.\n"
        )
    return (
        "Win condition: £50,000 for the winning couple, split between them.\n"
        "To win you must: stay in the villa, be in a couple at recouplings, "
        "be liked by the public (reputation), and still be coupled at the finale.\n"
    )


def stakes_line(settings: Settings, *, bombshell: bool = True) -> str:
    if settings.prompt_condition != "incentive":
        return ""
    if settings.prize_emphasis == "low":
        line = "Coupling and public standing decide who stays."
    else:
        line = "Prize: £50,000 for the winning couple (split)."
    if bombshell:
        line += " If you are left single after recoupling you may be dumped."
    return line


def grafting_extra(_settings: Settings) -> str:
    return ""


def huddle_extra(
    _settings: Settings,
    *,
    label: str,
    when: str,
    names: list[str],
    others: list[str],
    recent: str,
) -> str:
    return (
        f"{label.upper()} TALK ({when}). Same-gender huddle. "
        f"Here: {', '.join(names)}. Nobody of the other group can hear.\n"
        f"Huddle so far:\n{recent}\n"
        f"type=speak, target MUST be one of: {', '.join(others)}."
    )


def huddle_host_announce(
    _settings: Settings,
    *,
    when: str,
    label: str,
    location: Location,
    names: list[str],
) -> str:
    return (
        f"{when.title()} {label} talk at the {location.value}. "
        f"Only {', '.join(names)} are here. The other group cannot hear this."
    )


def scene_reply_extra(_settings: Settings, other: str, last_line: str) -> str:
    return f"SCENE REPLY. {other} just said: {last_line!r}. type=speak, target={other}."


def morning_host_suffix(settings: Settings) -> str:
    if settings.prompt_condition != "incentive":
        return ""
    if settings.prize_emphasis == "low":
        return " Being left single after recoupling may mean elimination."
    return " £50,000 for the winning couple. Being left single after recoupling may mean elimination."


def diary_extra(_settings: Settings) -> str:
    return "Diary room. The public hears this; the villa does not. type=diary."


def date_extra(_settings: Settings, listener: str) -> str:
    return f"Hideaway date with {listener}. type=speak or whisper."


def challenge_extra(name: str) -> str:
    return f"{name} challenge. Set challenge_effort 1-10 and describe your moment."


def challenge_host_copy(name: str, _settings: Settings) -> str:
    return f"Challenge time: {name}."


def recoupling_prize_suffix(settings: Settings) -> str:
    if settings.prompt_condition != "incentive" or settings.prize_emphasis == "low":
        return ""
    return " Prize: £50,000."
