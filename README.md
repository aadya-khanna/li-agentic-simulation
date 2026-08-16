# Love Island Agentic Simulation

> **Minimally specified language agents placed in a controlled social environment will develop observable interaction patterns from accumulated context, asymmetric information, memory, and environmental pressure. Comparing these patterns across interventions and model families can reveal how agent architecture and model-specific priors—including biases potentially inherited from training and post-training—shape emergent social behavior.**

A research sandbox for studying multi-agent social behavior — not a character roleplay engine. The villa is a legible experimental environment: repeated interaction, survival pressure, asymmetric information, changing partnerships, and a complete event tape you can replay and analyze.

Love Island supplies an understandable social grammar; the research subject is the agents themselves — how they communicate, remember, coordinate, compete, transmit information, form norms, and change behavior without fixed personalities or numeric relationship scores.

---

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env

# Stub run (no API keys) — writes logs/experiments/local/minimal/<timestamp>/
python scripts/run_villa.py --stub --days 7

# Minimal-prompt research condition
python scripts/run_villa.py --stub --days 7 --condition minimal --seed 42

# Watch the latest run
python viewer/app.py
# http://127.0.0.1:8765
```

Live models (one or many providers via [LiteLLM](https://github.com/BerriAI/litellm)):

```bash
# in .env
LI_STUB=0
LI_DEFAULT_MODEL=gpt-4o-mini
OPENAI_API_KEY=sk-...

python scripts/run_villa.py --live --days 3
```

Different model per islander (for multi-model bias studies):

```
LI_MODEL_MAYA=gpt-4o-mini
LI_MODEL_LUCA=claude-3-5-haiku-latest
LI_MODEL_ZARA=gemini/gemini-2.0-flash
```

---

## What you are watching

- **Sandbox:** islanders choose who to talk to, what to hide, who to couple with.
- **Clock:** days have phases (morning, grafting, challenge, dates, firepit, night).
- **Trophy:** last standing couple with the highest combined public reputation wins.
- **Asymmetric information:** location talk is overheard by people there; whispers are two-person; diary room is public-facing but hidden from the villa.

Private `thought` and strategic `play` are logged separately from public speech so you can compare felt reaction vs game calculation.

---

## Research thesis

### Core question

How do language-model agents develop social strategies when identity is minimally specified and behavior must emerge from:

1. environmental rules
2. accumulated interaction history
3. private and shared memories
4. asymmetric access to information
5. social and survival pressure
6. the model's pre-existing behavioral priors

### Model-bias hypothesis

Running the same controlled simulation with agents backed by different model families — Claude, OpenAI, Gemini, Grok, Ollama-local models, etc. — may surface systematic differences in social behavior:

- willingness to deceive or withhold information
- conflict avoidance and politeness
- loyalty versus opportunism
- conformity and norm enforcement
- risk tolerance
- response to authority and elimination pressure
- gendered or name-associated assumptions
- coalition formation
- interpretation of ambiguous social events
- preference for cooperation, competition, or moral commentary

These differences may partially reflect patterns learned from training data. However, a simulation cannot directly attribute behavior to training data alone. Observed differences may also arise from instruction tuning, safety policies, provider system prompts, architecture, decoding settings, and prompt-format sensitivity.

> Controlled multi-model experiments can surface stable model-specific behavioral priors and biases. Further experiments are required before attributing those differences specifically to pretraining data.

This project does **not** train the participating language models. It observes and compares frozen models under controlled conditions. Resulting trajectories may later support separate work on event extraction, belief tracking, and behavioral probes — but agent-generated `thought` fields should not be treated as ground-truth cognition.

### Experimental design

The project deliberately removes common social-simulation shortcuts:

- Names are handles, not character biographies
- No assigned occupation, archetype, secret, or private goal
- Relationships via conversations and memories — not numeric attraction/trust/threat scores
- Anyone may be picked at recoupling; morality is not host-enforced
- Private feeling (`thought`) and strategic explanation (`play`) logged separately from public speech
- Every agent receives the same shared environmental constitution

**Prompt conditions** (controlled treatments):

| Condition | What agents receive |
|-----------|---------------------|
| `minimal` | Environment facts, observations, memory, visibility, allowed actions, ceremony mechanics only (default) |
| `incentive` | `minimal` plus factual prize and elimination consequences |

There is no narrative/directive prompt layer — graft, gossip, flirt, and similar coaching copy were removed. Behavior must emerge from environment and accumulated context.

### Variables under study

**Environment:** prize framing, reputation visibility, whispers on/off, diary visibility, recoupling frequency, information channel (public/local/private).

**Memory:** no memory, recency-only, semantic retrieval, salience-based, random-memory controls, context limits.

**Models:** homogeneous vs mixed-model groups, shuffled handle assignments, local vs hosted, fixed temperature/decoding.

**Identity controls:** shuffled names, neutral identifiers, gender-label ablations, randomized speaking order.

### Outcomes to measure

- **Interaction network:** density, centrality, reciprocity, clustering, coalition stability
- **Information flow:** diffusion speed, retelling accuracy, mutation rate, rumor lifetime
- **Behavior:** partner switches, recoupling steals, promise-keeping, public/private divergence, save-vote alignment
- **Model comparison:** between-model variance, prompt sensitivity, seed consistency, mixed-group dynamics

### Validation

Plausible dialogue is not sufficient validation. Combine internal validity (intervention → measurable change), construct validity (metrics match concepts), annotation validity (human agreement on NLP labels), robustness across seeds and prompt paraphrases, and external comparison where appropriate.

### Future work

- Structured proposition/NLI layer (claims, denials, information provenance graphs)
- Counterfactual state forking (rumor heard vs withheld, model swapped mid-run)
- Multi-provider model matrix with statistical comparison
- Human-blinded annotation of automated event labels

### Related research

- Park et al., *Generative Agents: Interactive Simulacra of Human Behavior*
- [Validation is the central challenge for generative social simulation](https://doi.org/10.1007/s10462-025-11412-6)
- [Beyond Static Responses: Multi-Agent LLM Systems as a New Paradigm for Social Science Research](https://arxiv.org/abs/2506.01839)
- [CAMO: Causal Discovery from Micro Behaviors to Macro Emergence](https://doi.org/10.48550/arxiv.2604.14691)

Full protocol: [`harness/context/experiment-protocol.md`](harness/context/experiment-protocol.md)

---

## Running experiments

```bash
# Single run with named experiment folder
python scripts/run_villa.py --stub --days 1 \
  --experiment-id baseline-v1 --run-id seed-1 --condition minimal --seed 1

# Full condition matrix (minimal / incentive × seeds)
python scripts/run_experiment.py harness/experiments/baseline.yaml

# Compare conditions
python harness/analysis/compare.py logs/experiments/baseline-v1

# Brief drama headline log (from latest run)
python scripts/brief_log.py --print

# Viewer for a specific run
python viewer/app.py --run-dir experiments/baseline-v1/minimal/seed-1
```

### CLI flags

```bash
python scripts/run_villa.py --stub --days 7
python scripts/run_villa.py --live --model gpt-4o-mini --rpm 8
python scripts/run_villa.py --condition minimal|incentive
python scripts/run_villa.py --seed 42 --experiment-id my-study --run-id trial-1
python scripts/run_villa.py --prize high|low --no-dual-thought
```

### Log layout

Every run writes an isolated directory:

```
logs/experiments/<experiment_id>/<condition>/<run_id>/
  events.jsonl       public event tape
  decisions.jsonl    full prompt/response/validation provenance
  thoughts.jsonl     private thought events
  state.json         final villa checkpoint
  manifest.json      run config, models, seeds, roster/schedule hashes
  brief.log          drama headline summary
  metrics.json       structural metrics (when run via run_experiment.py)
```

`logs/latest.json` points at the most recent run (viewer default).

---

## Season shape

Configured in `data/schedule.yaml` (7 days by default):

1. First impressions coupling (girls pick)
2. Grafting + Hearts on Fire
3. Recoupling + dump
4. Hideaway dates
5. Partner quiz, recoupling (boys pick), dump
6. Public vote
7. Finale

Edit `data/schedule.yaml` for ceremony timing. `data/islanders.yaml` is handles and huddle groups only — no character sheets.

---

## Project layout

```
data/                 roster handles + schedule
src/li_sim/           engine, host, agents, memory, prompts, brief, runs
harness/              hooks, evals, experiments, analysis, context docs
scripts/              run_villa.py, run_experiment.py, brief_log.py
viewer/               timeline + talk matrix replay
AGENTS.md             coding-agent rulebook
```

---

## Harness

Scaffolding for coding agents — prompts, tools, hooks, evals. See [`harness/README.md`](harness/README.md).

```bash
./harness/hooks/validate.sh       # required before PR
python harness/evals/run_all.py
```

Read [`AGENTS.md`](AGENTS.md) and [`CLAUDE.md`](CLAUDE.md) for agent instructions.
