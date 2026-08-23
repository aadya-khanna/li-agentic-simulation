# Run 008: `scheduled/incentive/cron-20260823-1253`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-23 |
| Condition | `incentive` |
| Seed | 2026082312 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/incentive/cron-20260823-1253` |

## Headline arc

- **Day 1:** Initial pairings formed (Kai & Maya, Theo & Zara, Luca & Nia).
- **Day 3:** Bombshell Rio enters, stealing Maya; Kai is left single and dumped.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Luca & Nia, and Theo & Zara.
- **Day 5:** Bombshell Freya enters, stealing Theo; Zara is left single and dumped.
- **Day 6:** Public vote places Rio and Freya at risk; Freya is dumped via islander vote.
- **Day 7:** Luca & Nia win the season and £50,000 with a couple score of 153, defeating Maya & Rio (132).

## Insights

- **Persistent zero-whisper baseline:** Replicates previous runs with 0 whisper actions across 709 events, confirming that Gemini Flash Lite relies entirely on public speech channels.
- **Structural alignment over internal agency:** Agent self-reports emphasize relational continuity, yet final outcomes map directly to hard-coded bombshell schedules and recoupling windows.
- **High contact density without private subnets:** Achieved a 0.7857 contact density while maintaining zero hidden communication, illustrating broad public social structuring.
- **Divergence in network topologies:** High-frequency dialogue interactions (e.g., Maya & Nia, Luca & Rio) track broad social engagement rather than exclusive romantic pairing stability.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private strategies.
- Season progression is entirely governed by hard-coded schedule milestones rather than emergent social pacing.

## Next from this run

- - [ ] Execute multi-seed batch runs for the incentive condition to test win-rate stability across varied initial seeds.
- - [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- - [ ] Compare network density and partner retention metrics directly against minimal-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/incentive/cron-20260823-1253
python scripts/brief_log.py --print
```
