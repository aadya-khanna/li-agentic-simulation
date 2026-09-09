#!/usr/bin/env python3
"""Agent-triggered events: islanders can call a gathering themselves (type=gather)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.agent import WORLD_ACTIONS, system_prompt  # noqa: E402
from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation, load_profiles  # noqa: E402
from li_sim.models import ActionType  # noqa: E402


def run() -> None:
    assert ActionType.GATHER in WORLD_ACTIONS, "gather not offered during grafting ticks"

    profile = load_profiles(settings=Settings())["gemini-agent1"]
    rules = system_prompt(profile, Settings())
    assert "gather" in rules, "gather mechanic not documented in world_rules"

    settings = Settings(stub=True, season_days=3, experiment_id="harness-gather", run_id="test")
    sim = Simulation(settings)
    state = sim.run()

    gather_events = [e for e in sim.log.events if e.kind == "gather"]
    assert gather_events, "expected at least one gather event over a 3-day stub run"

    convened = [e for e in gather_events if len(e.participants) >= 2]
    assert convened, "gather events should carry 2+ participants"
    for event in convened:
        assert len(event.participants) <= 3, f"gather group exceeded cap: {event.participants}"

    caller_names = {e.actor for e in gather_events}
    for name in caller_names:
        assert name in state.islanders, f"gather caller {name} not a real islander"

    gather_moments = [m for m in state.major_moments if "gathering" in m.text.lower()]
    assert gather_moments, "gathering should register as a major moment"


if __name__ == "__main__":
    run()
    print("agent_triggered_events ok")
