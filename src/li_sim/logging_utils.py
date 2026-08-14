from __future__ import annotations

import json
from pathlib import Path

from .models import LogEvent, VillaState


class EventLog:
    def __init__(self, path: Path):
        self.path = path
        self.thoughts_path = path.parent / "thoughts.jsonl"
        self.events: list[LogEvent] = []
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("", encoding="utf-8")
        self.thoughts_path.write_text("", encoding="utf-8")

    def write(self, event: LogEvent) -> LogEvent:
        self.events.append(event)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(event.model_dump_json() + "\n")
        if event.kind == "thought":
            with self.thoughts_path.open("a", encoding="utf-8") as handle:
                handle.write(event.model_dump_json() + "\n")
        return event

    def for_day(self, day: int) -> list[LogEvent]:
        return [e for e in self.events if e.day == day]


def save_checkpoint(state: VillaState, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(state.model_dump_json(indent=2), encoding="utf-8")


def load_events(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows
