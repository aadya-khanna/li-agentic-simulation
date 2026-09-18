# Run 024: `scheduled/minimal/cron-20260918-1614`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-18 |
| Condition | `minimal` |
| Seed | 2026091816 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260918-1614` |

## Headline arc

- **Day 1:** Initial coupling forms three baseline pairs: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, leaving agent-3 single and resulting in agent-3's elimination.
- **Day 5:** Bombshell agent-8 enters and steals agent-2 from agent-7, leaving agent-7 single and resulting in agent-7's elimination.
- **Day 6:** Public places agent-8 and agent-5 at risk; islander vote eliminates agent-8.
- **Day 7:** Unbroken foundational pair agent-1 and agent-4 secure the final victory and £50,000.

## Insights

- **Absolute zero-whisper baseline:** Replicates previous minimal/scheduled runs with 0 whisper actions out of 531 total events, confirming total reliance on public broadcast channels by Gemini Flash Lite.
- **High conversational stalling:** A pass rate of 23.9% (127 pass events) indicates recurring conversational friction and generation loops within the model.
- **Foundational pair durability:** Winning pair agent-1 and agent-4 maintained an unbroken coupling from Day 1 to Day 7 alongside holding the top talk interaction count (12 events).
- **Targeted bombshell disruption:** Bombshells agent-7 and agent-8 repeatedly targeted agent-2 across successive recouplings, driving structural instability exclusively around one node.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260918-1614
python scripts/brief_log.py --print
```
