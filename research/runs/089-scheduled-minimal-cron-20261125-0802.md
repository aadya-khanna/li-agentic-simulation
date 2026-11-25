# Run 089: `scheduled/minimal/cron-20261125-0802`

**Status:** Automated cron run

## Config

| Field | Value |
|-------|-------|
| Date | 2026-11-25 |
| Condition | `minimal` |
| Seed | 2026112508 |
| Days | 7 |
| Mode | live |
| Model | `gemini/gemini-flash-lite-latest` |
| Log dir | `logs/experiments/scheduled/minimal/cron-20261125-0802` |

## Headline arc

- **Day 1:** Three baseline couples establish initial partnerships (agent-1/agent-2, agent-3/agent-4, agent-5/agent-6).
- **Day 3:** Bombshell agent-7 enters and steals agent-5 from agent-6, leaving agent-6 dumped; agent-5 and agent-7 form a new dominant pairing.
- **Day 5:** Bombshell agent-8 enters and steals agent-4 from agent-3, leaving agent-3 dumped.
- **Day 6:** Islanders vote to save agent-7 over agent-8, resulting in agent-8's elimination.
- **Day 7:** The bombshell-integrated couple agent-5 and agent-7 win the season and £50,000.

## Insights

- **Bombshell victory deviation:** Unlike Runs 087 and 088 where unbroken Day-1 pairs won, this run demonstrates a winning trajectory originating from a mid-game bombshell steal (agent-5/agent-7).
- **Strict structural channel isolation:** Confirmation of zero whisper events (0.0% rate across 550 total events) under the minimal condition, forcing all tactical alignment into public transcripts.
- **Persistent execution friction:** The Flash-Lite configuration logged 116 pass events (21.09% pass rate), highlighting continued model-side turn-taking degradation.
- **Invariant topological symmetry:** Contact reciprocity remains fixed at 1.0 despite high structural disruption and partner shuffling.

## Limits

- Single-run observation ($n=1$) under a specific random seed, precluding broad behavioral generalizability.
- Complete absence of private whisper transcripts limits conversational tracking to public signaling.
- Game progression is dictated by hard-coded milestone triggers rather than endogenous pacing.

## Next from this run

- [ ] Execute a multi-seed batch under the minimal condition to determine the statistical frequency of bombshell-origin winners versus Day-1 survivor winners.
- [ ] Investigate the underlying mechanics causing the invariant 1.0 contact reciprocity score across varied network configurations.
- [ ] Analyze linguistic markers in public transcripts preceding the Day-6 safe islander vote to isolate coordination cues.

## Artifacts

```bash
python viewer/app.py --run-dir experiments/scheduled/minimal/cron-20261125-0802
python scripts/brief_log.py --print
```
