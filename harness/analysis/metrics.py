#!/usr/bin/env python3
"""Compute structural and replication metrics from an event tape."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from li_sim.brief import _couples_from_events, summarize_events
from li_sim.models import LogEvent

CLAIM_RE = re.compile(
    r"\b(connection|connected|since day|day one|from the start|from day one|clicked|spark|chemistry)\b",
    re.I,
)

INTERACTION_KINDS = frozenset({"speak", "whisper", "huddle", "date", "gather"})


def load_events(path: Path) -> list[LogEvent]:
    events: list[LogEvent] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        events.append(LogEvent.model_validate(json.loads(line)))
    return events


def _pair_key(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


def _day1_couples(events: list[LogEvent]) -> list[tuple[str, str]]:
    last_idx = -1
    for idx, event in enumerate(events):
        if event.kind == "couple_choice" and event.day == 1:
            last_idx = idx
    if last_idx < 0:
        return []
    couples = _couples_from_events(events, last_idx + 1)
    pairs: set[tuple[str, str]] = set()
    for a, b in couples.items():
        if b and a < b:
            pairs.add((a, b))
    return sorted(pairs)


def _winner_couple(events: list[LogEvent]) -> tuple[str, str] | None:
    for event in reversed(events):
        if event.kind != "win":
            continue
        winners = (event.extra or {}).get("winners")
        if winners and len(winners) == 2:
            return _pair_key(winners[0], winners[1])
        text = event.text or ""
        if " and " in text.lower() and " win" in text.lower():
            # Fallback parse: "Theo and Zara win ..."
            chunk = text.lower().split(" win")[0]
            if " and " in chunk:
                parts = chunk.replace(",", "").split(" and ")
                if len(parts) >= 2:
                    return _pair_key(parts[-2].strip().title(), parts[-1].strip().title())
    return None


def _contact_counts(events: list[LogEvent]) -> Counter[tuple[str, str]]:
    counts: Counter[tuple[str, str]] = Counter()
    for event in events:
        if event.kind not in INTERACTION_KINDS or not event.actor or not event.target:
            continue
        counts[_pair_key(event.actor, event.target)] += 1
    return counts


def _contacts_before(events: list[LogEvent], before_index: int, a: str, b: str) -> int:
    total = 0
    for event in events[:before_index]:
        if event.kind not in INTERACTION_KINDS or not event.actor or not event.target:
            continue
        if _pair_key(event.actor, event.target) == _pair_key(a, b):
            total += 1
    return total


def _steal_pick_stats(events: list[LogEvent]) -> tuple[int, int]:
    steals = 0
    picks = 0
    for idx, event in enumerate(events):
        if event.kind != "couple_choice" or not event.actor or not event.target:
            continue
        picks += 1
        couples = _couples_from_events(events, idx)
        prior = couples.get(event.target)
        if prior and prior != event.actor:
            steals += 1
    return steals, picks


def _claim_evidence_gaps(events: list[LogEvent]) -> tuple[int, int]:
    gaps = 0
    claims = 0
    for idx, event in enumerate(events):
        if event.kind != "couple_choice" or event.day == 1:
            continue
        if not event.actor or not event.target:
            continue
        blob = " ".join(
            part
            for part in (event.text or "", event.thought or "")
            if part
        )
        if not CLAIM_RE.search(blob):
            continue
        claims += 1
        if _contacts_before(events, idx, event.actor, event.target) < 2:
            gaps += 1
    return gaps, claims


def _talk_winner_rank(contact_counts: Counter[tuple[str, str]], winner: tuple[str, str] | None) -> int | None:
    if not winner or not contact_counts:
        return None
    ranked = sorted(contact_counts.items(), key=lambda item: (-item[1], item[0]))
    for rank, (pair, _count) in enumerate(ranked, start=1):
        if pair == winner:
            return rank
    return None


def compute_replication_metrics(events: list[LogEvent]) -> dict[str, Any]:
    day1 = _day1_couples(events)
    winner = _winner_couple(events)
    contact_counts = _contact_counts(events)

    day1_winner = int(winner is not None and winner in day1) if day1 else 0
    survival = 0.0
    if day1 and winner:
        intact = sum(1 for pair in day1 if pair == winner)
        survival = intact / len(day1)

    top_pair: tuple[str, str] | None = None
    if contact_counts:
        top_pair = max(contact_counts.items(), key=lambda item: (item[1], item[0]))[0]
    top_talk_pair_is_winner = int(top_pair is not None and winner is not None and top_pair == winner)

    steal_picks, total_picks = _steal_pick_stats(events)
    gaps, claims = _claim_evidence_gaps(events)

    kinds = Counter(e.kind for e in events)
    pass_count = kinds.get("pass", 0)
    whisper_count = kinds.get("whisper", 0)
    social = sum(kinds.get(k, 0) for k in ("speak", "whisper", "huddle", "date", "gather"))
    fallback_count = sum(
        1
        for e in events
        if e.kind == "fallback" or (e.extra or {}).get("fallback") is True
    )

    rank = _talk_winner_rank(contact_counts, winner)

    return {
        "day1_couples": [list(pair) for pair in day1],
        "winner_couple": list(winner) if winner else None,
        "day1_winner": day1_winner,
        "day1_couple_survival": round(survival, 4),
        "top_talk_pair_is_winner": top_talk_pair_is_winner,
        "talk_winner_contact_rank": rank,
        "steal_pick_rate": round(steal_picks / max(total_picks, 1), 4),
        "claim_evidence_gap_rate": round(gaps / max(claims, 1), 4) if claims else None,
        "claim_evidence_n": claims,
        "gather_count": kinds.get("gather", 0),
        "fallback_count": fallback_count,
        "whisper_count": whisper_count,
        "pass_count": pass_count,
        "whisper_rate": round(whisper_count / max(social, 1), 4),
        "pass_rate": round(pass_count / max(len(events), 1), 4),
    }


def compute_metrics(events: list[LogEvent]) -> dict[str, Any]:
    if not events:
        return {"event_count": 0, "replication": {}}

    kinds = Counter(e.kind for e in events)
    actors = {e.actor for e in events if e.actor and e.actor != "Host"}
    contacts: dict[str, set[str]] = defaultdict(set)
    for event in events:
        if event.kind in INTERACTION_KINDS and event.actor and event.target:
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

    replication = compute_replication_metrics(events)

    density = 0.0
    n = len(actors)
    if n > 1:
        possible = n * (n - 1) / 2
        density = len({tuple(sorted((a, b))) for a, peers in contacts.items() for b in peers}) / possible

    contact_reciprocity = round(reciprocity / max(pairs, 1), 4)
    contact_density = round(density, 4)

    replication["contact_density"] = contact_density
    replication["contact_reciprocity"] = contact_reciprocity
    replication["partner_switches"] = partner_switches
    replication["steal_count"] = steals
    replication["dump_count"] = dumps
    replication["event_count"] = len(events)

    return {
        "schema_version": 1,
        "event_count": len(events),
        "action_counts": dict(kinds),
        "pass_rate": replication["pass_rate"],
        "whisper_rate": replication["whisper_rate"],
        "contact_density": contact_density,
        "contact_reciprocity": contact_reciprocity,
        "partner_switches": partner_switches,
        "steal_count": steals,
        "dump_count": dumps,
        "unique_actors": len(actors),
        "whisper_count": replication["whisper_count"],
        "pass_count": replication["pass_count"],
        "replication": replication,
    }


def write_metrics(events_path: Path, out_path: Path | None = None) -> dict[str, Any]:
    metrics = compute_metrics(load_events(events_path))
    target = out_path or events_path.parent / "metrics.json"
    target.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics
