# Run 060: `scheduled/minimal/cron-20261025-1556`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-25 |
| Condition | `minimal` |
| Seed | 2026102515 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261025-1556` |

## Headline arc

- **Day 1:** Baseline couples establish: agent-1/agent-2, agent-3/agent-6, and agent-4/agent-5.
- **Day 3:** Bombshell agent-7 enters and steals agent-4, leaving agent-5 single; agent-1 pivots to agent-5, leaving agent-2 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-7, leaving agent-4 single; agent-4 immediately pivots to couple with agent-1, leaving agent-5 dumped.
- **Day 6:** Safe islanders vote unanimously to save agent-7, eliminating bombshell agent-8.
- **Day 7:** Late-formed cross-couple agent-1 and agent-4 win the season and £50,000 following consecutive hideaway dates.

## Insights

- **Late structural convergence:** Replicates prior runs showing that pairs forming midway through the simulation (Day 5 pivot between agent-1 and agent-4) can successfully claim victory despite missing Day 1 continuity.
- **Absolute zero whisper rate:** Maintains a strict 0.0 whisper rate across 579 events, confirming that communication topologies remain entirely confined to public channels.
- **Model emission friction:** A 19.17% pass rate (111 pass events) highlights persistent token emission drag for the Flash Lite backend.
- **Perfect contact reciprocity:** Contact reciprocity remains fixed at 1.0 despite high structural volatility, partner shuffling, and bombshell interruptions.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Total absence of private whisper data restricts structural analysis exclusively to public dialogue.
- Progression remains bound to hard-coded chronological milestones rather than organic social timing.

## Next from this run

- - [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability across varied seeds.
- - [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- - [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261025-1556
python scripts/brief_log.py --print
```
