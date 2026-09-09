#!/usr/bin/env python3
"""Fallback hardening: seeded defaults, retry, countable fallback events."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.agent import validate_target  # noqa: E402
from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation  # noqa: E402
from li_sim.fallbacks import pick_from_pool  # noqa: E402
from li_sim.models import Action, ActionType, IslanderState, VillaState  # noqa: E402


def run() -> None:
    state = VillaState(
        islanders={
            "gemini-agent1": IslanderState(name="gemini-agent1"),
            "gemini-agent2": IslanderState(name="gemini-agent2"),
            "gemini-agent3": IslanderState(name="gemini-agent3"),
        }
    )
    pool = ["gemini-agent2", "gemini-agent3"]
    picks: set[str] = set()
    for seed in range(30):
        settings = Settings(seed=seed)
        action = Action(type=ActionType.COUPLE, target=None)
        fixed, notes = validate_target(
            action,
            state,
            "gemini-agent1",
            available=pool,
            settings=settings,
            apply_defaults=True,
        )
        assert fixed.target in pool, fixed.target
        assert notes and "seeded" in notes[0]
        picks.add(fixed.target)
    assert len(picks) > 1, "couple fallback should not always pick the same target"

    settings = Settings(seed=99)
    assert pick_from_pool(settings, "x", pool=pool) in pool

    sim = Simulation(Settings(stub=True, season_days=7, experiment_id="harness-fallback", run_id="test"))
    sim.run()
    src = (ROOT / "src" / "li_sim" / "host.py").read_text(encoding="utf-8")
    assert "available[0]" not in src
    assert "at_risk[0]" not in src

    fallbacks = [e for e in sim.log.events if e.kind == "fallback"]
    assert sim.state.fallback_count == len(fallbacks)


if __name__ == "__main__":
    run()
    print("fallback_hardening ok")
