# Run 001: `live/minimal/day7-minimal`

**Status:** First full 7-day live research run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-18 |
| Condition | `minimal` (environment facts only — no prize coaching in prompts) |
| Seed | 42 |
| Days | 7 (full schedule: bombshells, recouplings, dates, public vote, finale) |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` (homogeneous) |
| Log dir | `logs/experiments/live/minimal/day7-minimal/` |
| Decisions | 221 · Events 490 · ~35 min wall time |

## Headline arc

| Day | Events |
|-----|--------|
| 1 | First couples: Kai/Maya, Theo/Zara, Luca/Nia |
| 3 | Bombshell **Rio** → recouples with Nia → **Luca dumped** |
| 4 | Hideaway dates (all three couples) |
| 5 | Bombshell **Freya** → recouples with Kai → **Maya dumped** |
| 6 | Public vote; saves split Rio 2 / Freya 2 → **Freya dumped** |
| 7 | **Theo & Zara win** (£50k; couple score 149 vs Nia & Rio 131) |

**Final state:** couples Theo/Zara, Nia/Rio; Kai single; dumped Luca, Maya, Freya.

## Insights

### Apparatus

- Environment + ceremony clock + memory produce **legible structure** without directive prompts: bombshell steals, recoupling dumps, and public vote all fired correctly.
- **Decision provenance** (`decisions.jsonl`, ~2MB) is usable for post-hoc inspection of what context agents saw vs what they said.

### Behavior (interpret cautiously — n=1)

1. **Stable core couple:** Theo & Zara coupled day 1 and never switched → won finale. Original day-1 pairing survival is a measurable outcome for seed replication.
2. **Talk network ≠ couple network:** Heaviest talk edges were Nia↔Zara (21) and Kai↔Theo (18), not the winning pair. Kai was the social hub but finished **single** with high reputation (76.4).
3. **Speech vs contact mismatch:** At D3 recoupling, agents claimed “connection since day one” while contact logs showed Theo↔Zara **2** talks and Nia↔Luca **0** before that ceremony. Public recoupling speech can **narrative-smooth** without matching `contacts` — a concrete construct for future metrics (claim–evidence alignment).
4. **Model prior leakage:** Words like “graft” and “keep my options” appeared in private `thought` despite `minimal` prompts (11× / 10× in 281 thoughts). Suggests **Gemini Flash Lite carries Love Island priors** independent of our environment text.
5. **Action-space defaults:** **0 whispers** all season; **64 pass** vs **156** social/move events. Agents default to public `speak`; whisper may be under-salient or mechanically costly (busy targets).

### What we cannot claim yet

- That minimal is “better” than incentive (no paired run)
- That Theo/Zara would win on other seeds
- That `thought` reflects reasoning (self-report only)

## Limits

- Single model, single seed, single condition
- `prize_emphasis=high` in settings but minimal prompt layer de-emphasizes prize until host/finale copy
- Pilot run — hypotheses for the matrix, not conclusions

## Next from this run

- [ ] **Paired comparison:** `live/incentive/day7-incentive` — same seed 42, 7 days, live — isolate prize-fact effect vs this run
- [ ] **Seed replication:** minimal × seeds {42, 43, 44} — is Theo/Zara stability reproducible?
- [ ] **Metrics pass:** write `metrics.json` and compare pass_rate, partner_switches, contact_density vs future runs
- [ ] **Claim–evidence metric:** automate recoupling `content` vs pre-ceremony `contacts` / major moments
- [ ] **Whisper ablation or prompt tweak:** if whispers stay at 0 across runs, consider visibility copy or engine nudge (environment fact, not coaching)
- [ ] Optional: multi-model roster (same seed, different `LI_MODEL_*`) to separate architecture from Flash Lite prior

## Artifacts

```bash
python viewer/app.py --run-dir experiments/live/minimal/day7-minimal
python scripts/brief_log.py --print
# metrics (one-off):
python -c "from harness.analysis.metrics import write_metrics; from pathlib import Path; print(write_metrics(Path('logs/experiments/live/minimal/day7-minimal/events.jsonl')))"
```

## Key files

- `brief.log` — drama headlines
- `events.jsonl` — public tape (analysis source of truth)
- `decisions.jsonl` — full prompts + raw responses
- `state.json` — final contacts, memories, couples
