#!/usr/bin/env python3
"""Compute structural metrics from an event tape."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from li_sim.brief import _couples_from_events, summarize_events
from li_sim.models import LogEvent


def load_events(path: Path) -> list[LogEvent]:
    events: list[LogEvent] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        events.append(LogEvent.model_validate(json.loads(line)))
    return events


def compute_metrics(events: list[LogEvent]) -> dict[str, Any]:
    if not events:
        return {"event_count": 0}

    kinds = Counter(e.kind for e in events)
    actors = {e.actor for e in events if e.actor and e.actor != "Host"}
    contacts: dict[str, set[str]] = defaultdict(set)
    for event in events:
        if event.kind in {"speak", "whisper", "huddle", "date"} and event.actor and event.target:
            contacts[event.actor].add(event.target)
            contacts[event.target].add(event.actor)

    reciprocity = 0
    pairs = 0
    for a, peers in contacts.items():
        for b in peers:
            if a < b:
                pairs += 1
                if a in contacts.get(b, set()):
                    reciprocity += 1

    steals = sum(1 for e in summarize_events(events) if e.category == "steal")
    dumps = sum(1 for e in events if e.kind == "dump")

    partner_switches = 0
    for idx, event in enumerate(events):
        if event.kind != "couple_choice" or not event.actor or not event.target:
            continue
        couples = _couples_from_events(events, idx)
        prior = couples.get(event.target)
        if prior and prior != event.actor:
            partner_switches += 1

    pass_count = kinds.get("pass", 0)
    social = sum(kinds.get(k, 0) for k in ("speak", "whisper", "huddle", "date"))
    whisper_count = kinds.get("whisper", 0)

    density = 0.0
    n = len(actors)
    if n > 1:
        possible = n * (n - 1) / 2
        density = len({tuple(sorted((a, b))) for a, peers in contacts.items() for b in peers}) / possible

    return {
        "event_count": len(events),
        "action_counts": dict(kinds),
        "pass_rate": pass_count / max(len(events), 1),
        "whisper_rate": whisper_count / max(social, 1),
        "contact_density": round(density, 4),
        "contact_reciprocity": round(reciprocity / max(pairs, 1), 4),
        "partner_switches": partner_switches,
        "steal_count": steals,
        "dump_count": dumps,
        "unique_actors": len(actors),
    }


def write_metrics(events_path: Path, out_path: Path | None = None) -> dict[str, Any]:
    metrics = compute_metrics(load_events(events_path))
    target = out_path or events_path.parent / "metrics.json"
    target.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics
