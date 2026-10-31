# Run 066: `scheduled/minimal/cron-20261031-1708`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-31 |
| Condition | `minimal` |
| Seed | 2026103117 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261031-1708` |

## Headline arc

- **Day 1:** Baseline couples form with agent-1/agent-2, agent-3/agent-6, and agent-4/agent-5.
- **Day 3:** Bombshell agent-7 enters and steals agent-4, leaving agent-5 dumped, while initial couples agent-1/agent-2 and agent-3/agent-6 hold firm.
- **Day 5:** Bombshell agent-8 enters and steals agent-6, disrupting agent-3/agent-6; agent-3 pivots to agent-4 while agent-7 is dumped.
- **Day 6:** Islanders vote to save agent-2, resulting in the elimination of bombshell agent-8.
- **Day 7:** Original pairing agent-1 and agent-2 win the season and £50,000.

## Insights

- **Early-couple resilience:** Unlike prior runs where top conversation volume dictated the winner, the Day 1 persistent pairing of agent-1 and agent-2 successfully converted stability into a win despite ranking 3rd in talk volume.
- **Zero-whisper baseline:** Replicates previous minimal-condition runs with a 0.0% whisper rate across 561 events, proving that communication channels collapse entirely into public broadcasts.
- **Invariant generation friction:** The model backend maintained a stable pass rate of 17.65% (99 pass events), matching historical structural token-generation drag.
- **Reciprocity ceiling:** Contact reciprocity remains rigidly locked at 1.0, showing no variance despite bombshell disruptions and partner switches.

## Limits

- Single-run observation ($n=1$) bound to a specific seed and stochastic configuration.
- Complete absence of private whisper records restricts social network topology analysis to public text exchanges.
- System evolution relies entirely on chronological hard-coded milestone triggers rather than organic behavioral timing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to test winner distribution variance.
- [ ] Enforce whisper constraints via prompt engineering to evaluate whether communication topologies diversify away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261031-1708
python scripts/brief_log.py --print
```
