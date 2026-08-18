# Run 003: `scheduled/incentive/cron-20260818-0650`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-18 |
| Condition | `incentive` |
| Seed | 2026081806 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/incentive/cron-20260818-0650` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Theo, Luca & Zara, Kai & Nia).
- **Day 3:** Bombshell Rio enters and steals Nia; Kai is left single and dumped.
- **Day 4:** Hideaway dates conducted for all three established couples.
- **Day 5:** Bombshell Freya enters and steals Theo; Maya is left single and dumped.
- **Day 6:** Public vote places Rio and Freya at risk; Rio is dumped after failing to secure enough votes.
- **Day 7:** Luca & Zara win the season and £50,000 with a couple score of 148.

## Insights

- **Stable core retention:** Luca & Zara maintained their pairing from Day 1 through Day 7, successfully winning despite intervening bombshell disruption.
- **Zero whisper utilization:** Agents recorded 0 whispers across 711 events, relying entirely on public speech and structured actions.
- **Top talk network divergence:** The highest frequency talk pair was Luca & Theo (27), despite not being romantically coupled, pointing to cross-cutting social maintenance.
- **Self-report vs behavior:** Agent thoughts heavily lean on internal narrative framing (e.g., strong connections) that occasionally mask tactical recoupling choices required by the ceremony clock.

## Limits

- Single-run observation ($n=1$) using homogeneous Gemini Flash Lite instances.
- Results reflect specific prompt conditions (incentive-heavy) and seed constraints; broader generalizability requires multi-seed replication.
- Action space constraints (e.g., zero whispers, 44 passes) limit dynamic tactical signaling.

## Next from this run

- - [ ] Run multi-seed replication across the incentive condition to test stability of early pairing survival.
- - [ ] Introduce whisper-incentivized constraints to test if communication topologies shift away from 100% public speak.
- - [ ] Perform cross-run comparison against minimal prompt conditions to isolate the effect of prize-emphasis framing on talk networks.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/incentive/cron-20260818-0650
python scripts/brief_log.py --print
```
