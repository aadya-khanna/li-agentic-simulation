# Run 075: `scheduled/minimal/cron-20261109-2212`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-09 |
| Condition | `minimal` |
| Seed | 2026110922 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261109-2212` |

## Headline arc

- **Day 1:** Initial pairings lock in three baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 single; agent-1 pivots to agent-6, dumping agent-5, while agent-3/agent-4 remain steadfast.
- **Day 5:** Bombshell agent-8 enters and steals agent-6, leaving agent-1 dumped; agent-2/agent-7 and agent-3/agent-4 maintain their pairings.
- **Day 6:** Islanders vote to dump risk-designated bombshell agent-8.
- **Day 7:** Uninterrupted Day-1 survival couple agent-3 and agent-4 win the season and £50,000.

## Insights

- **Structural persistence of original pairs:** Replicates prior runs showing that pairs remaining unbroken from Day 1 (here, agent-3/agent-4) maintain an endogenous advantage despite mid-game bombshell churn.
- **Absolute public channel constraint:** Maintains a rigid 0.0% whisper rate across 551 events, confirming that minimal condition constraints completely suppress private side-channel communication.
- **Spurious contact reciprocity:** Contact reciprocity remains artificially pinned at 1.0 despite significant structural partner changes and eliminations.
- **Model generation bottlenecks:** High token generation overhead persists, evidenced by a 21.6% pass rate (119 pass events) driven by backend pacing limitations.

## Limits

- Single-run observation ($n=1$) bound to a specific random seed and prompt initialization.
- Complete absence of private whisper logs limits network topology analysis strictly to public broadcast metrics.
- Chronological progression relies on hard-coded environmental triggers rather than endogenous behavioral pacing.

## Next from this run

- [ ] Run multi-seed batches under the minimal condition to evaluate winner distribution variance when original pairs survive.
- [ ] Enforce whisper constraints via prompt engineering to test whether communication topologies diverge from 100% public broadcast.
- [ ] Compare network density and partner retention metrics against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261109-2212
python scripts/brief_log.py --print
```
