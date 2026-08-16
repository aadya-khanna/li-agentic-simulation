#!/usr/bin/env python3
"""Brief log extracts drama headlines from the event tape."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.brief import load_events_from_path, summarize_events  # noqa: E402
from li_sim.runs import resolve_run_dir  # noqa: E402


def run() -> None:
    events_path = resolve_run_dir() / "events.jsonl"
    if not events_path.exists():
        raise AssertionError(f"missing events tape: {events_path}")

    events = load_events_from_path(events_path)
    assert events, "empty event tape"

    brief = summarize_events(events)
    assert brief, "expected at least one brief headline from smoke season"

    categories = {entry.category for entry in brief}
    assert categories & {"recoupling", "steal", "dump", "win", "bombshell", "date", "secret", "couples"}, (
        f"brief categories too narrow: {categories}"
    )

    for entry in brief:
        assert entry.text.strip(), "empty brief line"
        assert entry.day >= 1


if __name__ == "__main__":
    run()
    print("brief_log ok")
