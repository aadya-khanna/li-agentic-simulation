# Run 040: `scheduled/minimal/cron-20261006-0558`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-06 |
| Condition | `minimal` |
| Seed | 2026100605 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261006-0558` |

## Headline arc

- **Day 1:** Initial baseline couples form: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, triggering re-pairings where agent-1 moves to agent-5, leaving agent-6 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-3; agent-4 pivots to agent-2 while agent-1 and agent-5 unite, dumping agent-7.
- **Day 6:** Islander vote protects agent-2 and eliminates bombshell agent-8.
- **Day 7:** Non-Day-1 pairing agent-1 and agent-5 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 587 events, maintaining the 0.0 whisper rate characteristic of minimal condition runs.
- **Talk vs. couple network dissociation:** The winning pair (agent-1 and agent-5) ranked 4th in talk-network contacts, reinforcing that conversational frequency does not dictate final structural survival.
- **Model generation friction:** A pass rate of 17.04% (100 pass events) continues to demonstrate token emission constraints and loop limits under the Flash Lite backend.
- **Structural instability:** Zero Day-1 couples survived to win, contrasting with Run 038 and demonstrating high sensitivity to bombshell-induced routing shifts under identical prompt conditions.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper logs restricts analysis exclusively to public broadcast interactions.
- Simulation progression remains strictly bound to hard-coded chronological milestones rather than emergent social pacing.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test winner-type distribution stability.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261006-0558
python scripts/brief_log.py --print
```
