# Run 022: `scheduled/minimal/cron-20260916-1638`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-16 |
| Condition | `minimal` |
| Seed | 2026091616 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260916-1638` |

## Headline arc

- **Day 1:** Baseline pairing forms three couples: agent-1/agent-2, agent-3/agent-6, and agent-4/agent-5.
- **Day 3:** Bombshell agent-7 enters and steals agent-5, leaving agent-4 single; agent-3 pivots to agent-4, resulting in agent-6 being dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-4; agent-3 pivots to agent-5, resulting in bombshell agent-7 being dumped.
- **Day 6:** Public puts agent-8 and agent-2 at risk; islander vote saves agent-2 and eliminates agent-8.
- **Day 7:** Late-formed pair agent-3 and agent-5 secure the final win and £50,000.

## Insights

- **Zero-whisper invariant:** Replicates prior minimal runs with 0 whisper actions out of 540 events, confirming absolute reliance on public broadcast channels by Gemini Flash Lite.
- **High conversational pass rate:** A pass rate of 23.1% (125 pass events) highlights persistent conversational stalling and loop tendencies within the model architecture.
- **Divergent talk vs. couple networks:** Top talk pairs (e.g., agent-4/agent-8 with 12 interactions) failed to win; winning pair agent-3/agent-5 had a modest contact rank of 5.
- **Structural schedule dominance:** Elimination and survival outcomes remain entirely governed by hard-coded milestone triggers rather than emergent relational pacing.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private subnets.
- Season progression is strictly constrained by hard-coded schedule milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260916-1638
python scripts/brief_log.py --print
```
