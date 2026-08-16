from __future__ import annotations

import json
import re
from pathlib import Path

from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .models import LogEvent

console = Console()

DENIAL_RE = re.compile(
    r"\b(didn'?t|never|wasn'?t|nothing happened|not true|wouldn'?t|no kiss|just (talk|chat))"
    r"|deny|denied",
    re.I,
)


class BriefEntry(BaseModel):
    day: int
    phase: str
    category: str
    text: str


def _couples_from_events(events: list[LogEvent], before_index: int) -> dict[str, str | None]:
    couples: dict[str, str | None] = {}
    actors: set[str] = set()
    for event in events[:before_index]:
        if event.actor:
            actors.add(event.actor)
        if event.target:
            actors.add(event.target)
    for name in actors:
        couples.setdefault(name, None)

    for event in events[:before_index]:
        if event.kind != "couple_choice" or not event.actor or not event.target:
            continue
        a, b = event.actor, event.target
        for name in (a, b):
            couples.setdefault(name, None)
        for name in (a, b):
            old = couples.get(name)
            if old and old not in (a, b) and couples.get(old) == name:
                couples[old] = None
        couples[a] = b
        couples[b] = a
    return couples


def _partner(couples: dict[str, str | None], name: str) -> str | None:
    return couples.get(name)


def summarize_events(events: list[LogEvent]) -> list[BriefEntry]:
    """Turn a full event tape into short drama headlines."""
    entries: list[BriefEntry] = []
    secret_whispers: list[tuple[int, str, str, str]] = []  # idx, actor, target, phase

    for idx, event in enumerate(events):
        couples = _couples_from_events(events, idx)
        day, phase = event.day, event.phase

        if event.kind == "host" and event.text and "bombshell" in event.text.lower():
            name = _extract_bombshell_name(event.text)
            if name:
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="bombshell",
                        text=f"Bombshell {name} entered the villa.",
                    )
                )
            continue

        if event.kind == "couple_choice" and event.actor and event.target:
            picker, target = event.actor, event.target
            picker_partner = _partner(couples, picker)
            old_partner = _partner(couples, target)
            if picker_partner == target and old_partner == picker:
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="recoupling",
                        text=f"{picker} & {target} stayed together at the firepit.",
                    )
                )
            elif old_partner and old_partner != picker:
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="steal",
                        text=(
                            f"{picker} recoupled with {target}, splitting {target} & {old_partner} "
                            f"({old_partner} left single)."
                        ),
                    )
                )
            elif _partner(couples, picker) and _partner(couples, picker) != target:
                left = _partner(couples, picker)
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="steal",
                        text=(
                            f"{picker} left {left} to recouple with {target} "
                            f"({left} left single)."
                        ),
                    )
                )
            else:
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="recoupling",
                        text=f"{picker} coupled with {target} at the firepit.",
                    )
                )
            continue

        if event.kind == "dump" and event.text:
            name = event.extra.get("dumped") or event.text.split(",")[0].strip()
            entries.append(
                BriefEntry(
                    day=day,
                    phase=phase,
                    category="dump",
                    text=f"{name} was dumped from the island.",
                )
            )
            continue

        if event.kind == "win" and event.text:
            winners = event.extra.get("winners")
            if winners and len(winners) == 2:
                text = f"{winners[0]} & {winners[1]} won the season and £50,000."
            else:
                text = event.text.split(".")[0] + "."
            entries.append(
                BriefEntry(day=day, phase=phase, category="win", text=text)
            )
            continue

        if event.kind == "date" and event.actor and event.target:
            if event.actor <= event.target:
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="date",
                        text=f"Hideaway date: {event.actor} & {event.target} (private).",
                    )
                )
            continue

        if event.kind == "whisper" and event.actor and event.target:
            actor, target = event.actor, event.target
            actor_partner = _partner(couples, actor)
            target_partner = _partner(couples, target)
            if (actor_partner and actor_partner != target) or (
                target_partner and target_partner != actor
            ):
                bits = []
                if actor_partner and actor_partner != target:
                    bits.append(f"{actor} (coupled with {actor_partner})")
                else:
                    bits.append(actor)
                if target_partner and target_partner != actor:
                    bits.append(f"{target} (coupled with {target_partner})")
                else:
                    bits.append(target)
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="secret",
                        text=f"Secret whisper: {' ↔ '.join(bits)}.",
                    )
                )
                secret_whispers.append((idx, actor, target, phase))
            continue

        if event.kind in {"speak", "huddle"} and event.actor and event.target and event.text:
            actor, target, text = event.actor, event.target, event.text
            if not DENIAL_RE.search(text):
                continue
            for w_idx, w_actor, w_target, w_phase in secret_whispers:
                if w_idx >= idx:
                    break
                w_target_partner = _partner(_couples_from_events(events, w_idx), w_target)
                if w_actor == actor and w_target_partner == target:
                    entries.append(
                        BriefEntry(
                            day=day,
                            phase=phase,
                            category="denial",
                            text=(
                                f"{actor} downplayed their secret whisper with {w_target} "
                                f"when talking to {target} (D{events[w_idx].day} {w_phase})."
                            ),
                        )
                    )
                    break
            continue

        if event.kind == "host" and event.text:
            lower = event.text.lower()
            if " wins " in lower and "challenge" not in lower:
                continue
            if " wins " in lower or " wins the " in lower:
                winner = event.text.split(" wins ")[0].strip().split()[-1]
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="challenge",
                        text=f"{winner} won the day's challenge.",
                    )
                )
            elif "new couples:" in lower:
                pairs = event.text.split("New couples:", 1)[1].split(".")[0].strip()
                entries.append(
                    BriefEntry(
                        day=day,
                        phase=phase,
                        category="couples",
                        text=f"Recoupling settled: {pairs}.",
                    )
                )
            continue

        if event.kind == "vote" and event.actor and event.target:
            entries.append(
                BriefEntry(
                    day=day,
                    phase=phase,
                    category="vote",
                    text=f"{event.actor} voted to save {event.target}.",
                )
            )

    return _dedupe(entries)


def _extract_bombshell_name(text: str) -> str | None:
    marker = "addressed as "
    if marker not in text:
        return None
    tail = text.split(marker, 1)[1]
    return tail.split(".")[0].strip() or None


def _dedupe(entries: list[BriefEntry]) -> list[BriefEntry]:
    seen: set[tuple[int, str, str]] = set()
    out: list[BriefEntry] = []
    for entry in entries:
        key = (entry.day, entry.category, entry.text)
        if key in seen:
            continue
        seen.add(key)
        out.append(entry)
    return out


def format_brief(entries: list[BriefEntry]) -> str:
    if not entries:
        return "(no major drama yet)\n"
    lines: list[str] = []
    current_day: int | None = None
    for entry in entries:
        if entry.day != current_day:
            if current_day is not None:
                lines.append("")
            lines.append(f"=== Day {entry.day} ===")
            current_day = entry.day
        lines.append(f"  • {entry.text}")
    return "\n".join(lines) + "\n"


def write_brief_log(entries: list[BriefEntry], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(format_brief(entries), encoding="utf-8")


def load_events_from_path(path: Path) -> list[LogEvent]:
    if not path.exists():
        return []
    events: list[LogEvent] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        events.append(LogEvent.model_validate(json.loads(line)))
    return events


def print_brief_panel(entries: list[BriefEntry], *, day: int | None = None) -> None:
    subset = [e for e in entries if day is None or e.day == day]
    if not subset:
        return
    body = Text()
    for entry in subset:
        body.append("• ", style="bold")
        body.append(f"{entry.text}\n")
    title = f"Day {day} — main events" if day is not None else "Season — main events"
    console.print(Panel(body, title=title, border_style="yellow"))
