#!/usr/bin/env python3
"""One-day stub season smoke test — proves engine + logging loop works."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation  # noqa: E402


def run() -> None:
    settings = Settings(stub=True, season_days=1, experiment_id="harness-smoke", run_id="smoke")
    sim = Simulation(settings)
    state = sim.run()

    events = sim.log.events
    assert len(events) >= 10, f"expected substantive season, got {len(events)} events"
    kinds = {e.kind for e in events}
    assert "host" in kinds, "missing host announcements"
    assert any(k in kinds for k in ("speak", "couple_choice")), "missing social beats"
    assert "huddle" not in kinds, "gender huddles should be removed"

    thought_events = [e for e in events if e.thought]
    assert thought_events, "expected private thought on at least one event"

    checkpoint = settings.run_dir() / "state.json"
    assert checkpoint.exists(), "state.json not written"
    data = json.loads(checkpoint.read_text(encoding="utf-8"))
    assert "islanders" in data
    sample = next(iter(data["islanders"].values()))
    assert "contacts" in sample, "checkpoint missing contacts (talk history)"
    assert "relationships" not in sample, "checkpoint still has relationship scores"
    assert (settings.run_dir() / "events.jsonl").exists()
    assert (settings.run_dir() / "manifest.json").exists()
    assert (settings.run_dir() / "decisions.jsonl").exists()

    assert state.day == 1
    assert len(state.active_names()) >= 2, "villa emptied unexpectedly on day 1"


if __name__ == "__main__":
    run()
    print("smoke_season ok")
