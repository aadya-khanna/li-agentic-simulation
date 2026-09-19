# Run 025: `scheduled/minimal/cron-20260919-1545`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-19 |
| Condition | `minimal` |
| Seed | 2026091915 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260919-1545` |

## Headline arc

- **Day 1:** Initial pairings form baseline couples (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters, steals agent-1 from agent-2; agent-2 retaliates by stealing agent-3, leaving agent-4 dumped.
- **Day 5:** Bombshell agent-8 enters, steals agent-7; agent-2 reunites with original partner agent-1, leaving agent-3 dumped.
- **Day 6:** Islander vote eliminates agent-8 following public risk designation.
- **Day 7:** Original Day 1 pair agent-1 and agent-2 reunite to win the season and £50,000.

## Insights

- **Total whisper absence:** Replicates prior runs with 0 whisper actions out of 566 total events, confirming absolute reliance on public broadcast architecture by Gemini Flash Lite.
- **Conversational friction:** A pass rate of 20.1% (114 pass events) indicates recurring generation loops and dialogue stalling within the model.
- **Revenge coupling dynamics:** Agent-2 actively navigated multiple partner displacements, successfully cycling through partnerships before reclaiming the original winning node (agent-1).
- **Zero-correlation talk networks:** The top-talking pair (agent-5 and agent-6, 12 interactions) failed to secure the win, ranking 6th in talk-winner contact metrics.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical private subnets.
- Season progression is strictly constrained by hard-coded schedule milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260919-1545
python scripts/brief_log.py --print
```
