# Claude Code / Claude agent context

Read **`AGENTS.md`** first — it is the canonical rulebook for every coding agent in this repo.

## Harness entrypoints

- Architecture map: `harness/context/architecture.md`
- Research goals: `harness/context/research-goals.md`
- Subagent specs: `harness/agents/`
- Tool registry: `harness/tools/registry.yaml`
- MCP plans: `harness/mcp/README.md`
- Validation hook: `./harness/hooks/validate.sh`
- Eval suite: `python harness/evals/run_all.py`

## Default workflow

1. Read the task against research invariants in `AGENTS.md`.
2. Change the smallest surface in `src/li_sim/` or `data/`.
3. Run `./harness/hooks/validate.sh` before declaring done.
4. If validation fails, fix and re-run — do not hand off broken harness state.

## Simulation smoke test

```bash
python scripts/run_villa.py --stub --days 1
```

Logs land in `logs/run.jsonl`. Use the viewer or `harness/tools/inspect-logs.md` to read them.
