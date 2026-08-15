# Harness evals

Run via `./harness/hooks/validate.sh` or:

```bash
python harness/evals/run_all.py
python harness/evals/prompt_invariants.py
python harness/evals/smoke_season.py
```

| Eval | Asserts |
|------|---------|
| `prompt_invariants` | No persona YAML/model fields; open-identity prompts; no TAKEN/steal host copy; no relationship score code |
| `smoke_season` | Stub day-1 runs; events logged; contacts in checkpoint |

Add new evals when an agent repeats a mistake — ratchet, don't brainstorm.
