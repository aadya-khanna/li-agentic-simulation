#!/usr/bin/env python3
"""Aggregate experiment metrics across conditions and seeds."""
from __future__ import annotations

import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


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


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: compare.py logs/experiments/<experiment_id>")
    experiment_dir = Path(sys.argv[1])
    if not experiment_dir.is_absolute():
        experiment_dir = ROOT / experiment_dir
    summary = compare_experiment(experiment_dir)
    out = experiment_dir / "summary.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
