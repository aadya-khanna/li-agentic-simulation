# Run 012: `scheduled/minimal/cron-20260905-0402`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-05 |
| Condition | `minimal` |
| Seed | 2026090504 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260905-0402` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Luca, Zara & Kai, Nia & Theo).
- **Day 3:** Bombshell Rio enters, stealing Nia; Theo is left single and dumped.
- **Day 4:** Hideaway dates conducted for Luca & Maya, Kai & Zara, and Nia & Rio.
- **Day 5:** Bombshell Freya enters, stealing Rio; Nia is left single and dumped.
- **Day 6:** Public vote places Rio at risk; Rio is dumped via islander vote.
- **Day 7:** Kai & Zara win the season and £50,000, tying on score with Luca & Maya.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior minimal runs with 0 whisper actions across 709 events, confirming that Gemini Flash Lite relies entirely on public speech channels.
- **Talk vs. couple network dissociation:** High dialogue frequency between Kai & Luca (32 exchanges) and Maya & Zara (28 exchanges) occurs outside official romantic pairings, showing broad socialization.
- **Structural schedule dominance:** Elimination and survival outcomes map strictly to hard-coded bombshell schedules rather than emergent social dynamics.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private strategies.
- Season progression is entirely governed by hard-coded schedule milestones rather than emergent social pacing.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260905-0402
python scripts/brief_log.py --print
```
