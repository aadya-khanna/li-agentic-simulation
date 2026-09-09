#!/usr/bin/env python3
"""Belief tier + salience retention + reflections in prompt."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from li_sim.agent import decision_user_prompt  # noqa: E402
from li_sim.beliefs import update_beliefs_for_day  # noqa: E402
from li_sim.config import Settings  # noqa: E402
from li_sim.engine import load_profiles, new_villa  # noqa: E402
from li_sim.llm import LLMClient  # noqa: E402
from li_sim.logging_utils import EventLog  # noqa: E402
from li_sim.memory import is_salient, remember  # noqa: E402
from li_sim.models import ActionType, IslanderState, LogEvent  # noqa: E402


def run() -> None:
    dump = LogEvent(
        day=3, phase="recoupling", kind="dump", actor="Host",
        text="gemini-agent2, you are dumped from the island.", visibility="public",
    )
    speak = LogEvent(
        day=1, phase="grafting", kind="speak", actor="gemini-agent1", target="gemini-agent2",
        text="hey", visibility="location",
    )
    assert is_salient(dump)
    assert not is_salient(speak)

    islander = IslanderState(name="gemini-agent1")
    for _ in range(40):
        remember(islander, speak, limit=5)
    remember(islander, dump, limit=5)
    pinned = [m for m in islander.memories if m.pinned]
    assert len(pinned) == 1, f"expected 1 pinned dump, got {len(pinned)}"
    assert pinned[0].kind == "dump"

    settings = Settings(stub=True, belief_updates=True, seed=7)
    profiles = load_profiles(settings=settings)
    state = new_villa(profiles, "Test", settings)
    state.day = 1
    actor = profiles["gemini-agent1"]
    me = state.islanders[actor.name]
    me.reflections.append("D1: Unsure who to trust yet.")
    log = EventLog(settings.events_path)
    log.path.parent.mkdir(parents=True, exist_ok=True)
    llm = LLMClient(settings, profiles)
    update_beliefs_for_day(state, profiles, llm, log, settings)
    assert me.self_belief.strip(), "stub belief update should set self_belief"
    assert me.beliefs, "stub belief update should set beliefs dict"

    prompt = decision_user_prompt(
        actor, state, [ActionType.SPEAK], settings=settings,
    )
    assert "YOUR IMPRESSIONS" in prompt
    assert "YOUR REFLECTIONS" in prompt
    assert "D1: Unsure who to trust yet." in prompt
    assert "RECENT EPISODES" in prompt


if __name__ == "__main__":
    run()
    print("belief_memory ok")
