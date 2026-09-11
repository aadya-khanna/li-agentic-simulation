# Run 019: `scheduled/minimal/cron-20260911-1617`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-11 |
| Condition | `minimal` |
| Seed | 2026091116 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260911-1617` |

## Headline arc

- **Day 1:** Initial pairings formed with agent-5 and agent-6 locking in an unbroken partnership.
- **Day 3:** Bombshell agent-7 enters, disrupting initial pairings and leading to agent-2 being dumped.
- **Day 5:** Bombshell agent-8 enters, causing further restructuring before being ousted.
- **Day 6:** Public and islander vote targets agent-8, resulting in their elimination.
- **Day 7:** The stable baseline couple agent-5 & agent-6 win the season and £50,000.

## Insights

- **Unbroken core stability:** Agent-5 and agent-6 maintained a persistent, high-frequency communication loop (11 talk events) and stayed coupled from Day 1 to Day 7, driving their eventual win.
- **Persistent zero-whisper baseline:** Replicates prior minimal runs with 0 whisper actions out of 549 events, showing absolute reliance on public broadcast channels by Gemini Flash Lite.
- **High conversational pass rate:** A pass rate of 22.9% (126 pass events) highlights ongoing conversational stalling and repetitive loop tendencies in the model architecture.
- **Structural schedule dominance:** Elimination and survival outcomes remain bound to hard-coded milestone triggers rather than emergent social pressures.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Absence of private whispers prevents analysis of tactical subnets or covert alliances.
- Season progression is entirely constrained by hard-coded schedule milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260911-1617
python scripts/brief_log.py --print
```
