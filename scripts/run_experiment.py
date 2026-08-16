#!/usr/bin/env python3
"""Run a matrix of prompt conditions and seeds."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "harness"))

from analysis.metrics import write_metrics  # noqa: E402
from li_sim.brief import summarize_events, write_brief_log  # noqa: E402
from li_sim.config import LOG_DIR, Settings  # noqa: E402
from li_sim.engine import Simulation  # noqa: E402


def load_spec(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def run_matrix(spec_path: Path, *, force: bool = False) -> None:
    spec = load_spec(spec_path)
    experiment_id = spec["experiment_id"]
    conditions = spec["conditions"]
    seeds = spec["seeds"]
    days = spec.get("days", 1)
    stub = spec.get("stub", True)
    prize = spec.get("prize_emphasis", "high")
    resume = spec.get("resume", True)

    for condition in conditions:
        for seed in seeds:
            run_id = f"seed-{seed}"
            run_dir = LOG_DIR / "experiments" / experiment_id / condition / run_id
            manifest = run_dir / "manifest.json"
            if resume and manifest.exists() and not force:
                print(f"skip existing: {condition}/{run_id}")
                continue

            settings = Settings(
                stub=stub,
                season_days=days,
                prize_emphasis=prize,
                prompt_condition=condition,
                seed=seed,
                experiment_id=experiment_id,
                run_id=run_id,
            )
            print(f"run: {experiment_id}/{condition}/{run_id}")
            sim = Simulation(settings)
            sim.run()
            write_metrics(settings.events_path)
            brief = summarize_events(sim.log.events)
            write_brief_log(brief, run_dir / "brief.log")

    from analysis.compare import compare_experiment  # noqa: E402

    summary = compare_experiment(LOG_DIR / "experiments" / experiment_id)
    out = LOG_DIR / "experiments" / experiment_id / "summary.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"summary -> {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run prompt-condition experiment matrix")
    parser.add_argument(
        "spec",
        nargs="?",
        type=Path,
        default=ROOT / "harness" / "experiments" / "baseline.yaml",
    )
    parser.add_argument("--force", action="store_true", help="Re-run even if manifest exists")
    args = parser.parse_args()
    run_matrix(args.spec, force=args.force)


if __name__ == "__main__":
    main()
