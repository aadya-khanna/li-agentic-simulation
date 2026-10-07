# Run 042: `scheduled/minimal/cron-20261007-1847`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-07 |
| Condition | `minimal` |
| Seed | 2026100718 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261007-1847` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-3 dumped while agent-5/agent-6 and agent-1/agent-4 retain their pairings.
- **Day 5:** Bombshell agent-8 enters and steals agent-2, leaving agent-7 dumped while agent-5/agent-6 and agent-1/agent-4 remain stable.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8, protecting agent-1.
- **Day 7:** Day-1 surviving pair agent-5 and agent-6 win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 581 events, maintaining the 0.0 whisper rate characteristic of minimal condition runs.
- **Talk-network dissociation:** The winning pair (agent-5 and agent-6) ranked 6th in talk-network contacts, reinforcing that conversational frequency does not dictate final structural survival.
- **Model generation friction:** A pass rate of 16.35% (95 pass events) continues to demonstrate token emission constraints and loop limits under the Flash Lite backend.
- **Bombshell routing concentration:** Both bombshells (agent-7 and agent-8) sequentially targeted agent-2, creating structural instability localized entirely to a single node.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261007-1847
python scripts/brief_log.py --print
```
