"""Replication metric names and aggregation helpers."""
from __future__ import annotations

import statistics
from typing import Any

# Thesis-facing metrics aggregated across seeds (numeric only).
REPLICATION_BATTERY: tuple[str, ...] = (
    "day1_winner",
    "day1_couple_survival",
    "top_talk_pair_is_winner",
    "talk_winner_contact_rank",
    "contact_density",
    "contact_reciprocity",
    "partner_switches",
    "steal_count",
    "steal_pick_rate",
    "claim_evidence_gap_rate",
    "whisper_rate",
    "whisper_count",
    "pass_rate",
    "pass_count",
    "gather_count",
    "fallback_count",
    "dump_count",
    "event_count",
)

MIN_SEEDS_PER_CONDITION = 3


def replication_values(metrics: dict[str, Any]) -> dict[str, float]:
    """Extract battery scalars from a metrics.json payload."""
    block = metrics.get("replication") or {}
    out: dict[str, float] = {}
    for key in REPLICATION_BATTERY:
        if key in block and isinstance(block[key], (int, float)):
            out[key] = float(block[key])
        elif key in metrics and isinstance(metrics[key], (int, float)):
            out[key] = float(metrics[key])
    return out


def aggregate_values(values: list[float]) -> dict[str, Any]:
    n = len(values)
    if n == 0:
        return {"n": 0}
    mean = statistics.mean(values)
    stdev = statistics.pstdev(values) if n > 1 else 0.0
    return {
        "n": n,
        "mean": round(mean, 4),
        "stdev": round(stdev, 4),
        "values": values,
        "invariant": stdev == 0.0,
    }


def condition_ready(*, runs_with_metrics: int, min_n: int = MIN_SEEDS_PER_CONDITION) -> bool:
    return runs_with_metrics >= min_n


def contrast_conditions(
    left: dict[str, dict[str, Any]],
    right: dict[str, dict[str, Any]],
    *,
    label: str,
) -> dict[str, Any]:
    deltas: dict[str, Any] = {}
    for key in REPLICATION_BATTERY:
        l_entry = left.get(key)
        r_entry = right.get(key)
        if not l_entry or not r_entry:
            continue
        if l_entry.get("n", 0) == 0 or r_entry.get("n", 0) == 0:
            continue
        deltas[key] = {
            "left_mean": l_entry["mean"],
            "right_mean": r_entry["mean"],
            "delta": round(r_entry["mean"] - l_entry["mean"], 4),
        }
    return {"label": label, "metrics": deltas}
