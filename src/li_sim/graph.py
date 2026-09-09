"""LangGraph wiring for the day/phase state machine.

This module owns *when* each phase of a day runs. It contains no simulation
logic of its own — every node is a thin wrapper around an existing
`Simulation`/`Host` method, and the conditional edges reproduce the exact
branching that used to live in `Simulation.run()`/`run_day()`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

from langgraph.graph import END, StateGraph

from .beliefs import update_beliefs_for_day
from .brief import print_brief_panel, summarize_events, write_brief_log
from .logging_utils import save_checkpoint
from .models import DayPlan
from .recap import print_day, print_finale

if TYPE_CHECKING:
    from .engine import Simulation


class DayState(TypedDict):
    plan: DayPlan
    tick_remaining: int


class SeasonState(TypedDict):
    days: list[DayPlan]
    plan_index: int
    season_over: bool


def build_day_graph(sim: "Simulation"):
    """Day subgraph: morning -> bombshells -> grafting ticks -> optional
    ceremonies -> earned rewards -> optional diary/beliefs/finale -> end of day.
    Mirrors `Simulation.run_day()` phase order and gating conditions verbatim.
    """

    def morning(s: DayState) -> DayState:
        plan = s["plan"]
        state = sim.state
        state.day = plan.day
        state.tick = 0
        sim.host.morning(state)
        return s

    def bombshells(s: DayState) -> DayState:
        plan = s["plan"]
        if plan.bombshell_slots:
            names = [sim.slots[slot].name for slot in plan.bombshell_slots if slot in sim.slots]
            sim.host.introduce_bombshells(sim.state, names)
        return {**s, "tick_remaining": plan.grafting_ticks}

    def grafting_tick(s: DayState) -> DayState:
        sim.state.tick += 1
        sim.grafting_tick()
        return {**s, "tick_remaining": s["tick_remaining"] - 1}

    def recoupling(s: DayState) -> DayState:
        plan = s["plan"]
        sim.host.recoupling(
            sim.state,
            sim.decide,
            plan.recoupling_label or "Recoupling",
            dump_singles=plan.recoupling_dump_singles,
        )
        return s

    def public_vote(s: DayState) -> DayState:
        plan = s["plan"]
        sim.host.public_vote_save(sim.state, sim.decide, plan.at_risk_count)
        return s

    def dumping(s: DayState) -> DayState:
        plan = s["plan"]
        sim.host.dumping(sim.state, sim.decide, plan.dump_count, plan.dump_mode)
        return s

    def earned_rewards(s: DayState) -> DayState:
        sim._fire_earned_rewards()
        return s

    def diary(s: DayState) -> DayState:
        sim.host.diary_round(sim.state, sim.decide)
        return s

    def beliefs(s: DayState) -> DayState:
        update_beliefs_for_day(sim.state, sim.profiles, sim.llm, sim.log, sim.settings)
        return s

    def finale(s: DayState) -> DayState:
        sim.host.finale(sim.state)
        return s

    def end_of_day(s: DayState) -> DayState:
        state = sim.state
        print_day(state, sim.log)
        brief = summarize_events(sim.log.events)
        write_brief_log(brief, sim.brief_path)
        print_brief_panel(brief, day=state.day)
        if state.season_over:
            print_finale(state)
        save_checkpoint(state, sim.settings.run_dir() / "state.json")
        return s

    # Router chain: each function decides the next node, cascading past any
    # phase this DayPlan doesn't enable. Order matches the original
    # if-statement sequence in Simulation.run_day() exactly.
    def route_finale(s: DayState) -> str:
        return "finale" if s["plan"].finale else "end_of_day"

    def route_beliefs(s: DayState) -> str:
        if sim.settings.belief_updates and not s["plan"].finale:
            return "beliefs"
        return route_finale(s)

    def route_diary(s: DayState) -> str:
        plan = s["plan"]
        if plan.diary and not plan.finale:
            return "diary"
        return route_beliefs(s)

    def route_dumping(s: DayState) -> str:
        return "dumping" if s["plan"].dumping else "earned_rewards"

    def route_public_vote(s: DayState) -> str:
        return "public_vote" if s["plan"].public_vote else route_dumping(s)

    def route_recoupling(s: DayState) -> str:
        return "recoupling" if s["plan"].recoupling else route_public_vote(s)

    def route_grafting_loop(s: DayState) -> str:
        if s["tick_remaining"] > 0:
            return "grafting_tick"
        return route_recoupling(s)

    graph = StateGraph(DayState)
    for name, fn in [
        ("morning", morning),
        ("bombshells", bombshells),
        ("grafting_tick", grafting_tick),
        ("recoupling", recoupling),
        ("public_vote", public_vote),
        ("dumping", dumping),
        ("earned_rewards", earned_rewards),
        ("diary", diary),
        ("beliefs", beliefs),
        ("finale", finale),
        ("end_of_day", end_of_day),
    ]:
        graph.add_node(name, fn)

    graph.set_entry_point("morning")
    graph.add_edge("morning", "bombshells")
    graph.add_edge("bombshells", "grafting_tick")
    graph.add_conditional_edges(
        "grafting_tick",
        route_grafting_loop,
        {
            "grafting_tick": "grafting_tick",
            "recoupling": "recoupling",
            "public_vote": "public_vote",
            "dumping": "dumping",
            "earned_rewards": "earned_rewards",
        },
    )
    graph.add_conditional_edges(
        "recoupling",
        route_public_vote,
        {"public_vote": "public_vote", "dumping": "dumping", "earned_rewards": "earned_rewards"},
    )
    graph.add_conditional_edges(
        "public_vote",
        route_dumping,
        {"dumping": "dumping", "earned_rewards": "earned_rewards"},
    )
    graph.add_edge("dumping", "earned_rewards")
    graph.add_conditional_edges(
        "earned_rewards",
        route_diary,
        {"diary": "diary", "beliefs": "beliefs", "finale": "finale", "end_of_day": "end_of_day"},
    )
    graph.add_conditional_edges(
        "diary",
        route_beliefs,
        {"beliefs": "beliefs", "finale": "finale", "end_of_day": "end_of_day"},
    )
    graph.add_conditional_edges(
        "beliefs",
        route_finale,
        {"finale": "finale", "end_of_day": "end_of_day"},
    )
    graph.add_edge("finale", "end_of_day")
    graph.add_edge("end_of_day", END)
    return graph.compile()


def build_season_graph(sim: "Simulation"):
    """Season graph: run each scheduled day's subgraph in order, stopping early
    on `season_over`, then the same finale-if-not-over fallback as before.
    """
    day_graph = build_day_graph(sim)

    def run_day(s: SeasonState) -> SeasonState:
        plan = s["days"][s["plan_index"]]
        day_graph.invoke({"plan": plan, "tick_remaining": 0}, config={"recursion_limit": 100})
        return {**s, "plan_index": s["plan_index"] + 1, "season_over": sim.state.season_over}

    def finale_check(s: SeasonState) -> SeasonState:
        if not sim.state.season_over:
            sim.host.finale(sim.state)
            print_finale(sim.state)
            save_checkpoint(sim.state, sim.settings.run_dir() / "state.json")
        return s

    def route_season(s: SeasonState) -> str:
        if s["season_over"] or s["plan_index"] >= len(s["days"]):
            return "finale_check"
        return "run_day"

    graph = StateGraph(SeasonState)
    graph.add_node("run_day", run_day)
    graph.add_node("finale_check", finale_check)
    graph.set_entry_point("run_day")
    graph.add_conditional_edges("run_day", route_season, {"run_day": "run_day", "finale_check": "finale_check"})
    graph.add_edge("finale_check", END)
    return graph.compile()
