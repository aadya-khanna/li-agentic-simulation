# Run 058: `scheduled/minimal/cron-20261023-1652`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-10-23 |
| Condition | `minimal` |
| Seed | 2026102316 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261023-1652` |

## Headline arc

- **Day 1:** Baseline couples establish: agent-1/agent-4, agent-2/agent-3, and agent-5/agent-6.
- **Day 3:** Bombshell agent-7 enters, steals agent-2, leaving agent-3 dumped; original pairs agent-5/agent-6 and agent-1/agent-4 hold.
- **Day 5:** Bombshell agent-8 enters, steals agent-1; agent-6 splits from agent-5 to couple with agent-4, leaving agent-5 dumped.
- **Day 6:** Safe islanders vote to save agent-7, eliminating agent-8.
- **Day 7:** Cross-coupled pair agent-4 and agent-6 win the season and £50,000 despite forming late on Day 5.

## Insights

- **Late cross-couple victory:** Unlike runs 057 (where original Day 1 pairs won) and 056 (where a bombshell-stepped pair won), this run demonstrates that a late structural pivot (agent-4 and agent-6 pairing on Day 5) can successfully claim victory.
- **Absolute zero whisper artifact:** Replicates a 0.0 whisper rate across 576 events, confirming that communication topologies remain locked to public broadcasts under this configuration.
- **Perfect contact reciprocity:** Contact reciprocity holds at 1.0 despite disruptive bombshell steals and late partner reconfigurations.
- **Backend generation drag:** A 16.84% pass rate (97 pass events) continues to signal persistent token emission friction with the Flash Lite model.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Total absence of private whisper data restricts structural analysis exclusively to public dialogue.
- Progression remains bound to hard-coded chronological milestones rather than organic social timing.

## Next from this run

- [ ] Execute multi-seed batch runs under the minimal condition to test winner distribution stability across varied seeds.
- [ ] Enforce whisper constraints via prompt engineering to evaluate if communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261023-1652
python scripts/brief_log.py --print
```
