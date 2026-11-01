# Run 067: `scheduled/minimal/cron-20261101-1750`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-01 |
| Condition | `minimal` |
| Seed | 2026110117 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261101-1750` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters, steals agent-1, and triggers a cascade resulting in agent-6 being dumped while agent-2/agent-3 and agent-4/agent-5 form new pairs.
- **Day 5:** Bombshell agent-8 enters and steals agent-4; agent-2/agent-3 remain stable while agent-5 is dumped.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8.
- **Day 7:** Stable mid-run formation couple agent-2 and agent-3 win the season and £50,000.

## Insights

- **Network-outcome alignment:** Replicating prior runs, the top talking pair (agent-2 and agent-3 with 18 interactions) successfully converted high conversational volume into a season win.
- **Zero whisper utilization:** Maintains an absolute absence of private communication channels across 585 events, showing total collapse into public broadcast.
- **Consistent generation drag:** The model backend exhibits an invariant pass rate of 17.09% (100 pass events), matching historical structural friction levels.
- **Locked reciprocity ceiling:** Contact reciprocity remains fixed at 1.0 despite high partner volatility, bombshell steals, and dynamic recoupling cascades.

## Limits

- Single-run observation ($n=1$) bound to a specific seed and stochastic configuration.
- Complete absence of private whisper records restricts social network topology analysis strictly to public text exchanges.
- System evolution relies entirely on chronological hard-coded milestone triggers rather than organic behavioral timing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to test winner distribution variance.
- - [ ] Enforce whisper constraints via prompt engineering to evaluate whether communication topologies diversify away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261101-1750
python scripts/brief_log.py --print
```
