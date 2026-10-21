# Run 056: `scheduled/minimal/cron-20261021-1700`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-21 |
| Condition | `minimal` |
| Seed | 2026102117 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261021-1700` |

## Headline arc

- **Day 1:** Baseline couples establish: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 single; agent-5 pivots to steal agent-1, leaving agent-6 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-3, leaving agent-4 dumped.
- **Day 6:** Islanders vote to save agent-7, eliminating agent-8.
- **Day 7:** Original bombshell-stepped pair agent-2 and agent-7 win the season and £50,000.

## Insights

- **Bombshell-winner trajectory conversion:** Unlike prior runs where late cross-couples won, this iteration shows an early bombshell intervention (agent-7 stealing agent-2 on Day 3) successfully converting into a Day 7 win.
- **Strict zero-whisper channel constraint:** Replicates a 0.0 whisper rate across 571 events, forcing all negotiations completely into public broadcasts.
- **Flawless communication reciprocity:** Contact reciprocity remains fixed at 1.0 despite disruptive bombshell steals and subsequent eliminations.
- **Persistence of backend generation bottlenecks:** A pass rate of 18.04% (103 pass events) underscores ongoing token emission friction with the Flash Lite backend model.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Absolute absence of private whisper data restricts structural analysis exclusively to public dialogue.
- Progression remains bound to hard-coded chronological milestones rather than organic social timing.

## Next from this run

- [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability across varied seeds.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261021-1700
python scripts/brief_log.py --print
```
