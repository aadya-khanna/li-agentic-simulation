# Run 002: `scheduled/minimal/cron-20260818-0415`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-08-18 |
| Condition | `minimal` |
| Seed | 2026081804 |
| Days | 7 |
| Mode | stub |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20260818-0415` |

## Headline arc

=== Day 1 ===
  • Maya coupled with Luca at the firepit.
  • Zara coupled with Theo at the firepit.
  • Nia coupled with Kai at the firepit.
  • Recoupling settled: Luca & Maya, Theo & Zara, Kai & Nia.

=== Day 3 ===
  • Bombshell Rio entered the villa.
  • Rio recoupled with Zara, splitting Zara & Theo (Theo left single).
  • Maya & Luca stayed together at the firepit.
  • Nia left Kai to recouple with Theo (Kai left single).
  • Recoupling settled: Rio & Zara, Luca & Maya, Nia & Theo.
  • Kai was dumped from the island.

=== Day 4 ===
  • Hideaway date: Luca & Maya (private).
  • Hideaway date: Rio & Zara (private).
  • Hideaway date: Nia & Theo (private).

=== Day 5 ===
  • Bombshell Freya entered the villa.
  • Freya recoupled with Rio, splitting Rio & Zara (Zara left single).
  • Luca & Maya stayed together at the firepit.
  • Theo left Nia to recouple with Zara (Nia left single).
  • Recoupling settled: Freya & Rio, Luca & Maya, Theo & Zara.
  • Nia was dumped from the island.

=== Day 6 ===
  • Maya voted to save Freya.
  • Luca voted to save Freya.
  • Zara voted to save Freya.
  • Theo voted to save Freya.
  • Rio was dumped from the island.

=== Day 7 ===
  • Luca & Maya won the season and £50,000.

## Insights

- Stub summarizer: automated note from brief.log and metrics.
- Events: 653; partner_switches=2; steals=4.

## Limits

- n=1; stub summarizer only (no live LLM analysis in this path).

## Next from this run

- [ ] Re-run summarizer with live LLM for richer interpretation.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20260818-0415
python scripts/brief_log.py --print
```
