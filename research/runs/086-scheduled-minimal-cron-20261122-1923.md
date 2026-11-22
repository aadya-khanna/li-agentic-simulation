# Run 086: `scheduled/minimal/cron-20261122-1923`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-22 |
| Condition | `minimal` |
| Seed | 2026112219 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261122-1923` |

## Headline arc

- **Day 1:** Three baseline couples establish initial alignment: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-4, leaving agent-3 single and dumped; agent-1/agent-2 and agent-5/agent-6 preserve their partnerships.
- **Day 5:** Bombshell agent-8 enters and steals agent-2, breaking up agent-1/agent-2; agent-1 retaliates by stealing agent-4 from agent-7, leaving agent-7 single and dumped.
- **Day 6:** Islanders vote to save agent-4 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Late-formed cross-initial couple agent-1 and agent-4 win the season and £50,000.

## Insights

- **Late-formation victory pattern:** Replicates prior runs where a cross-initial couple formed via mid-game bombshell restructuring captures the season win rather than an intact Day-1 pair.
- **Absolute whisper suppression:** The minimal condition maintains a strict 0.0% whisper rate (0 whispers across 549 events), forcing all communication into public spaces.
- **Invariant topological symmetry:** Contact reciprocity remains pinned at 1.0 despite substantial partner turnover, reflecting persistent spatial tracking artifacts in the simulation environment.
- **High action friction:** Flash-lite configuration yields 118 pass events (21.49% pass rate), highlighting continuous execution constraints during action phases.

## Limits

- Single-run observation ($n=1$) under a fixed random seed and prompt setting.
- Absence of private whisper logs restricts communication analysis exclusively to public channels.
- Chronological progression relies on hard-coded milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to quantify winner survival variance when Day-1 couples are disrupted.
- [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261122-1923
python scripts/brief_log.py --print
```
