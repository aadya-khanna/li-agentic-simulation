# Run 015: `scheduled/minimal/cron-20260907-1739`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-09-07 |
| Condition | `minimal` |
| Seed | 2026090717 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260907-1739` |

## Headline arc

- **Day 1:** Initial pairings formed (Maya & Kai, Zara & Theo, Nia & Luca).
- **Day 3:** Bombshell Rio enters, stealing Maya; cascading switches leave Luca dumped.
- **Day 4:** Hideaway dates conducted for Maya & Rio, Kai & Zara, and Nia & Theo.
- **Day 5:** Bombshell Freya enters, stealing Rio; Maya is left single and dumped.
- **Day 6:** Public vote places Freya at risk; islander vote results in Rio being dumped instead.
- **Day 7:** Kai & Zara win the season and £50,000 with a couple score of 142.

## Insights

- **Persistent zero-whisper baseline:** Replicates prior runs with 0 whisper actions across 691 events, confirming that Gemini Flash Lite relies entirely on public speech channels without utilizing private subnets.
- **Talk vs. couple network dissociation:** High conversational frequency (e.g., Kai & Theo with 30 exchanges, Nia & Zara with 20) occurs outside formal romantic partnerships, demonstrating broad cross-cutting socialization.
- **Structural schedule dominance:** Elimination and survival outcomes map strictly to hard-coded bombshell schedules and recoupling windows rather than emergent relational pacing.
- **Model prior leakage:** High dialogue counts and stable initial pairings reflect generic LLM conversational tropes rather than deep strategic adaptation to the villa environment.

## Limits

- Single-run observation ($n=1$) under specific seed constraints using homogeneous model instances.
- Complete absence of whispers prevents analysis of tactical alliances or private strategies.
- Season progression is entirely governed by hard-coded schedule milestones rather than emergent social dynamics.

## Next from this run

- [ ] Execute multi-seed batch runs for the minimal condition to test win-rate stability across varied initial seeds.
- [ ] Implement explicit prompt constraints forcing whisper usage to test whether communication topologies shift away from 100% public broadcast.
- [ ] Compare network density and partner retention metrics directly against incentive-condition runs to isolate the behavioral effect of financial framing.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260907-1739
python scripts/brief_log.py --print
```
