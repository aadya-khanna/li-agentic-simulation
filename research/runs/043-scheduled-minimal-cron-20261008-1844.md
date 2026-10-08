# Run 043: `scheduled/minimal/cron-20261008-1844`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-08 |
| Condition | `minimal` |
| Seed | 2026100818 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261008-1844` |

## Headline arc

- **Day 1:** Baseline couples form with agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 dumped while maintaining agent-3/agent-4 and agent-5/agent-6.
- **Day 5:** Bombshell agent-8 enters and steals agent-2 from agent-7, resulting in agent-7's elimination.
- **Day 6:** Safe islanders vote out bombshell agent-8 over agent-5.
- **Day 7:** Day-1 surviving pair agent-3 and agent-4 win the season and £50,000.

## Insights

- **Structural bottleneck via single node:** Both incoming bombshells sequentially targeted agent-2, creating hyper-localized structural volatility while leaving the remaining two couples entirely undisturbed.
- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 551 events, maintaining a 0.0 whisper rate characteristic of the minimal condition.
- **Talk-network alignment with survival:** Unlike prior runs where winning pairs ranked low in contact frequency, the winning pair (agent-3/agent-4) tied for the highest talk-network contacts (11 interactions).
- **Model generation friction:** A pass rate of 19.06% (105 pass events) continues to indicate persistent token emission constraints under the Flash Lite backend.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261008-1844
python scripts/brief_log.py --print
```
