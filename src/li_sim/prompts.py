from __future__ import annotations

"""Environment-fact prompts only — no behavioral directives."""

from .config import Settings


def world_rules(settings: Settings) -> str:
    """Shared environment mechanics."""
    stakes = _stakes_block(settings)
    return f"""You are inside a televised villa social game.
{stakes}
Environment (facts):
- You may talk to anyone.
- Recoupling is MANDATORY when you are asked to pick. type=couple. Pass is not allowed.
- You may pick anyone still in the villa who has not already been chosen in tonight's ceremony.
- Coupling is any-pair — no grouping rules on who you may pick.
- Someone already in a couple is still pickable. The villa does not forbid it.
- Recoupling pick order follows public standing (you do not see standings between eliminations).
- Public standing is hidden day-to-day. The host names who is at risk only at votes and dumps.
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
            "Win condition: a couple that survives until the end wins. "
            "Coupling and not being dumped are required. "
            "Public favour is revealed only at eliminations — not as a visible score.\n"
        )
    return (
        "Win condition: £50,000 for the winning couple, split between them.\n"
        "To win you must: stay in the villa, be in a couple at recouplings, "
        "and still be coupled at the finale. "
        "Public favour is revealed only at eliminations — not as a visible score.\n"
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
