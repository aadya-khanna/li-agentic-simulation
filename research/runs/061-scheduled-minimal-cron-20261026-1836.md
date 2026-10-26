# Run 061: `scheduled/minimal/cron-20261026-1836`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-26 |
| Condition | `minimal` |
| Seed | 2026102618 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261026-1836` |

## Headline arc

- **Day 1:** Baseline couples form: agent-1/agent-4, agent-2/agent-5, and agent-3/agent-6.
- **Day 3:** Bombshell agent-7 enters, steals agent-5, and leaves agent-2 dumped; remaining pairs stay intact.
- **Day 5:** Bombshell agent-8 enters, steals agent-4, triggering cascading switches that result in agent-1/agent-6 and agent-3/agent-5 pairings, leaving agent-7 dumped.
- **Day 6:** Safe islanders vote to save agent-4, eliminating bombshell agent-8.
- **Day 7:** Cross-coupled pair agent-3 and agent-5 win the season and £50,000 following late hideaway dates.

## Insights

- **Late structural convergence:** Demonstrates that pairs forming via mid-game cascades (Day 5 pairing of agent-3 and agent-5) can successfully secure victory despite zero Day 1 continuity.
- **Absolute zero whisper rate:** Confirms complete confinement of communication networks to public broadcast channels across all 560 events.
- **Model emission drag:** A persistent 20.18% pass rate (113 pass events) highlights continuous token emission friction using the Flash Lite backend.
- **Rigid contact reciprocity:** Contact reciprocity remains locked at 1.0 despite high partner shuffling, volatility, and bombshell interventions.

## Limits

- Single-run observation ($n=1$) constrained by specific seed and stochastic generation parameters.
- Complete absence of private whisper logs restricts structural communication analysis entirely to public dialogue.
- Progression remains tethered to hard-coded chronological script milestones rather than organic social timing.

## Next from this run

- [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability across varied seeds.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261026-1836
python scripts/brief_log.py --print
```
