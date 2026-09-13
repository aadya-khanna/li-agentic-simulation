# Run 021: `scheduled/minimal/cron-20260913-1602`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-13 |
| Condition | `minimal` |
| Seed | 2026091316 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260913-1602` |

## Headline arc

- **Day 1:** Initial baseline couplings form three pairs (1-2, 3-6, 4-5).
- **Day 3:** Bombshell agent-7 enters, steals agent-4, leaving agent-5 dumped; remaining original pairs (1-2, 3-6) hold steady.
- **Day 5:** Bombshell agent-8 enters, steals agent-6, displacing agent-3; agent-3 pivots to steal agent-4, resulting in agent-7 being dumped.
- **Day 6:** Public places agents 6 and 8 at risk; islander vote saves agent-6 and eliminates agent-8.
- **Day 7:** Unbroken foundational pair agent-1 and agent-2 secure the final win and £50,000.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior minimal runs with 0 whisper actions out of 536 events, confirming absolute reliance on public broadcast channels by Gemini Flash Lite.
- **High conversational pass rate:** A pass rate of 24.3% (130 pass events) highlights persistent conversational stalling and loop tendencies within the model architecture.
- **Foundational pair resilience:** Agent-1 and agent-2 maintained an unbroken coupling from Day 1 to Day 7, directly translating low-volatility pairing into a season win.
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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260913-1602
python scripts/brief_log.py --print
```
