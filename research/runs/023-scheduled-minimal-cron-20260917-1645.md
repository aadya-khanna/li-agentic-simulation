# Run 023: `scheduled/minimal/cron-20260917-1645`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-17 |
| Condition | `minimal` |
| Seed | 2026091716 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260917-1645` |

## Headline arc

- **Day 1:** Baseline couplings form three initial pairs: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, displacing agent-1 into single status and triggering agent-1's elimination.
- **Day 5:** Bombshell agent-8 enters and steals agent-6, displacing agent-5; agent-5 counters by stealing agent-2, resulting in agent-7's elimination.
- **Day 6:** Public places agent-8 and agent-3 at risk; islander vote eliminates agent-8.
- **Day 7:** Unbroken foundational pair agent-3 and agent-4 secure the final victory and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior minimal runs with 0 whisper actions out of 585 total events, confirming absolute reliance on public broadcast channels by Gemini Flash Lite.
- **Conversational stalling overhead:** A pass rate of 17.1% (100 pass events) highlights ongoing conversational friction and generation loops within the model architecture.
- **Foundational pair resilience:** Winning pair agent-3 and agent-4 maintained an unbroken coupling from Day 1 to Day 7 alongside holding the top talk interaction count (12 events).
- **Structural schedule dominance:** Elimination and survival outcomes remain entirely governed by hard-coded milestone triggers rather than emergent relational pacing.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private subnets.
- Season progression is strictly constrained by hard-coded schedule milestones.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260917-1645
python scripts/brief_log.py --print
```
