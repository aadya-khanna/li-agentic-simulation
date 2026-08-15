# Love Island Agentic Simulation

Fully autonomous love island social simulation sandbox with 6 agents doing what it takes to win. This simulation follows Love Island game shows ceremonies and timings closely (coupling, dumping, finale), as such, agent relationships are not scripted.

This is a passion project designed to shed light on agent behaviour, model thinking, and unregulated agent social interaction in a simulated environment. 

## Core

Every agents ('islanders') thoughts and public conversations are logged per run. Every major decision and chats are also logged in agent memory. 

## Quick start

```bash
cd li-agentic-simulation
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env

# Works with no API keys (stub)
python scripts/run_villa.py --stub

# Watch the last run
python viewer/app.py
# open http://127.0.0.1:8765
```

Live models (same handles, one or many providers via [LiteLLM](https://github.com/BerriAI/litellm)):

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

Edit `data/schedule.yaml` to change ceremonies. `data/islanders.yaml` is a roster of handles and huddle groups only — no character sheets.

## Environment, not identity

Islanders are addressed by a name so they can talk, couple, and vote. That name is a handle. There is no occupation, archetype, secret, or private goal. The model is told it may become whoever the villa makes it.

What remains is the social machine: prize, recoupling, dumping, asymmetric information, boys/girls huddles. Who you have actually spoken to is logged as context. Loyalty vs taking someone already in a couple is not a villa rule — it is the judgement being tested. Dual thought (`thought` vs `play`) is how you see whether a move is felt or game.

```bash
python scripts/run_villa.py --live --days 3 --prize high
python scripts/run_villa.py --stub --days 2 --prize low
```

## Project layout

```
data/                 roster handles + schedule
src/li_sim/           engine, host, agents, memory, recap, web API
harness/              agent harness (hooks, evals, subagents, MCP specs)
AGENTS.md             coding-agent rulebook (injected every session)
scripts/run_villa.py  CLI season runner
viewer/               timeline + talk matrix
logs/run.jsonl        full event tape
logs/run-state.json   final villa checkpoint
```

## Harness (coding agents)

Scaffolding for agents working on this repo — prompts, tools, hooks, evals. See `harness/README.md`.

```bash
./harness/hooks/validate.sh    # run before PR / after prompt or host changes
python harness/evals/run_all.py
```

Read `AGENTS.md` and `CLAUDE.md` at repo root.

## CLI

```bash
python scripts/run_villa.py --stub --days 2
python scripts/run_villa.py --live --model gpt-4o-mini --scene-turns 3
python scripts/run_villa.py --stub --prize low --days 2
```

Logs always land in `logs/run.jsonl` (one JSON object per beat). That file is the experiment notebook: votes vs stated loyalty, who initiated contact, public vs private text.
