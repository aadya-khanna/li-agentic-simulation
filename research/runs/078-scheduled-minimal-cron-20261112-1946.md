# Run 078: `scheduled/minimal/cron-20261112-1946`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-12 |
| Condition | `minimal` |
| Seed | 2026111219 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261112-1946` |

## Headline arc

- **Day 1:** Initial pairings establish three baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 single and subsequently dumped; agent-5/agent-6 and agent-3/agent-4 preserve their original pairings.
- **Day 5:** Bombshell agent-8 enters and steals agent-4, leaving agent-3 single and dumped; agent-5/agent-6 remain intact while agent-2/agent-7 stay paired.
- **Day 6:** Islanders vote to save agent-7 over agent-8, resulting in agent-8's elimination.
- **Day 7:** Unbroken Day-1 survivor couple agent-5 and agent-6 win the season and £50,000.

## Insights

- **Day-1 couple resilience:** Replicates findings that pairs maintaining original Day-1 coupling (agent-5/agent-6) successfully insulate against mid-game bombshell volatility and secure victory.
- **Absolute channel suppression:** Minimal condition strictly enforces a 0.0% whisper rate across 561 events, completely eliminating private side-channels.
- **Topological artifacts:** Contact reciprocity remains artificially pinned at 1.0 despite high partner turnover, pointing to structural symmetry constraints in movement or logging.
- **Model generation overhead:** High backend pacing limitations persist, evidenced by a 21.03% pass rate (118 pass events).

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt initialization.
- Absence of private whisper logs restricts structural communication analysis entirely to public broadcast metrics.
- Narrative progression relies on hard-coded chronological milestone triggers rather than endogenous behavioral pacing.

## Next from this run

- - [ ] Run multi-seed batches under the minimal condition to evaluate winner distribution variance when original pairs survive.
- - [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- - [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261112-1946
python scripts/brief_log.py --print
```
