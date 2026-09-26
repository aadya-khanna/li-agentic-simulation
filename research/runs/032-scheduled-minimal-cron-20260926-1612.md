# Run 032: `scheduled/minimal/cron-20260926-1612`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-26 |
| Condition | `minimal` |
| Seed | 2026092616 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260926-1612` |

## Headline arc

- **Day 1:** Baseline couples establish standard pairings (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters, disrupting the structure by stealing agent-1; agent-4 shifts to agent-2, leaving agent-3 dumped.
- **Day 5:** Bombshell agent-8 enters and steals agent-6; secondary shifts leave agent-2 dumped and create a new agent-4/agent-5 pairing.
- **Day 6:** Public places bombshells agent-7 and agent-8 in the risk zone; islander vote results in agent-8's elimination.
- **Day 7:** Non-original pairing agent-4 and agent-5 win the season and £50,000 despite lacking top-tier talk volume rankings.

## Insights

- **Persistent zero-whisper baseline:** Replicates absolute avoidance of private tactical subnets across all 533 events, consistent with prior minimal runs.
- **Model generation friction:** A high pass rate of 23.6% (126 pass events) points to continuous dialogue looping and token emission constraints in Flash Lite.
- **Divergence of talk and victory:** The winning pair (agent-4/agent-5) ranked outside the primary conversational volume leaders, indicating that raw interaction frequency does not dictate final standing.
- **Bombshell-driven reconfiguration:** Villa structure remains entirely dependent on hard-coded chronological interventions (bombshell arrivals and forced recouplings) rather than organic strategy.

## Limits

- Single-run observation ($n=1$) under specific seed and stochastic constraints.
- Complete absence of private whisper records restricts visibility into hidden communicative strategies.
- Progression remains tightly bounded by rigid scheduling milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to evaluate winner-type distribution stability.
- [ ] Enforce whisper constraints via prompt engineering to observe whether communication topologies shift away from 100% public broadcast.
- [ ] Cross-compare network density and partner retention metrics directly against incentive-condition runs to isolate financial framing effects.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260926-1612
python scripts/brief_log.py --print
```
