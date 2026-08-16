#!/usr/bin/env python3
"""Same seed + config should produce identical event tapes in stub mode."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation  # noqa: E402


def _run(seed: int, run_id: str) -> list[dict]:
    settings = Settings(
        stub=True,
        season_days=1,
        seed=seed,
        prompt_condition="minimal",
        experiment_id="repro-test",
        run_id=run_id,
    )
    sim = Simulation(settings)
    sim.run()
    return [json.loads(line) for line in settings.events_path.read_text(encoding="utf-8").splitlines() if line.strip()]


def run() -> None:
    a = _run(42, "a")
    b = _run(42, "b")
    assert len(a) == len(b), "event count differs for same seed"
    for idx, (left, right) in enumerate(zip(a, b, strict=True)):
        assert left["kind"] == right["kind"], f"kind mismatch at {idx}"
        assert left.get("actor") == right.get("actor"), f"actor mismatch at {idx}"
        assert left.get("target") == right.get("target"), f"target mismatch at {idx}"


if __name__ == "__main__":
    run()
    print("reproducibility ok")
