# Architecture (for coding agents)

## Runtime loop

```
schedule.yaml (days/phases)
       ↓
Simulation.run()  ← Settings (stub, prize, dual_thought)
       ↓
Host ceremonies (morning, recoupling, dump, finale)
       ↓
Per-islander decide() → LLM or stub
       ↓
EventLog → logs/experiments/<id>/<condition>/<run>/events.jsonl
       ↓
remember() / note_chat() → per-islander context
```

## Decision prompt (every tick)

**System (stable):** `world_rules` + `handle_block` + JSON contract — same environment constitution for all islanders.

**User (dynamic):** day/phase, couples, reputation, major moments, contact log, retrieved memories, allowed actions, ceremony-specific `extra`.

## State that matters

| State | Where | Feeds decisions? |
|-------|-------|------------------|
| Major moments | `VillaState.major_moments` | Yes — shared villa history |
| Memories | `IslanderState.memories` | Yes — private, visibility-filtered |
| Contacts | `IslanderState.contacts` | Yes — talk counts, not scores |
| Couples | `coupled_with` on islanders | Yes — via couple map in prompt |
| Reputation | `VillaState.reputation` | Yes — public standings |
| Reflections | `IslanderState.reflections` | No — stored, not injected yet |

## Files to touch by task

| Task | Files |
|------|-------|
| Change villa rules / prompt constitution | `src/li_sim/agent.py` |
| Change ceremony behaviour | `src/li_sim/host.py` |
| Change memory / contact tracking | `src/li_sim/memory.py` |
| Change roster or season shape | `data/islanders.yaml`, `data/schedule.yaml` |
| Change logging / viewer | `src/li_sim/logging_utils.py`, `viewer/` |
