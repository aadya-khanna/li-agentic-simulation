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


def run_matrix(
    spec_path: Path,
    *,
    force: bool = False,
    live: bool | None = None,
    stub_on_error: bool | None = None,
) -> None:
    spec = load_spec(spec_path)
    experiment_id = spec["experiment_id"]
    conditions = spec["conditions"]
    seeds = spec["seeds"]
    days = spec.get("days", 1)
    stub = spec.get("stub", True) if live is None else not live
    prize = spec.get("prize_emphasis", "high")
    resume = spec.get("resume", True)
    use_stub_on_error = spec.get("stub_on_error", False) if stub_on_error is None else stub_on_error

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
                stub_on_error=use_stub_on_error,
            )
            mode = "stub" if stub else "live"
            print(f"run: {experiment_id}/{condition}/{run_id} ({mode})")
            sim = Simulation(settings)
            sim.run()
            write_metrics(settings.events_path)
            brief = summarize_events(sim.log.events)
            write_brief_log(brief, run_dir / "brief.log")

    from analysis.compare import write_summaries  # noqa: E402

    exp_dir = LOG_DIR / "experiments" / experiment_id
    write_summaries(exp_dir)
    print(f"summary -> {exp_dir / 'summary.json'}")
    print(f"replication_summary -> {exp_dir / 'replication_summary.json'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run prompt-condition experiment matrix")
    parser.add_argument(
        "spec",
        nargs="?",
        type=Path,
        default=ROOT / "harness" / "experiments" / "baseline.yaml",
    )
    parser.add_argument("--force", action="store_true", help="Re-run even if manifest exists")
    parser.add_argument("--live", action="store_true", help="Live LLM (overrides spec stub: false)")
    parser.add_argument(
        "--stub-on-error",
        action="store_true",
        help="Fall back to stub decisions on API errors (cron parity)",
    )
    args = parser.parse_args()
    run_matrix(
        args.spec,
        force=args.force,
        live=True if args.live else None,
        stub_on_error=True if args.stub_on_error else None,
    )


if __name__ == "__main__":
    main()
