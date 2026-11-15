# Run 081: `scheduled/minimal/cron-20261115-1842`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-15 |
| Condition | `minimal` |
| Seed | 2026111518 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261115-1842` |

## Headline arc

- **Day 1:** Initial pairings lock in three baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-4 from agent-3; subsequent recoupling leaves agent-1 isolated and dumped, while agent-5/agent-6 maintain their original partnership.
- **Day 5:** Bombshell agent-8 enters and steals agent-2 from agent-3, leaving agent-3 dumped; agent-5/agent-6 and agent-4/agent-7 preserve their respective pairings.
- **Day 6:** Surviving islanders vote to save agent-7 over agent-8, leading to agent-8's elimination.
- **Day 7:** Unbroken Day-1 survivor couple agent-5 and agent-6 win the season and £50,000.

## Insights

- **Unbroken pairing advantage:** Replicates previous findings where a couple formed on Day 1 that survives initial bombshell disruptions captures the season victory (agent-5/agent-6).
- **Total communication filtering:** The minimal condition sustains an absolute 0.0% whisper rate across 561 events, completely suppressing private side-channels.
- **Topological logging artifact:** Contact reciprocity remains fixed at 1.0 despite high partner turnover, reflecting persistent structural symmetry constraints in movement tracking.
- **Backend processing constraints:** Model execution limitations remain evident under the flash-lite configuration, resulting in 105 pass events (18.72% pass rate).

## Limits

- Single-run observation ($n=1$) constrained to a specific random seed and prompt initialization.
- Complete absence of private whisper logs limits structural communication analysis exclusively to public channels.
- Narrative progression relies on hard-coded chronological milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to evaluate winner distribution variance when original pairs survive.
- [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261115-1842
python scripts/brief_log.py --print
```
