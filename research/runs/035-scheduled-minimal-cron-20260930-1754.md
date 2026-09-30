# Run 035: `scheduled/minimal/cron-20260930-1754`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-30 |
| Condition | `minimal` |
| Seed | 2026093017 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260930-1754` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-3; agent-2 switches to agent-5, leaving agent-6 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-5; agent-2 returns to agent-3, leaving bombshell agent-7 dumped.
- **Day 6:** Public places agent-8 and agent-5 at risk; islander vote leads to agent-8's elimination.
- **Day 7:** Original Day-1 pairing agent-1 and agent-4 maintain their unbroken run and win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 546 events, maintaining the 0.0 whisper rate characteristic of the minimal prompt condition.
- **Day-1 anchor resilience:** Original pairing agent-1 and agent-4 successfully resisted all external disruptions from bombshell arrivals and secured the win without ever switching partners.
- **Model generation friction:** A pass rate of 23.8% (130 pass events) continues to highlight LLM token emission limits and dialogue looping under the Flash Lite backend.
- **Environmental gatekeeping:** Structural shifts remain strictly bound to hard-coded bombshell entrances and scheduled recoupling events rather than emergent agent-driven strategies.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper logs prevents analysis of latent sub-network communication topologies.
- Simulation trajectory is tightly constrained by rigid chronological scheduling milestones rather than organic pacing.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test winner-type distribution stability.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260930-1754
python scripts/brief_log.py --print
```
