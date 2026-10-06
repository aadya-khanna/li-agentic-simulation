# Run 041: `scheduled/minimal/cron-20261006-1813`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-06 |
| Condition | `minimal` |
| Seed | 2026100618 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261006-1813` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-1, leaving agent-2 dumped while agent-5/agent-6 and agent-3/agent-4 retain their pairings.
- **Day 5:** Bombshell agent-8 enters and steals agent-3, leaving agent-4 dumped while agent-5/agent-6 remain stable and agent-1 couples with agent-7.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8, protecting agent-7.
- **Day 7:** Day-1 surviving pair agent-5 and agent-6 win the season and £50,000.

## Insights

- **Day-1 survival anomaly:** Unlike prior runs where initial couples completely dissolved, agent-5 and agent-6 survived the entire run intact to win.
- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 567 events, maintaining the 0.0 whisper rate characteristic of minimal condition runs.
- **Talk-network alignment:** The winning pair (agent-5 and agent-6) also ranked among the top talk pairs (9 interactions), aligning conversational frequency with final survival.
- **Model generation friction:** A pass rate of 18.17% (103 pass events) continues to demonstrate token emission constraints and loop limits under the Flash Lite backend.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261006-1813
python scripts/brief_log.py --print
```
