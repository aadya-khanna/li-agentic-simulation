# Run 077: `scheduled/minimal/cron-20261110-1934`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-10 |
| Condition | `minimal` |
| Seed | 2026111019 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261110-1934` |

## Headline arc

- **Day 1:** Baseline pairings establish three couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 steals agent-2, triggering cascading swaps; agent-1 pairs with agent-3 while agent-4 is dumped, and agent-5/agent-6 remain intact.
- **Day 5:** Bombshell agent-8 steals agent-6; agent-5 pivots to steal agent-2, leaving agent-7 dumped, while agent-1/agent-3 maintain their pairing.
- **Day 6:** Islanders vote to eliminate bombshell agent-8 over agent-6.
- **Day 7:** Non-Day-1 survivor couple agent-2 and agent-5 win the season and £50,000.

## Insights

- **Day-1 survival not required:** Unlike prior runs where original pairings dominated, this run demonstrates that a late-formed hybrid pair (agent-2/agent-5) can successfully claim victory after extensive mid-game shuffling.
- **Absolute channel suppression:** The minimal condition strictly maintains a 0.0% whisper rate across 581 events, confirming total elimination of private side-channels.
- **Persistent topological artifact:** Contact reciprocity remains artificially pinned at 1.0 despite high partner turnover, pointing to structural symmetry constraints in the logging or movement mechanics.
- **Generation overhead:** High backend pacing limitations persist, evidenced by a 17.73% pass rate (103 pass events).

## Limits

- Single-run observation ($n=1$) constrained to a specific random seed and prompt initialization.
- Complete lack of private whisper logs limits network analysis entirely to public broadcast interactions.
- Narrative progression relies on hard-coded chronological milestone triggers rather than fully endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to test winner distribution variance when non-original pairs win.
- [ ] Investigate the root cause of the invariant 1.0 contact reciprocity score across varied network topologies.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261110-1934
python scripts/brief_log.py --print
```
