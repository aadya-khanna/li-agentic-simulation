# Harness

Scaffolding around the model — not the model itself. This repo treats the harness as a first-class artifact: prompts, tools, hooks, subagents, and evals that keep coding agents aligned with the simulation research design.

Inspired by [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/) (Osmani / Trivedy / HumanLayer / Anthropic).

```
Agent = Model + Harness
```

## Anatomy (this repo)

| Layer | Path | Purpose |
|-------|------|---------|
| Rulebook | `AGENTS.md`, `CLAUDE.md` | Injected every session; keep short, earn each line |
| Context | `harness/context/` | Architecture + research goals for agents |
| Subagents | `harness/agents/` | Focused roles (engineer, analyst, maintainer) |
| Tools | `harness/tools/` | Registry + how to invoke repo operations |
| MCP | `harness/mcp/` | Planned MCP servers (log inspection, run control) |
| Hooks | `harness/hooks/` | Deterministic gates: validate, block secrets |
| Evals | `harness/evals/` | Smoke runs + prompt/host invariants |
| Cursor rules | `.cursor/rules/` | File-scoped conventions |

## Quick start

```bash
./harness/hooks/validate.sh
```

Runs import check, research invariants, and a one-day stub season.

## Ratchet policy

1. Agent makes a repeatable mistake → add a rule to `AGENTS.md` or an eval in `harness/evals/`.
2. Eval passes on a capable model → consider removing redundant prompt text.
3. Every harness component should map to a behaviour you want (or a failure you've seen).

## Adding MCP later

See `harness/mcp/README.md` for the villa-logs server sketch. Wire it in Cursor/Claude MCP config when implemented; until then, agents use bash + `harness/tools/`.
