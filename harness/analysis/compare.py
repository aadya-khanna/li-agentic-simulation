#!/usr/bin/env python3
"""Aggregate experiment metrics across conditions and seeds."""
from __future__ import annotations

import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_HARNESS = ROOT / "harness"
if str(_HARNESS) not in sys.path:
    sys.path.insert(0, str(_HARNESS))

from analysis.replication_battery import (
    MIN_SEEDS_PER_CONDITION,
    REPLICATION_BATTERY,
    aggregate_values,
    condition_ready,
    contrast_conditions,
    replication_values,
)


def _load_metrics(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def compare_experiment(experiment_dir: Path) -> dict:
    summary: dict[str, dict[str, dict[str, float]]] = {}
    for condition_dir in sorted(experiment_dir.iterdir()):
        if not condition_dir.is_dir():
            continue
        condition = condition_dir.name
        runs: dict[str, list[float]] = defaultdict(list)
        for run_dir in sorted(condition_dir.iterdir()):
            metrics_path = run_dir / "metrics.json"
            if not metrics_path.exists():
                continue
            metrics = _load_metrics(metrics_path)
            for key, value in metrics.items():
                if isinstance(value, (int, float)):
                    runs[key].append(float(value))
        if not runs:
            continue
        summary[condition] = {
            key: {
                "mean": statistics.mean(values),
                "stdev": statistics.pstdev(values) if len(values) > 1 else 0.0,
                "n": len(values),
            }
            for key, values in runs.items()
        }
    return summary


def replication_summary(experiment_dir: Path, *, min_n: int = MIN_SEEDS_PER_CONDITION) -> dict:
    per_condition: dict[str, dict[str, dict]] = {}
    run_counts: dict[str, int] = {}

    for condition_dir in sorted(experiment_dir.iterdir()):
        if not condition_dir.is_dir():
            continue
        condition = condition_dir.name
        collected: dict[str, list[float]] = defaultdict(list)
        n_runs = 0
        for run_dir in sorted(condition_dir.iterdir()):
            metrics_path = run_dir / "metrics.json"
            if not metrics_path.exists():
                continue
            n_runs += 1
            for key, value in replication_values(_load_metrics(metrics_path)).items():
                collected[key].append(value)
        run_counts[condition] = n_runs
        if not collected:
            continue
        per_condition[condition] = {
            key: aggregate_values(values)
            for key, values in collected.items()
            if key in REPLICATION_BATTERY
        }

    readiness = {
        condition: {
            "ready": condition_ready(
                runs_with_metrics=run_counts.get(condition, 0),
                min_n=min_n,
            ),
            "runs_with_metrics": run_counts.get(condition, 0),
            "min_seeds": min_n,
        }
        for condition, stats in per_condition.items()
    }

    contrasts: dict[str, dict] = {}
    if "minimal" in per_condition and "incentive" in per_condition:
        if readiness["minimal"]["ready"] and readiness["incentive"]["ready"]:
            contrasts["incentive_vs_minimal"] = contrast_conditions(
                per_condition["minimal"],
                per_condition["incentive"],
                label="incentive minus minimal",
            )

    invariants: dict[str, list[str]] = {}
    for condition, stats in per_condition.items():
        inv = [key for key, entry in stats.items() if entry.get("invariant")]
        if inv:
            invariants[condition] = inv

    return {
        "experiment_id": experiment_dir.name,
        "min_seeds_per_condition": min_n,
        "conditions": per_condition,
        "readiness": readiness,
        "invariants": invariants,
        "contrasts": contrasts,
    }


def write_summaries(experiment_dir: Path) -> tuple[dict, dict]:
    summary = compare_experiment(experiment_dir)
    replication = replication_summary(experiment_dir)
    (experiment_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (experiment_dir / "replication_summary.json").write_text(
        json.dumps(replication, indent=2), encoding="utf-8"
    )
    return summary, replication


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: compare.py logs/experiments/<experiment_id>")
    experiment_dir = Path(sys.argv[1])
    if not experiment_dir.is_absolute():
        experiment_dir = ROOT / experiment_dir
    summary, replication = write_summaries(experiment_dir)
    print(json.dumps(summary, indent=2))
    print(f"\nWrote {experiment_dir / 'summary.json'}")
    print(json.dumps(replication, indent=2))
    print(f"\nWrote {experiment_dir / 'replication_summary.json'}")


if __name__ == "__main__":
    main()
