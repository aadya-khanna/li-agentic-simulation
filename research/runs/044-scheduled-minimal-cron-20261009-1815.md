# Run 044: `scheduled/minimal/cron-20261009-1815`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-09 |
| Condition | `minimal` |
| Seed | 2026100918 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261009-1815` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-5, triggering a cascade where agent-6 steals agent-4, leaving agent-1 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-2 from agent-3, leaving agent-3 dumped.
- **Day 6:** Safe islanders vote to eliminate bombshell agent-8 over agent-7.
- **Day 7:** Cross-coupled survivors agent-4 and agent-6 win the season and £50,000.

## Insights

- **Network-survival alignment:** Unlike previous minimal runs, the winning pair (agent-4 and agent-6) also held the highest talk-network contact volume (15 interactions), demonstrating a rare convergence between conversational frequency and structural longevity.
- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 572 events, maintaining the 0.0 whisper rate characteristic of the minimal condition.
- **Model generation friction:** A pass rate of 19.76% (113 pass events) continues to indicate token emission constraints under the Flash Lite backend.
- **Structural cascade mechanics:** Unlike runs where bombshells relentlessly target a single node, agent-7's intrusion on Day 3 forced a multi-agent reshuffling that successfully preserved and recombined secondary nodes into the ultimate winning pair.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261009-1815
python scripts/brief_log.py --print
```
