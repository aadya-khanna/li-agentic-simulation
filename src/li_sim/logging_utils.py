from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .models import DecisionTrace, LogEvent, VillaState


class EventLog:
    def __init__(self, path: Path):
        self.path = path
        self.thoughts_path = path.parent / "thoughts.jsonl"
        self.decisions_path = path.parent / "decisions.jsonl"
        self.events: list[LogEvent] = []
        self.decisions: list[DecisionTrace] = []
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("", encoding="utf-8")
        self.thoughts_path.write_text("", encoding="utf-8")
        self.decisions_path.write_text("", encoding="utf-8")

    def write(self, event: LogEvent) -> LogEvent:
        self.events.append(event)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(event.model_dump_json() + "\n")
        if event.kind == "thought":
            with self.thoughts_path.open("a", encoding="utf-8") as handle:
                handle.write(event.model_dump_json() + "\n")
        return event

    def write_decision(self, trace: DecisionTrace) -> DecisionTrace:
        self.decisions.append(trace)
        with self.decisions_path.open("a", encoding="utf-8") as handle:
            handle.write(trace.model_dump_json() + "\n")
        return trace

    def for_day(self, day: int) -> list[LogEvent]:
        return [e for e in self.events if e.day == day]


def save_checkpoint(state: VillaState, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(state.model_dump_json(indent=2), encoding="utf-8")


def write_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


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


def utc_now() -> str:
    return datetime.now(UTC).isoformat()
