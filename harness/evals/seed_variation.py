#!/usr/bin/env python3
"""Different seeds should produce different stub trajectories."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation  # noqa: E402


def _signature(settings: Settings) -> tuple:
    sim = Simulation(settings)
    sim.run()
    kinds = tuple(e.kind for e in sim.log.events)
    couples = tuple(sim.state.couples())
    return kinds, couples


def run() -> None:
    base = dict(stub=True, season_days=1, prompt_condition="minimal", experiment_id="seed-var")
    a = _signature(Settings(**base, seed=1, run_id="s1"))
    b = _signature(Settings(**base, seed=99, run_id="s99"))
    assert a != b, "different seeds produced identical trajectories"


if __name__ == "__main__":
    run()
    print("seed_variation ok")
