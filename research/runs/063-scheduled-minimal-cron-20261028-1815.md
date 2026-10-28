# Run 063: `scheduled/minimal/cron-20261028-1815`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-28 |
| Condition | `minimal` |
| Seed | 2026102818 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261028-1815` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-1, displacing agent-2 who subsequently couples with agent-3, leaving agent-4 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-6, triggering a cascade where agent-2 returns to agent-1 and agent-3 pairs with agent-5, leaving agent-7 dumped.
- **Day 6:** Safe islanders vote to save agent-6, eliminating bombshell agent-8.
- **Day 7:** Original Day 1 pair agent-1 and agent-2 reunite and win the season and £50,000.

## Insights

- **Day 1 retention variance:** Unlike prior runs (061, 062) where mid-game cascades dominated, this seed yielded a winning couple (agent-1/agent-2) originating directly from the Day 1 baseline.
- **Zero private channel utilization:** Confirms absolute confinement of communication networks to public broadcast channels across all 579 events, mirroring prior minimal runs.
- **Persistent emission friction:** The model backend maintains a high pass rate of 17.79% (103 pass events), showing structural token emission drag irrespective of seed changes.
- **Invariant reciprocity ceiling:** Contact reciprocity remains rigidly locked at 1.0 despite high volatility, partner shuffling, and bombshell interventions.

## Limits

- Single-run observation ($n=1$) limited to the specific seed and stochastic generation parameters.
- Complete absence of private whisper logs restricts structural communication analysis entirely to public dialogue.
- System progression remains governed by hard-coded chronological script milestones rather than organic social timing.

## Next from this run

- [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability across varied seeds.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261028-1815
python scripts/brief_log.py --print
```
