#!/usr/bin/env python3
"""Assert research invariants in prompts, models, roster, and host copy."""
from __future__ import annotations

import inspect
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src" / "li_sim"


def run() -> None:
    _roster_is_handles_only()
    _profile_model_fields()
    _agent_prompt_invariants()
    _host_recoupling_invariants()
    _no_relationship_score_code()


def _roster_is_handles_only() -> None:
    raw = yaml.safe_load((ROOT / "data" / "islanders.yaml").read_text(encoding="utf-8"))
    allowed = {"name", "gender", "enters_on", "model"}
    for row in raw["islanders"]:
        extra = set(row) - allowed
        assert not extra, f"islanders.yaml has non-handle fields {extra} on {row.get('name')}"


def _profile_model_fields() -> None:
    from li_sim.models import IslanderProfile

    fields = set(IslanderProfile.model_fields)
    forbidden = {"age", "occupation", "hometown", "speaking_style", "values", "private_goal", "secrets", "dealbreakers", "archetype"}
    assert not (fields & forbidden), f"IslanderProfile still has persona fields: {fields & forbidden}"


def _agent_prompt_invariants() -> None:
    from li_sim.agent import handle_block, system_prompt, world_rules
    from li_sim.config import Settings
    from li_sim.engine import load_profiles

    profile = load_profiles()["Maya"]
    settings = Settings()
    blob = "\n".join(
        [
            world_rules(settings.prize_emphasis),
            handle_block(profile),
            system_prompt(profile, settings),
        ]
    )
    lower = blob.lower()
    positive_persona_markers = (
        "archetype:",
        "private goal:",
        "speaking style:",
        "you are maya,",
        "occupation from",
        "trust=",
        "attraction=",
        "relationship_updates",
    )
    for marker in positive_persona_markers:
        assert marker not in lower, f"agent prompt contains persona marker: {marker!r}"
    assert "your judgement" in lower
    assert "pick anyone" in lower or "pick anyone still" in lower


def _host_recoupling_invariants() -> None:
    source = inspect.getsource(
        __import__("li_sim.host", fromlist=["Host"]).Host.recoupling
    )
    upper = source.upper()
    assert "TAKEN — YOU CANNOT" not in upper and "TAKEN — YOU CANNOT" not in source
    assert "CAN STEAL" not in upper
    # Gender filter on pick pool removed — recoupling should not filter by picker_gender
    assert "picker_gender" not in source, "recoupling still filters partners by gender"


def _no_relationship_score_code() -> None:
    for path in SRC.rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "class Relationship" not in text, f"{path} defines Relationship scores"
        assert "apply_relationship_updates" not in text, f"{path} still applies relationship updates"
        assert "ensure_relationships" not in text, f"{path} still ensures relationship graph"


if __name__ == "__main__":
    run()
    print("prompt_invariants ok")
