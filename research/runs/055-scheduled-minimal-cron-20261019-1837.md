# Run 055: `scheduled/minimal/cron-20261019-1837`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-19 |
| Condition | `minimal` |
| Seed | 2026101918 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261019-1837` |

## Headline arc

- **Day 1:** Initial baseline couples form: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters, steals agent-5 from agent-6, leaving agent-6 to pivot and steal agent-1 from agent-2 (dumping agent-2).
- **Day 5:** Bombshell agent-8 enters, steals agent-4 from agent-3, leaving agent-3 to couple with agent-1 (dumping agent-6).
- **Day 6:** Islanders vote to save agent-7, resulting in the elimination of bombshell agent-8.
- **Day 7:** Cross-coupled pair agent-1 and agent-3 win the season and £50,000.

## Insights

- **Structural replication of zero whispers:** The run strictly maintains a 0.0 whisper rate (0 out of 557 events), forcing all social interactions entirely into public broadcast channels.
- **High network reciprocity:** Despite frequent partner switching and bombshell interventions, communication reciprocity remains locked at 1.0.
- **Elevated generation friction:** A pass rate of 20.83% (116 pass events) highlights persistent token emission bottlenecks with the flash-lite backend.
- **Dynamic cross-coupling success:** Winning pair agent-1 and agent-3 emerged from late-stage structural reorganization after initial baseline couples were broken apart.

## Limits

- Single-run observation ($n=1$) under specific stochastic and seed constraints.
- Total absence of private whisper data restricts structural analysis exclusively to public utterances.
- Simulation progression remains strictly dictated by hard-coded chronological milestones rather than organic social pacing.

## Next from this run

- [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261019-1837
python scripts/brief_log.py --print
```
