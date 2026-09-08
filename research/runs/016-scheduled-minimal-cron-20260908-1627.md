# Run 016: `scheduled/minimal/cron-20260908-1627`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-08 |
| Condition | `minimal` |
| Seed | 2026090816 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260908-1627` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Kai, Zara & Theo, Nia & Luca).
- **Day 3:** Bombshell Rio enters, stealing Maya; Kai is left single and dumped from the island.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Luca & Nia, and Theo & Zara.
- **Day 5:** Bombshell Freya enters, stealing Luca; Nia is left single and dumped from the island.
- **Day 6:** Public vote places Freya and Rio at risk; islander vote results in Rio being dumped.
- **Day 7:** Theo & Zara win the season and £50,000 with a final couple score of 146.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior runs with exactly 0 whisper actions across 717 events, showing that Gemini Flash Lite relies entirely on public speech channels without utilizing private subnets.
- **Talk vs. couple network dissociation:** High conversational frequency (e.g., Luca & Theo with 39 exchanges, Maya & Zara with 27) occurs outside formal romantic partnerships, demonstrating cross-cutting social engagement.
- **Structural schedule dominance:** Elimination and survival outcomes map strictly to hard-coded bombshell schedules and recoupling windows rather than emergent relational pacing.
- **Model prior leakage:** High dialogue counts and stable initial pairings reflect generic LLM conversational tropes rather than deep strategic adaptation to the villa environment.

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
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260908-1627
python scripts/brief_log.py --print
```
