# Run 034: `scheduled/minimal/cron-20260929-1759`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-29 |
| Condition | `minimal` |
| Seed | 2026092917 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260929-1759` |

## Headline arc

- **Day 1:** Initial pairings establish standard baseline couples (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-1 single; subsequent picks result in agent-4 being dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-7; agent-2 returns to agent-1, and agent-3 is subsequently dumped.
- **Day 6:** Public places bombshells agent-7 and agent-8 at risk; islander vote leads to agent-8's elimination.
- **Day 7:** Original Day-1 pairing agent-1 and agent-2 reunite and win the season and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 568 events, matching prior minimal runs.
- **Day-1 anchor reunion:** Unlike runs where original couples are permanently broken, agent-1 and agent-2 re-established their initial pairing by Day 5 and won the season.
- **Generation friction persists:** A pass rate of 20.7% (118 pass events) continues to demonstrate LLM token emission limits and dialogue looping under Flash Lite.
- **Environmental dependency:** Structural changes remain strictly gated by hard-coded bombshell arrivals and forced recouplings rather than autonomous agent strategies.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper logs limits insight into latent communication topologies.
- Simulation progression is tightly bound to rigid chronological scheduling milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test winner-type distribution stability.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260929-1759
python scripts/brief_log.py --print
```
