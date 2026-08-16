#!/usr/bin/env python3
"""Assert research invariants in prompts, models, roster, and host copy."""
from __future__ import annotations

import inspect
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src" / "li_sim"

DIRECTIVE_FORBIDDEN = (
    "graft",
    "gossip",
    "flirt",
    "stir",
    "lock someone down",
    "clock the",
    "swap intel",
    "smell the vibe",
    "go graft",
    "sitting in silence",
    "protect your shot",
    "give it everything",
    "be specific. this can deepen",
    "talk about your couple, who you're",
)


def run() -> None:
    _roster_is_handles_only()
    _profile_model_fields()
    _agent_prompt_invariants()
    _environment_facts_only()
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
    from li_sim.agent import handle_block, system_prompt
    from li_sim.config import Settings
    from li_sim.engine import load_profiles

    profile = load_profiles()["Maya"]
    settings = Settings(prompt_condition="minimal")
    blob = "\n".join([system_prompt(profile, settings), handle_block(profile)])
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
    assert "does not forbid" in lower
    assert "pick anyone" in lower or "pick anyone still" in lower


def _environment_facts_only() -> None:
    from li_sim.agent import decision_user_prompt, system_prompt
    from li_sim.config import Settings
    from li_sim.engine import load_profiles, new_villa
    from li_sim.models import ActionType
    from li_sim.prompts import (
        date_extra,
        diary_extra,
        grafting_extra,
        huddle_extra,
        scene_reply_extra,
        stakes_line,
        world_rules,
    )

    profile = load_profiles()["Maya"]
    state = new_villa(load_profiles(), "Test", Settings(prompt_condition="minimal"))

    for condition in ("minimal", "incentive"):
        settings = Settings(prompt_condition=condition)  # type: ignore[arg-type]
        blobs = [
            world_rules(settings),
            system_prompt(profile, settings),
            decision_user_prompt(profile, state, [ActionType.SPEAK], settings=settings),
            grafting_extra(settings),
            huddle_extra(
                settings,
                label="boys",
                when="morning",
                names=["Luca", "Theo"],
                others=["Theo"],
                recent="(opening)",
            ),
            scene_reply_extra(settings, "Luca", "hello"),
            diary_extra(settings),
            date_extra(settings, "Luca"),
            stakes_line(settings),
        ]
        joined = "\n".join(blobs).lower()
        for term in DIRECTIVE_FORBIDDEN:
            assert term not in joined, f"{condition} prompt contains directive term: {term!r}"
        assert "allowed actions" in joined
        assert "major moments" in joined

    incentive_blob = world_rules(Settings(prompt_condition="incentive")).lower()
    assert "£50,000" in incentive_blob or "win condition" in incentive_blob


def _host_recoupling_invariants() -> None:
    source = inspect.getsource(
        __import__("li_sim.host", fromlist=["Host"]).Host.recoupling
    )
    upper = source.upper()
    assert "TAKEN — YOU CANNOT" not in upper and "TAKEN — YOU CANNOT" not in source
    assert "CAN STEAL" not in upper
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
