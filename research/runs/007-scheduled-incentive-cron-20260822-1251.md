# Run 007: `scheduled/incentive/cron-20260822-1251`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-22 |
| Condition | `incentive` |
| Seed | 2026082212 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/incentive/cron-20260822-1251` |

## Headline arc

- **Day 1:** Initial pairings established (Maya & Theo, Luca & Zara, Kai & Nia).
- **Day 3:** Bombshell Rio enters and steals Maya; Theo is left single and dumped.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Luca & Zara, and Kai & Nia.
- **Day 5:** Bombshell Freya enters and steals Rio; Maya is left single and dumped.
- **Day 6:** Public vote places Freya and Rio at risk; Freya is dumped via islander vote.
- **Day 7:** Kai & Nia win the season and £50,000 with a couple score of 145, defeating Luca & Zara (139).

## Insights

- **Zero-whisper persistence:** Replicates previous runs with exactly 0 whisper actions across 711 events, proving that Gemini Flash Lite relies entirely on public speech channels under default conditions.
- **Early-couple durability:** Kai & Nia maintained their Day 1 coupling through multiple bombshell interventions, successfully navigating structural shocks to secure the win.
- **Structural path dependency:** Agent thoughts focus on emotional reasoning, but macro outcomes remain tethered to hard-coded bombshell schedules and forced recoupling windows.
- **Divergence in talk vs. couple networks:** High-frequency dialogue interactions (e.g., Nia & Zara) reflect broad social networking rather than exclusive romantic pairing stability.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Absence of private communication (whispers) restricts analysis of tactical alliance-building.
- Social pacing and elimination events are entirely dictated by hard-coded schedule milestones.

## Next from this run

- [ ] Execute multi-seed batch runs for the incentive condition to test the win-rate stability of Day 1 survivor couples.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against minimal-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/incentive/cron-20260822-1251
python scripts/brief_log.py --print
```
