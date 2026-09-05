# Run 013: `scheduled/minimal/cron-20260905-1458`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-05 |
| Condition | `minimal` |
| Seed | 2026090514 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260905-1458` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Kai, Zara & Theo, Nia & Luca).
- **Day 3:** Bombshell Rio enters, stealing Maya; Kai is left single and dumped.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Luca & Nia, and Theo & Zara.
- **Day 5:** Bombshell Freya enters, stealing Theo; Zara is left single and dumped.
- **Day 6:** Public vote places Freya at risk; islander vote leads to Freya being dumped.
- **Day 7:** Luca & Nia win the season and £50,000 with a couple score of 145.

## Insights

- **Maintained zero-whisper baseline:** Continues the pattern of 0 whisper actions across 697 events, indicating that Gemini Flash Lite relies entirely on public speech channels without utilizing private subnet features.
- **Talk vs. couple network dissociation:** High conversational frequency (e.g., Luca & Theo with 24 exchanges, Maya & Nia with 24) occurs outside formal romantic partnerships.
- **Structural schedule dominance:** Elimination and survival outcomes map strictly to hard-coded bombshell schedules and recoupling windows rather than emergent relational pacing.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private strategies.
- Season progression is entirely governed by hard-coded schedule milestones rather than emergent social dynamics.

## Next from this run

- - [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260905-1458
python scripts/brief_log.py --print
```
