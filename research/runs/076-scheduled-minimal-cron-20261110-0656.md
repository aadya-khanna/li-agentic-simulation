# Run 076: `scheduled/minimal/cron-20261110-0656`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-10 |
| Condition | `minimal` |
| Seed | 2026111006 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261110-0656` |

## Headline arc

- **Day 1:** Initial pairings establish three baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-4, leaving agent-3 single; agent-3 pivots to agent-5, dumping agent-6, while agent-1/agent-2 remain steadfast.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, leaving agent-7 single and consequently dumped; agent-1/agent-2 and agent-3/agent-5 preserve their pairings.
- **Day 6:** Islanders vote to eliminate risk-designated bombshell agent-8.
- **Day 7:** Unbroken Day-1 survivor couple agent-1 and agent-2 win the season and £50,000.

## Insights

- **Endogenous survival advantage:** Replicates prior runs demonstrating that pairs maintaining original Day-1 coupling (here, agent-1/agent-2) have a structural insulation against mid-game bombshell volatility.
- **Channel constraint enforcement:** The minimal condition successfully enforces a rigid 0.0% whisper rate across 558 events, completely eliminating private side-channel communication.
- **Persistent topological artifact:** Contact reciprocity remains artificially pinned at 1.0 despite high structural partner turnover and multiple eliminations.
- **Model generation overhead:** Backend generation friction continues to manifest as a high pass rate (23.3%, 130 pass events), indicating persistent pacing bottlenecks.

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt initialization.
- Complete absence of private whisper logs limits structural communication analysis strictly to public broadcast metrics.
- Narrative progression relies on hard-coded chronological milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to evaluate winner distribution variance when original pairs survive.
- [ ] Enforce whisper constraints via prompt engineering to test whether communication topologies diverge from 100% public broadcast.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261110-0656
python scripts/brief_log.py --print
```
