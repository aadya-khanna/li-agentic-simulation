#!/usr/bin/env python3
"""Earned events: rewards fire from state triggers, not fixed calendar dates."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

import yaml  # noqa: E402

from li_sim.agent import decision_user_prompt, system_prompt  # noqa: E402
from li_sim.config import DATA_DIR, Settings  # noqa: E402
from li_sim.engine import Simulation, load_profiles, new_villa  # noqa: E402
from li_sim.models import ActionType  # noqa: E402

REWARD_KINDS = frozenset({"date", "pull_aside", "singles_chat", "challenge"})


def run() -> None:
    raw = yaml.safe_load((DATA_DIR / "schedule.yaml").read_text(encoding="utf-8"))
    assert raw.get("reward_triggers"), "schedule missing reward_triggers catalog"
    for day in raw["days"]:
        assert "dates" not in day and "challenge" not in day, "fixed calendar rewards still present"
        assert not day.get("dates") and not day.get("challenge")

    settings = Settings(stub=True, season_days=7, experiment_id="harness-earned", run_id="test")
    sim = Simulation(settings)
    state = sim.run()

    kinds = {e.kind for e in sim.log.events}
    assert kinds & REWARD_KINDS, f"expected earned reward events, got kinds={sorted(kinds)}"

    trigger_hosts = [
        e for e in sim.log.events
        if e.kind == "host" and e.extra.get("trigger_id")
    ]
    assert trigger_hosts, "expected host announcements with trigger_id"

    profile = load_profiles(settings=settings)["gemini-agent1"]
    prompt = decision_user_prompt(profile, state, [ActionType.SPEAK], settings=settings)
    assert "Public reputation:" not in prompt
    rules = system_prompt(profile, settings)
    assert "villa activity" in rules

    assert state.last_reward_id, "expected at least one earned reward recorded on state"


if __name__ == "__main__":
    run()
    print("earned_events ok")
