# Agent instructions

Love Island agentic simulation — research sandbox where **environment and accumulated context** drive islander decisions, not character sheets.

## Commands

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -e .
python scripts/run_villa.py --stub --days 1          # no API keys
python scripts/run_scheduled_season.py --stub       # cron parity dry-run (local)
./harness/hooks/validate.sh                          # harness gate (run before PR)
python harness/evals/run_all.py                      # evals only
python viewer/app.py                                 # replay logs at :8765
```

## Layout

| Path | Role |
|------|------|
| `src/li_sim/` | Engine, host ceremonies, islander prompts, memory, LLM |
| `data/islanders.yaml` | Roster slots only (`slot`, `enters_on`) — handles derived as `{model}-agent{n}` |
| `data/schedule.yaml` | Ceremony timing — environment determinism |
| `logs/experiments/<id>/<condition>/<run>/` | Experiment tape (`events.jsonl`, `decisions.jsonl`, `state.json`, `manifest.json`) |
| `logs/latest.json` | Pointer to the most recent run (viewer default) |
| `research/runs/` | Interpretive notes for full 7-day seasons (may be auto-committed by cron) |
| `harness/` | Harness layer: agents, tools, MCP specs, hooks, evals |

## Research invariants (do not regress)

- **Open identity:** names are handles; no occupation, archetype, secrets, or private goals.
- **No relationship maths:** no trust/attraction/threat scores; use talk history (`contacts`) + memories.
- **Recoupling morality:** anyone still in the villa may be picked; taking someone already coupled is agent judgement, not a host-enforced rule. Only ceremony bookkeeping: already chosen *tonight* is unavailable.
- **Private thought:** prompts and logs a private `thought` field separate from public `content`.
- **No gender grouping:** no segregated huddles; recoupling is any-pair with rank pick order.
- **Hidden standing:** agents do not see numeric public reputation in prompts; host reveals at-risk names only at eliminations.
- **Shared constitution:** `world_rules()` + `handle_block()` in `src/li_sim/agent.py` — every islander gets the same environment text.

## Editing guide

- Prompts / JSON contract → `src/li_sim/agent.py`
- Ceremonies, recoupling, dumps → `src/li_sim/host.py`
- Memory, contacts, beliefs → `src/li_sim/memory.py`, `src/li_sim/beliefs.py`
- Roster / schedule → `data/*.yaml` (no psychology fields)
- Coding-agent scaffolding → `harness/` (see `harness/README.md`)

## Do not

- Commit `.env`, API keys, or `logs/` artifacts (automated cron may commit **`research/runs/` only**)
- Reintroduce persona YAML fields or numeric relationship matrices
- Add identity-based filters to recoupling partner pools or "TAKEN — cannot pick" host copy
- Skip `./harness/hooks/validate.sh` after changing prompts, host logic, or models

## Harness ratchet

When an agent (human or coding) repeats a mistake, encode the fix in `AGENTS.md`, `harness/hooks/`, or `harness/evals/` — not as a one-off chat instruction. See [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/).
