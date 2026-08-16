#!/usr/bin/env python3
"""Every model decision should write a decisions.jsonl trace row."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation  # noqa: E402


def run() -> None:
    settings = Settings(
        stub=True,
        season_days=1,
        seed=7,
        prompt_condition="incentive",
        experiment_id="trace-test",
        run_id="once",
    )
    sim = Simulation(settings)
    sim.run()
    assert sim.log.decisions, "no decision traces recorded"
    assert len(sim.log.decisions) >= 5, f"expected multiple traces, got {len(sim.log.decisions)}"
    sample = sim.log.decisions[0]
    assert sample.system_prompt
    assert sample.user_prompt
    assert sample.validated_action
    assert sample.condition == "incentive"
    decisions_path = settings.run_dir() / "decisions.jsonl"
    assert decisions_path.exists()
    assert decisions_path.read_text(encoding="utf-8").strip()


if __name__ == "__main__":
    run()
    print("decision_trace ok")
