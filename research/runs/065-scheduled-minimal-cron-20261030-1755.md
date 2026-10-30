# Run 065: `scheduled/minimal/cron-20261030-1755`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-30 |
| Condition | `minimal` |
| Seed | 2026103017 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261030-1755` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters, splits agent-5/agent-6, and cascades through the villa, resulting in agent-6 being dumped while agent-1/agent-3 form a new connection.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, triggering further shifts where agent-2 pairs with agent-5 while agent-1/agent-3 remain steady, leaving agent-7 dumped.
- **Day 6:** Safe islanders vote to save agent-1, eliminating bombshell agent-8.
- **Day 7:** Mid-run formation couple agent-2 and agent-5 win the season and £50,000.

## Insights

- **Network-outcome alignment:** Replicating prior runs, the top talking pair (agent-2 and agent-5, with 12 interactions) successfully translated conversation volume into a season victory.
- **Zero whisper utilization:** Maintains an absolute absence of private communication channels across 580 events, restricting all social mechanics strictly to public broadcasts.
- **Consistent emission friction:** The model backend exhibits an 18.45% pass rate (107 pass events), displaying structural generation drag stable across different seeds.
- **Locked reciprocity ceiling:** Contact reciprocity remains fixed at 1.0 despite high partner volatility, bombshell steals, and dynamic recoupling cascades.

## Limits

- Single-run observation ($n=1$) bound to a specific seed and stochastic generation parameters.
- Complete absence of private whisper logs limits structural network analysis strictly to public dialogue.
- System progression remains governed by hard-coded chronological script triggers rather than organic social timing.

## Next from this run

- [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability across varied seeds.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261030-1755
python scripts/brief_log.py --print
```
