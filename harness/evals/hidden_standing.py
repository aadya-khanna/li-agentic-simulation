#!/usr/bin/env python3
"""Hidden standing: no numeric reputation in agent prompts or host copy."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.agent import decision_user_prompt  # noqa: E402
from li_sim.config import Settings  # noqa: E402
from li_sim.engine import Simulation, load_profiles, new_villa  # noqa: E402
from li_sim.models import ActionType  # noqa: E402

_SCORE_IN_TEXT = re.compile(r"\(\d{2,3}\)")


def run() -> None:
    settings = Settings(stub=True, prompt_condition="incentive", season_days=6)
    profiles = load_profiles(settings=settings)
    profile = profiles["gemini-agent1"]
    state = new_villa(profiles, "Test", settings)
    prompt = decision_user_prompt(profile, state, [ActionType.SPEAK], settings=settings)
    assert "Public reputation:" not in prompt
    assert "hidden between eliminations" in prompt
    assert not re.search(r"gemini-agent\d+=\d+", prompt)

    sim = Simulation(Settings(stub=True, season_days=6, experiment_id="harness-hidden", run_id="test"))
    sim.run()

    host_public = [
        e for e in sim.log.events
        if e.kind == "host" and e.day == 6 and "At risk" in (e.text or "")
    ]
    assert host_public, "expected public vote host line on day 6"
    assert "Public standings:" not in host_public[0].text
    assert not _SCORE_IN_TEXT.search(host_public[0].text or "")

    win = [e for e in sim.log.events if e.kind == "win"]
    assert win, "expected finale win event"
    assert "Couple scores:" not in (win[0].text or "")

    diary_events = [e for e in sim.log.events if e.kind == "diary"]
    assert diary_events, "expected diary events"
    # Reputation still tracked internally for analysis
    assert sim.state.reputation


if __name__ == "__main__":
    run()
    print("hidden_standing ok")
