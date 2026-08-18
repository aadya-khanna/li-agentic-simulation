"""Generate research run notes from experiment tapes."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .config import LOG_DIR, ROOT, Settings
from .llm import LLMClient, parse_json_object
from .logging_utils import load_events
from .models import LogEvent

RESEARCH_RUNS = ROOT / "research" / "runs"
TEMPLATE_PATH = RESEARCH_RUNS / "_template.md"


def next_run_number() -> int:
    highest = 0
    for path in RESEARCH_RUNS.glob("[0-9][0-9][0-9]-*.md"):
        try:
            highest = max(highest, int(path.name[:3]))
        except ValueError:
            continue
    return highest + 1


def prior_run_notes(limit: int = 2) -> str:
    notes = sorted(RESEARCH_RUNS.glob("[0-9][0-9][0-9]-*.md"), key=lambda p: p.name, reverse=True)
    chunks: list[str] = []
    for path in notes[:limit]:
        chunks.append(f"--- {path.name} ---\n{path.read_text(encoding='utf-8')[:2500]}")
    return "\n\n".join(chunks) if chunks else "(none yet)"


def load_run_events(run_dir: Path) -> list[LogEvent]:
    path = run_dir / "events.jsonl"
    if not path.exists():
        return []
    return [LogEvent.model_validate(row) for row in load_events(path)]


def _top_contact_pairs(events: list[LogEvent], limit: int = 6) -> list[tuple[str, str, int]]:
    counts: Counter[tuple[str, str]] = Counter()
    for event in events:
        if event.kind not in {"speak", "whisper", "huddle", "date"}:
            continue
        if not event.actor or not event.target:
            continue
        pair = tuple(sorted((event.actor, event.target)))
        counts[pair] += 1
    return [(a, b, n) for (a, b), n in counts.most_common(limit)]


def build_event_excerpt(events: list[LogEvent]) -> str:
    lines: list[str] = []
    for event in events:
        if event.kind == "couple_choice":
            lines.append(f"D{event.day} pick: {event.actor} -> {event.target}: {(event.text or '')[:120]}")
        elif event.kind == "dump":
            dumped = event.extra.get("dumped") if event.extra else event.actor
            lines.append(f"D{event.day} dump: {dumped}: {(event.text or '')[:120]}")
        elif event.kind == "win":
            lines.append(f"D{event.day} win: {(event.text or '')[:160]}")
        elif event.kind == "host" and any(
            w in (event.text or "").lower() for w in ("bombshell", "recoupling", "text!")
        ):
            lines.append(f"D{event.day} host: {(event.text or '')[:160]}")
    pairs = _top_contact_pairs(events)
    if pairs:
        lines.append("Top talk pairs: " + ", ".join(f"{a}<->{b}({n})" for a, b, n in pairs))
    whispers = sum(1 for e in events if e.kind == "whisper")
    passes = sum(1 for e in events if e.kind == "pass")
    lines.append(f"Whispers: {whispers}, pass events: {passes}")
    return "\n".join(lines) if lines else "(no excerpt events)"


def load_run_context(run_dir: Path) -> dict[str, Any]:
    run_dir = run_dir if run_dir.is_absolute() else LOG_DIR / run_dir
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    brief = (run_dir / "brief.log").read_text(encoding="utf-8") if (run_dir / "brief.log").exists() else ""
    metrics: dict[str, Any] = {}
    metrics_path = run_dir / "metrics.json"
    if metrics_path.exists():
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    state: dict[str, Any] = {}
    state_path = run_dir / "state.json"
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
    events = load_run_events(run_dir)
    rel = run_dir.relative_to(LOG_DIR) if str(run_dir).startswith(str(LOG_DIR)) else run_dir
    return {
        "run_dir": str(rel.as_posix()),
        "manifest": manifest,
        "brief": brief,
        "metrics": metrics,
        "state": state,
        "excerpt": build_event_excerpt(events),
        "event_count": len(events),
    }


def _short_run_path(rel_run: str) -> str:
    prefix = "experiments/"
    return rel_run[len(prefix) :] if rel_run.startswith(prefix) else rel_run


def _format_note(
    *,
    number: int,
    slug: str,
    rel_run: str,
    manifest: dict[str, Any],
    headline_arc: str,
    insights: str,
    limits: str,
    next_steps: str,
) -> str:
    exp = manifest.get("experiment_id", "?")
    cond = manifest.get("prompt_condition", "?")
    run_id = manifest.get("run_id", "?")
    started = manifest.get("started_at", "")[:10] or datetime.now(UTC).date().isoformat()
    model = manifest.get("default_model", "?")
    stub = manifest.get("stub", False)
    mode = "stub" if stub else "live"
    log_dir = f"logs/{rel_run}"
    short = _short_run_path(rel_run)
    return f"""# Run {number:03d}: `{short}`

**Status:** {'Automated cron run' if exp == 'scheduled' else 'Full 7-day research run'}

## Config

| Field | Value |
|-------|-------|
| Date | {started} |
| Condition | `{cond}` |
| Seed | {manifest.get('seed', '?')} |
| Days | {manifest.get('season_days', 7)} |
| Mode | {mode} |
| Model | `{model}` |
| Log dir | `{log_dir}` |

## Headline arc

{headline_arc.strip()}

## Insights

{insights.strip()}

## Limits

{limits.strip()}

## Next from this run

{next_steps.strip()}

## Artifacts

```bash
python viewer/app.py --run-dir experiments/{short}
python scripts/brief_log.py --print
```
"""


def _stub_summary(context: dict[str, Any]) -> dict[str, str]:
    brief = context.get("brief") or "(empty brief)"
    metrics = context.get("metrics") or {}
    headline = brief if brief.strip() else "Season completed; see brief.log on runner."
    insights = (
        "- Stub summarizer: automated note from brief.log and metrics.\n"
        f"- Events: {context.get('event_count', 0)}; "
        f"partner_switches={metrics.get('partner_switches', '?')}; "
        f"steals={metrics.get('steal_count', '?')}."
    )
    limits = "- n=1; stub summarizer only (no live LLM analysis in this path)."
    next_steps = "- [ ] Re-run summarizer with live LLM for richer interpretation."
    return {
        "headline_arc": headline,
        "insights": insights,
        "limits": limits,
        "next_steps": next_steps,
    }


def _parse_summary_payload(raw: dict[str, Any]) -> dict[str, str]:
    def as_md(key: str, fallback: str = "") -> str:
        val = raw.get(key, fallback)
        if isinstance(val, list):
            return "\n".join(f"- {item}" for item in val)
        return str(val).strip()

    return {
        "headline_arc": as_md("headline_arc"),
        "insights": as_md("insights"),
        "limits": as_md("limits"),
        "next_steps": as_md("next_steps"),
    }


def generate_summary_text(context: dict[str, Any], settings: Settings | None = None) -> dict[str, str]:
    settings = settings or Settings()
    if settings.stub:
        return _stub_summary(context)

    system = """You are a research analyst for a multi-agent social simulation study.
Write concise, skeptical notes. Treat agent 'thought' fields as self-report, not ground truth.
Focus on: environment-driven structure, talk vs couple networks, model prior leakage, speech vs contact mismatches.
Do not claim human realism or training-data causation."""

    user = f"""Analyze this completed 7-day villa run and return JSON only:
{{
  "headline_arc": "markdown bullet list of main beats by day",
  "insights": "markdown bullet list of 3-6 research observations",
  "limits": "markdown bullet list of what we cannot conclude (n=1 etc)",
  "next_steps": "markdown checklist items starting with - [ ]"
}}

Prior research notes (for continuity):
{prior_run_notes()}

Run manifest:
{json.dumps(context['manifest'], indent=2)}

brief.log:
{context.get('brief') or '(empty)'}

metrics.json:
{json.dumps(context.get('metrics') or {}, indent=2)}

Final state (winners, dumped):
{json.dumps({k: context.get('state', {}).get(k) for k in ('winner_couple', 'dumped', 'day', 'season_over') if context.get('state')}, indent=2)}

Event excerpt:
{context.get('excerpt')}
"""
    client = LLMClient(settings)
    raw, text, _model = client.complete_json("Analyst", system, user)
    if not raw or raw == {}:
        try:
            raw = parse_json_object(text)
        except Exception:
            raw = _stub_summary(context)
            return raw
    return _parse_summary_payload(raw)


def slug_for_run(manifest: dict[str, Any]) -> str:
    exp = manifest.get("experiment_id", "run")
    cond = manifest.get("prompt_condition", "x")
    run_id = manifest.get("run_id", "unknown")
    safe = re.sub(r"[^a-zA-Z0-9-]+", "-", run_id).strip("-").lower()
    return f"{exp}-{cond}-{safe}"[:80]


def write_research_note(
    run_dir: Path,
    settings: Settings | None = None,
    *,
    number: int | None = None,
) -> Path:
    context = load_run_context(run_dir)
    manifest = context["manifest"]
    number = number or next_run_number()
    slug = slug_for_run(manifest)
    summary = generate_summary_text(context, settings)
    body = _format_note(
        number=number,
        slug=slug,
        rel_run=context["run_dir"],
        manifest=manifest,
        **summary,
    )
    out = RESEARCH_RUNS / f"{number:03d}-{slug}.md"
    out.write_text(body, encoding="utf-8")
    update_runs_index(number, manifest, out.name)
    return out


def update_runs_index(number: int, manifest: dict[str, Any], filename: str) -> None:
    readme = RESEARCH_RUNS / "README.md"
    exp = manifest.get("experiment_id", "?")
    cond = manifest.get("prompt_condition", "?")
    run_id = manifest.get("run_id", "?")
    started = manifest.get("started_at", "")[:10] or datetime.now(UTC).date().isoformat()
    stub = manifest.get("stub", False)
    mode = "stub" if stub else "live"
    rel_run = f"`{exp}/{cond}/{run_id}`"
    row = f"| [{number:03d}]({filename}) | {rel_run} | {cond} | {mode} | {started} |"

    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if filename in text:
            return
    else:
        text = "# Run summaries\n\nFull **7-day** seasons only. No smoke or truncated runs.\n\n"
        text += "| # | Run | Condition | Mode | Date |\n|---|-----|-----------|------|------|\n"

    if "| # | Run |" not in text:
        text += "| # | Run | Condition | Mode | Date |\n|---|-----|-----------|------|------|\n"
    text = text.rstrip() + "\n" + row + "\n"
    readme.write_text(text, encoding="utf-8")
