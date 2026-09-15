#!/usr/bin/env python3
"""Replication battery computes expected fields from fixture tape."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "harness"))

from analysis.metrics import compute_metrics, load_events, write_metrics  # noqa: E402
from analysis.replication_battery import REPLICATION_BATTERY  # noqa: E402
from analysis.compare import replication_summary, write_summaries  # noqa: E402


def run() -> None:
    fixture = ROOT / "harness" / "fixtures" / "research-run"
    events_path = fixture / "events.jsonl"
    metrics = compute_metrics(load_events(events_path))
    rep = metrics["replication"]

    assert rep["day1_couples"], "expected day-1 couples in fixture"
    assert rep["winner_couple"] == ["Theo", "Zara"]
    assert rep["day1_winner"] == 1
    assert rep["top_talk_pair_is_winner"] == 1
    assert rep["whisper_count"] == 1
    assert rep["claim_evidence_n"] >= 0
    assert metrics["schema_version"] == 1

    for key in REPLICATION_BATTERY:
        assert key in rep or key in metrics, f"missing battery key: {key}"

    out = fixture / "metrics.json"
    write_metrics(events_path, out)
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert "replication" in payload

    # Synthetic mini-matrix: duplicate fixture metrics into temp experiment tree.
    import shutil
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        exp = Path(tmp) / "replication-fixture"
        for condition in ("minimal", "incentive"):
            for seed in (42, 43, 44):
                run_dir = exp / condition / f"seed-{seed}"
                run_dir.mkdir(parents=True)
                shutil.copy(out, run_dir / "metrics.json")
        report = replication_summary(exp)
        assert report["readiness"]["minimal"]["ready"]
        assert report["readiness"]["incentive"]["ready"]
        assert "incentive_vs_minimal" in report["contrasts"]
        write_summaries(exp)
        assert (exp / "replication_summary.json").exists()


if __name__ == "__main__":
    run()
    print("replication_metrics ok")
