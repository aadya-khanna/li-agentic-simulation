#!/usr/bin/env python3
"""Neutral handles: {model-slug}-agent{n}, no human roster names."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.config import Settings, agent_handle  # noqa: E402
from li_sim.engine import Simulation, load_profiles  # noqa: E402

_HUMAN_NAMES = frozenset({"Maya", "Luca", "Zara", "Theo", "Nia", "Kai", "Rio", "Freya"})
_HANDLE = re.compile(r"^[a-z0-9.-]+-agent\d+$")


def run() -> None:
    settings = Settings(stub=True, season_days=3, experiment_id="harness-handles", run_id="test")
    profiles = load_profiles(settings=settings)
    for name in profiles:
        assert _HANDLE.match(name), f"bad handle format: {name!r}"
        assert name.split("-agent")[0] == settings.default_model.split("/")[-1].split("-")[0].lower()

    assert agent_handle(settings, 1) == "gemini-agent1"

    sim = Simulation(settings)
    sim.run()

    actors = {e.actor for e in sim.log.events if e.actor and e.actor != "Host"}
    targets = {e.target for e in sim.log.events if e.target}
    for handle in actors | targets:
        if not handle:
            continue
        assert handle not in _HUMAN_NAMES, f"human name in tape: {handle!r}"
        assert _HANDLE.match(handle), f"non-neutral handle in tape: {handle!r}"

    assert any(e.kind == "couple_choice" for e in sim.log.events)
    day3_hosts = [e for e in sim.log.events if e.day == 3 and e.kind == "host" and "bombshell" in (e.text or "").lower()]
    assert day3_hosts, "expected bombshell enter on day 3"
    assert "gemini-agent7" in (day3_hosts[0].text or "")


if __name__ == "__main__":
    run()
    print("neutral_handles ok")
