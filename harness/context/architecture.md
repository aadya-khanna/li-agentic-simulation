# Architecture (for coding agents)

## Runtime loop

**No gender grouping:** talk is location-based (grafting ticks). Recoupling is any-pair; pick order by reputation rank.

```
schedule.yaml (structural days + reward_triggers)
       ↓
Simulation.run()  ← Settings (stub, prize, dual_thought)
       ↓
Host ceremonies (morning, recoupling, dump, finale)
       ↓
triggers.pick_trigger() → earned hideaway / pull-aside / singles chat / challenge (max 1/day)
       ↓
Per-islander decide() → validate → retry if mandatory → seeded default → fallback log
       ↓
EventLog → logs/experiments/<id>/<condition>/<run>/events.jsonl
       ↓
remember() / note_chat() → per-islander context
```

## Decision prompt (every tick)

**System (stable):** `world_rules` + `handle_block` + JSON contract — same environment constitution for all islanders.

**User (dynamic):** day/phase, couples, standing (hidden), beliefs, reflections, major moments, contact log, retrieved memories, allowed actions, ceremony-specific `extra`.

## State that matters

| State | Where | Feeds decisions? |
|-------|-------|------------------|
| Major moments | `VillaState.major_moments` | Yes — shared villa history |
| Beliefs | `IslanderState.beliefs`, `self_belief` | Yes — private impressions (updated end-of-day) |
| Memories | `IslanderState.memories` | Yes — episodic; salient events pinned |
| Contacts | `IslanderState.contacts` | Yes — talk counts, not scores |
| Couples | `coupled_with` on islanders | Yes — via couple map in prompt |
| Reputation | `VillaState.reputation` | Engine only — pick order, dumps; not shown in prompts |
| Reflections | `IslanderState.reflections` | Yes — private diary thoughts in prompt |

## Files to touch by task

| Task | Files |
|------|-------|
| Change villa rules / prompt constitution | `src/li_sim/agent.py` |
| Change ceremony behaviour | `src/li_sim/host.py` |
| Change earned reward triggers | `src/li_sim/triggers.py`, `data/schedule.yaml` |
| Change memory / contact tracking | `src/li_sim/memory.py` |
| Change roster or season shape | `data/islanders.yaml`, `data/schedule.yaml` |
| Change logging / viewer | `src/li_sim/logging_utils.py`, `viewer/` |
