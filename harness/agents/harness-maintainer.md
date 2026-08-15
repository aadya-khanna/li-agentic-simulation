# Subagent: harness-maintainer

**Use when:** adding hooks, evals, MCP specs, AGENTS.md rules, or Cursor rules after agent failures.

## Scope

- `harness/**`
- `AGENTS.md`, `CLAUDE.md`
- `.cursor/rules/**`

## Ratchet workflow

1. Observe repeatable agent mistake (e.g. reintroduced persona field, skipped validation).
2. Add smallest fix: eval assertion > hook > AGENTS.md line (in that preference order when possible).
3. Run `./harness/hooks/validate.sh` to prove the ratchet holds.

## Keep AGENTS.md under ~60 lines

Every new rule must trace to a failure or hard external constraint. Remove rules when evals prove they're redundant.

## Do not

- Bloat tool registry with overlapping entries
- Add MCP servers to config without a spec in `harness/mcp/`
