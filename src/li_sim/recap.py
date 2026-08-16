from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .config import Settings
from .logging_utils import EventLog
from .models import IslanderProfile, LogEvent, VillaState

console = Console()

KIND_STYLE = {
    "host": "bold magenta",
    "speak": "cyan",
    "whisper": "dim cyan",
    "diary": "yellow",
    "vote": "white",
    "couple_choice": "green",
    "dump": "bold red",
    "win": "bold gold1",
    "challenge": "bright_blue",
    "date": "pink1",
    "huddle": "bright_magenta",
    "move": "dim",
    "pass": "dim",
    "thought": "italic gold1",
}


def print_open(
    state: VillaState,
    profiles: dict[str, IslanderProfile],
    stub: bool,
    model: str | None = None,
    settings: Settings | None = None,
) -> None:
    settings = settings or Settings()
    intro = Text()
    intro.append(f"{state.season_name}\n", style="bold magenta")
    intro.append("Islanders. One villa. Stay coupled or go home.\n")
    intro.append(f"handles only · prize={settings.prize_emphasis}\n")
    if stub:
        intro.append("Mode: stub (no API calls)\n\n")
    else:
        intro.append("Mode: live LLM")
        if model:
            intro.append(f" · {model}")
        intro.append(" (you'll see each islander think before they act)\n\n")
    for p in profiles.values():
        late = f" · bombshell day {p.enters_on}" if p.enters_on > 1 else ""
        intro.append(f"{p.name}", style="bold")
        intro.append(f" — handle ({p.gender}s huddle){late}\n")
    console.print(Panel(intro, title="Love Island Agentic Simulation", border_style="magenta"))


def print_day(state: VillaState, log: EventLog) -> None:
    events = log.for_day(state.day)
    body = Text()
    for event in events:
        if event.kind == "pass" and not event.thought:
            continue
        if event.kind == "thought":
            continue
        _append_event(body, event)
    couples = ", ".join(f"{a} & {b}" for a, b in state.couples()) or "none"
    singles = ", ".join(state.singles()) or "—"
    dumped = ", ".join(state.dumped) or "—"
    footer = f"Couples: {couples}\nSingles: {singles}\nDumped: {dumped}"
    console.print(
        Panel(body, title=f"Day {state.day} — episode recap", border_style="magenta", subtitle=footer)
    )
    _contact_table(state)


def _append_event(body: Text, event: LogEvent) -> None:
    style = KIND_STYLE.get(event.kind, "white")
    prefix = {
        "whisper": "whisper",
        "diary": "diary",
        "host": "HOST",
        "vote": "vote",
        "couple_choice": "pick",
        "dump": "DUMP",
        "win": "WIN",
        "challenge": "challenge",
        "date": "date",
        "huddle": "huddle",
        "move": "move",
        "speak": "talk",
        "pass": "beat",
        "thought": "thinks",
    }.get(event.kind, event.kind)
    actor = event.actor or "?"
    body.append(f"[{prefix}] ", style=style)
    if event.kind == "thought":
        body.append(f"{actor}: ", style="bold")
        body.append(f"{event.text}\n", style="italic gold1")
        return
    if event.kind in {"speak", "whisper", "date", "huddle"} and event.target:
        body.append(f"{actor} → {event.target}: ", style="bold")
    elif event.actor:
        body.append(f"{actor}: ", style="bold")
    body.append(f"{event.text}\n")
    if event.thought:
        body.append(f"         thinks: {event.thought}\n", style="italic gold1")


def _contact_table(state: VillaState) -> None:
    names = state.active_names()
    table = Table(title="Talked with (talks / whispers)", show_lines=False, pad_edge=False)
    table.add_column("", style="bold")
    for n in names:
        table.add_column(n[:4], justify="right")
    for row in names:
        cells = [row]
        for col in names:
            if row == col:
                cells.append("—")
            else:
                log = state.islanders[row].contacts.get(col)
                if not log or (log.talks == 0 and log.whispers == 0):
                    cells.append("")
                else:
                    cells.append(f"{log.talks}/{log.whispers}")
        table.add_row(*cells)
    console.print(table)

    rep = Table(title="Public reputation")
    rep.add_column("Islander")
    rep.add_column("Score", justify="right")
    for name in sorted(names, key=lambda n: state.reputation.get(n, 0), reverse=True):
        rep.add_row(name, f"{state.reputation.get(name, 0):.1f}")
    console.print(rep)


def print_finale(state: VillaState) -> None:
    if state.winner_couple:
        w = " & ".join(state.winner_couple)
        console.print(Panel(f"Winners: {w}", title="Finale", border_style="gold1"))
    else:
        console.print(Panel("Season ended without a crowned couple.", border_style="red"))
