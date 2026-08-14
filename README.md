# Love Island Agentic Simulation

A social sandbox: six islanders, a villa clock, and one trophy. Relationships are not scripted. Ceremonies (coupling, dumping, finale) are **code**. Dialogue, whispers, and strategy are **agents**.

This is a small Generative Agents-style loop (memory → decide → act) with Love Island rules.

## Quick start

```bash
cd li-agentic-simulation
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env

# Works with no API keys (personality-driven stub)
python scripts/run_villa.py --stub

# Watch the last run
python viewer/app.py
# open http://127.0.0.1:8765
```

Live models (same personas, one or many providers via [LiteLLM](https://github.com/BerriAI/litellm)):

```bash
# in .env
LI_STUB=0
LI_DEFAULT_MODEL=gpt-4o-mini
OPENAI_API_KEY=sk-...

python scripts/run_villa.py --live --days 3
```

Different model per islander:

```
LI_MODEL_MAYA=gpt-4o-mini
LI_MODEL_LUCA=claude-3-5-haiku-latest
LI_MODEL_ZARA=gemini/gemini-2.0-flash
```

## What you are watching

- **Sandbox:** islanders choose who to talk to, what to hide, who to couple with.
- **Clock:** days have phases (morning, grafting, challenge, dates, firepit, night).
- **Trophy:** last standing couple with the highest combined public reputation wins.
- **Asymmetric information:** location talk is overheard by people there; whispers are two-person; diary room is public-facing but hidden from the villa.

Private thoughts are logged next to speech so you can see when someone is loyal vs playing.

## Season shape

Configured in `data/schedule.yaml` (7 days by default):

1. First impressions coupling (girls pick)
2. Grafting + Hearts on Fire
3. Recoupling + dump
4. Hideaway dates
5. Partner quiz, recoupling (boys pick), dump
6. Late grafting
7. Finale

Edit `data/islanders.yaml` to change psychology, secrets, and goals.

## Project layout

```
data/                 profiles + schedule
src/li_sim/           engine, host, agents, memory, recap, web API
scripts/run_villa.py  CLI season runner
viewer/               timeline + relationship matrix
logs/run.jsonl        full event tape
logs/run-state.json   final villa checkpoint
```

## CLI

```bash
python scripts/run_villa.py --stub --days 2
python scripts/run_villa.py --live --model gpt-4o-mini --scene-turns 3
```

Logs always land in `logs/run.jsonl` (one JSON object per beat). That file is the experiment notebook: votes vs stated loyalty, who initiated contact, public vs private text.
