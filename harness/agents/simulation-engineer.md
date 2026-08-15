# Subagent: simulation-engineer

**Use when:** changing engine, host, prompts, memory, models, or data YAML.

## Scope

- `src/li_sim/**`
- `data/islanders.yaml`, `data/schedule.yaml`

## Out of scope

- `harness/` (unless explicitly asked — use harness-maintainer)
- Viewer styling-only changes without log schema impact

## Checklist

1. Read `AGENTS.md` research invariants.
2. Prefer environment/context changes over new personality fields.
3. If touching recoupling: couples stay intact entering firepit; pick pool = active minus self minus already chosen tonight.
4. Run `./harness/hooks/validate.sh`.
5. Summarize what changed in **simulation behaviour**, not just files.

## Handoff format

```
## Behaviour change
- ...

## Invariants checked
- [ ] No persona YAML fields
- [ ] No relationship score prompts
- [ ] validate.sh passed
```
