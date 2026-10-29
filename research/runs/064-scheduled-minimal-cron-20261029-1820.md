# Run 064: `scheduled/minimal/cron-20261029-1820`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-29 |
| Condition | `minimal` |
| Seed | 2026102918 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261029-1820` |

## Headline arc

- **Day 1:** Baseline couples established: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-2, triggering a cascade where agent-3 pairs with agent-6 and agent-5 pairs with agent-1, leaving agent-4 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-1, causing agent-5 to pair with agent-2, while agent-3 and agent-6 remain together, resulting in agent-7 being dumped.
- **Day 6:** Islanders vote to save agent-2, eliminating bombshell agent-8.
- **Day 7:** Stable mid-game pair agent-3 and agent-6 win the season and £50,000.

## Insights

- **Network-outcome alignment:** Unlike runs where early pairings persist or final-day shuffles win, the top talking pair (agent-3 and agent-6, with 17 interactions) successfully converted their high contact volume into a season win.
- **Absolute zero whisper rate:** Replicates prior runs showing a total absence of private communication channels, restricting all social dynamics strictly to public broadcasts across 582 events.
- **Persistent emission friction:** The model backend registered a 17.01% pass rate (99 pass events), demonstrating structural token generation drag invariant to seed variations.
- **Rigid reciprocity ceiling:** Contact reciprocity remains fixed at 1.0 despite high partner shuffling, cascading steals, and bombshell interventions.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261029-1820
python scripts/brief_log.py --print
```
