# Run 037: `scheduled/minimal/cron-20261002-1745`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-02 |
| Condition | `minimal` |
| Seed | 2026100217 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261002-1745` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-5; agent-6 switches to agent-2, leaving agent-1 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-7, leaving agent-5 dumped.
- **Day 6:** Public places bombshells agent-7 and agent-8 at risk; islander vote results in agent-8's elimination.
- **Day 7:** Original Day-1 pairing agent-3 and agent-4 maintain their coupling throughout and win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 584 events, matching the 0.0 whisper rate observed in prior minimal runs.
- **Day-1 anchor resilience:** Original pairing agent-3 and agent-4 successfully resisted all external disruptions from bombshell arrivals and secured the win without ever switching partners.
- **Model generation friction:** A pass rate of 19.86% (116 pass events) continues to illustrate token emission limits and dialogue loops under the Flash Lite backend.
- **Environmental scaffolding dominance:** Structural reconfigurations remain entirely bound to hard-coded bombshell entrances and scheduled recouplings rather than autonomous agent strategy.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper logs prevents analysis of latent sub-network communication topologies.
- Simulation progression is tightly constrained by rigid chronological milestones rather than organic pacing.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test winner-type distribution stability.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261002-1745
python scripts/brief_log.py --print
```
