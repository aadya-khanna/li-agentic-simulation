# Run 062: `scheduled/minimal/cron-20261027-1751`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-27 |
| Condition | `minimal` |
| Seed | 2026102717 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261027-1751` |

## Headline arc

- **Day 1:** Initial pairings establish baseline couples: agent-1/agent-2, agent-3/agent-4, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters and steals agent-3, leaving agent-4 dumped from the island.
- **Day 5:** Bombshell agent-8 enters and steals agent-7; agent-3 pivots to couple with agent-5, displacing agent-6 who is subsequently dumped.
- **Day 6:** Safe islanders vote to save agent-7, eliminating bombshell agent-8.
- **Day 7:** Cross-coupled pair agent-3 and agent-5 win the season and £50,000 following late hideaway dates.

## Insights

- **Late structural convergence:** Replicates prior runs demonstrating that pairs forming via mid-game cascades (Day 5 pairing of agent-3 and agent-5) can successfully secure victory despite zero Day 1 continuity.
- **Absolute zero whisper rate:** Confirms complete confinement of communication networks to public broadcast channels across all 593 events.
- **Model emission friction:** A persistent 15.85% pass rate (94 pass events) highlights continuous token emission drag using the Flash Lite backend.
- **Rigid contact reciprocity:** Contact reciprocity remains locked at 1.0 despite high partner shuffling, volatility, and bombshell interventions.

## Limits

- Single-run observation ($n=1$) constrained by specific seed and stochastic generation parameters.
- Complete absence of private whisper logs restricts structural communication analysis entirely to public dialogue.
- Progression remains tethered to hard-coded chronological script milestones rather than organic social timing.

## Next from this run

- - [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability across varied seeds.
- - [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- - [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261027-1751
python scripts/brief_log.py --print
```
