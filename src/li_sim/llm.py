from __future__ import annotations

import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from typing import Any

from .config import Settings, islander_model
from .models import Action, ActionType, Location
from .rng import derive_seed, seeded_rng


def _api_key_for_model(model: str) -> str | None:
    prefix = model.split("/", 1)[0].lower()
    if prefix == "gemini":
        return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or None
    if prefix in {"anthropic", "claude"}:
        return os.getenv("ANTHROPIC_API_KEY") or None
    if prefix == "groq":
        return os.getenv("GROQ_API_KEY") or None
    key = os.getenv("OPENAI_API_KEY")
    return key or None


def parse_json_object(text: str) -> dict[str, Any]:
    text = (text or "").strip()
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    if fenced:
        text = fenced.group(1)
    else:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            text = text[start : end + 1]
    return json.loads(text)


class GeminiRateLimitError(RuntimeError):
    def __init__(self, retry_after: float, detail: str = ""):
        self.retry_after = retry_after
        super().__init__(detail or f"rate limited, retry in {retry_after:.0f}s")


class RateLimiter:
    def __init__(self, rpm: float):
        self.min_interval = 60.0 / max(rpm, 0.5)
        self._next = 0.0

    def wait(self) -> None:
        now = time.monotonic()
        delay = self._next - now
        if delay > 0:
            time.sleep(delay)
        self._next = time.monotonic() + self.min_interval


def _gemini_model_id(model: str) -> str:
    name = model.split("/", 1)[-1]
    if name.startswith("models/"):
        name = name[len("models/") :]
    return name


def _gemini_complete(
    model: str,
    system: str,
    user: str,
    *,
    temperature: float,
    max_tokens: int,
    api_key: str | None,
) -> str:
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing")
    model_id = _gemini_model_id(model)
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_id}:generateContent?key={api_key}"
    )
    payload = {
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens,
            "responseMimeType": "application/json",
        },
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        if exc.code == 429:
            retry_after = 65.0
            header = exc.headers.get("Retry-After") if exc.headers else None
            if header:
                try:
                    retry_after = float(header)
                except ValueError:
                    pass
            raise GeminiRateLimitError(retry_after, detail[:180]) from exc
        raise RuntimeError(f"Gemini HTTP {exc.code}: {detail[:180]}") from exc
    parts = (
        ((body.get("candidates") or [{}])[0].get("content") or {}).get("parts") or []
    )
    texts = [str(part.get("text") or "") for part in parts if not part.get("thought")]
    if not texts:
        texts = [str(part.get("text") or "") for part in parts]
    return "\n".join(t for t in texts if t).strip()


def _litellm_complete(
    model: str,
    system: str,
    user: str,
    *,
    temperature: float,
    max_tokens: int,
) -> str:
    from litellm import completion

    kwargs: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    api_key = _api_key_for_model(model)
    if api_key:
        kwargs["api_key"] = api_key
    response = completion(**kwargs)
    return response.choices[0].message.content or ""


def action_from_dict(raw: dict[str, Any]) -> Action:
    loc = raw.get("location")
    location = None
    if loc:
        try:
            location = Location(str(loc).lower())
        except ValueError:
            location = None
    kind = str(raw.get("type") or raw.get("action") or "pass").lower()
    try:
        action_type = ActionType(kind)
    except ValueError:
        action_type = ActionType.PASS
    return Action(
        type=action_type,
        thought=str(raw.get("thought") or ""),
        target=raw.get("target"),
        content=raw.get("content") or raw.get("line") or raw.get("speech"),
        location=location,
        challenge_effort=raw.get("challenge_effort"),
    )


class LLMClient:
    def __init__(self, settings: Settings, profiles: dict[str, Any] | None = None):
        self.settings = settings
        self.profiles = profiles or {}
        self.limiter = RateLimiter(settings.rpm)

    def complete_json(
        self,
        name: str,
        system: str,
        user: str,
        *,
        fallback: dict[str, Any] | None = None,
    ) -> tuple[dict[str, Any], str, str]:
        profile = self.profiles.get(name)
        model = islander_model(self.settings, profile) if profile else self.settings.default_model
        if self.settings.stub:
            raw = fallback or self.stub_decision(name, user)
            return raw, json.dumps(raw), "stub"
        try:
            from .recap import console
        except Exception:
            console = None

        last_error: Exception | None = None
        for attempt in range(1, self.settings.max_retries + 1):
            if console:
                extra = f" retry {attempt}" if attempt > 1 else ""
                console.print(
                    f"  [dim]{name} thinking ({model}){extra}…[/dim]",
                    highlight=False,
                )
            else:
                print(f"  {name} thinking ({model})...", flush=True)
            self.limiter.wait()
            try:
                if model.startswith("gemini/") or model.startswith("gemini-"):
                    text = _gemini_complete(
                        model,
                        system,
                        user,
                        temperature=self.settings.temperature,
                        max_tokens=self.settings.max_tokens,
                        api_key=_api_key_for_model(
                            model if model.startswith("gemini/") else f"gemini/{model}"
                        ),
                    )
                else:
                    text = _litellm_complete(
                        model,
                        system,
                        user,
                        temperature=self.settings.temperature,
                        max_tokens=self.settings.max_tokens,
                    )
                return parse_json_object(text), text, model
            except GeminiRateLimitError as exc:
                last_error = exc
                wait_for = max(exc.retry_after, 60.0)
                msg = f"  rate limit hit — waiting {wait_for:.0f}s (free tier is 15 requests/min)"
                if console:
                    console.print(f"[yellow]{msg}[/yellow]")
                else:
                    print(msg, file=sys.stderr, flush=True)
                time.sleep(wait_for)
            except Exception as exc:
                last_error = exc
                print(f"[li_sim] LLM call failed for {name}: {exc}", file=sys.stderr)
                break

        if self.settings.stub_on_error:
            print(f"[li_sim] falling back to stub for {name}", file=sys.stderr)
            payload = fallback or self.stub_decision(name, user)
            return payload, json.dumps(payload), "stub-fallback"
        raise RuntimeError(f"LLM call failed for {name} after retries: {last_error}")

    def decide_action(self, name: str, system: str, user: str) -> tuple[Action, dict[str, Any], str, str]:
        raw, text, model = self.complete_json(name, system, user)
        try:
            return action_from_dict(raw), raw, text, model
        except Exception:
            action = Action(type=ActionType.PASS, thought="Couldn't lock in a move.")
            return action, raw, text, model

    def stub_decision(self, name: str, user: str) -> dict[str, Any]:
        others = _active_others(name, user)
        rng = seeded_rng(self.settings.seed, "stub", name, user[:280])
        chaos = 0.4
        loyalty = 0.5

        if "public vote dump" in user.lower() or "you are safe" in user.lower():
            pool = _must_targets(user) or others
            target = pool[0] if pool else name
            return {
                "type": "save",
                "thought": f"Saving {target} is the least messy play for the public.",
                "target": target,
                "content": f"I'm saving {target}.",
            }
            target = others[0] if others else name
            return {
                "type": "save",
                "thought": f"Saving {target} looks decent and keeps my options open.",
                "target": target,
                "content": f"I'm saving {target}.",
            }
        if "recoupling is mandatory" in user.lower() or "available partners" in user.lower():
            available = _available_partners(user)
            pool = available or others
            target = _preferred_target(name, pool, rng)
            return {
                "type": "couple",
                "thought": f"I have to lock someone. {target} is the strongest play for the money.",
                "target": target,
                "content": f"{name} chooses {target}.",
            }
        if "Set challenge_effort" in user or "challenge_effort" in user:
            effort = 8 if loyalty > 0.6 else rng.randint(5, 10)
            return {
                "type": "challenge",
                "thought": "Don't come last. The public hates last.",
                "content": f"{name} goes all in.",
                "challenge_effort": effort,
            }
        if "same-gender huddle" in user.lower() or "boys talk" in user.lower() or "girls talk" in user.lower():
            pool = _must_targets(user) or others
            target = pool[0] if pool else name
            return {
                "type": "speak",
                "thought": _stub_thought(name, target, chaos, loyalty),
                "target": target,
                "content": _stub_huddle_line(name, target, label_guess(user), rng),
            }
        if "SCENE REPLY" in user:
            scene_target = _scene_partner(name, user)
            target = scene_target or (others[0] if others else "them")
            return {
                "type": "speak",
                "thought": _stub_thought(name, target, chaos, loyalty),
                "target": target,
                "content": _stub_line(name, target, rng, chaos),
            }

        roll = rng.random()
        target = _preferred_target(name, others, rng) if others else None
        if roll < 0.12:
            return {
                "type": "diary",
                "thought": _stub_thought(name, target or "the villa", chaos, loyalty),
                "content": _stub_diary(name, target, chaos, loyalty),
            }
        if roll < 0.22 or not target:
            loc = rng.choice(["pool", "terrace", "lounge", "bedroom"])
            return {
                "type": "move",
                "thought": f"Need a different energy. {loc}.",
                "location": loc,
                "content": f"Heading to the {loc}.",
            }
        if chaos > 0.6 and roll < 0.55:
            return {
                "type": "whisper",
                "thought": _stub_thought(name, target, chaos, loyalty),
                "target": target,
                "content": _stub_whisper(name, target, rng),
            }
        return {
            "type": "speak",
            "thought": _stub_thought(name, target, chaos, loyalty),
            "target": target,
            "content": _stub_line(name, target, rng, chaos),
        }


_HANDLE_RE = re.compile(r"([\w.-]+-agent\d+)")


def _active_others(name: str, user: str) -> list[str]:
    marker = "Other islanders:"
    if marker in user:
        tail = user.split(marker, 1)[1].split("\n", 1)[0]
        found = [part.strip() for part in tail.split(",") if part.strip() and part.strip() != name]
        if found:
            return found
    dumped: set[str] = set()
    if "Dumped:" in user:
        dumped_line = user.split("Dumped:", 1)[1].split("\n", 1)[0]
        dumped = {
            part.strip()
            for part in dumped_line.split(",")
            if part.strip() and part.strip() != "nobody"
        }
    return [h for h in _HANDLE_RE.findall(user) if h != name and h not in dumped]


def _scene_partner(name: str, user: str) -> str | None:
    match = re.search(r"target=([\w.-]+-agent\d+)", user)
    if match and match.group(1) != name:
        return match.group(1)
    match = re.search(r"([\w.-]+-agent\d+) just said:", user)
    if match and match.group(1) != name:
        return match.group(1)
    match = re.search(r"Hideaway date with ([\w.-]+-agent\d+)", user)
    if match:
        return match.group(1)
    return None


def _available_partners(user: str) -> list[str]:
    if "AVAILABLE PARTNERS" not in user:
        return []
    line = user.split("AVAILABLE PARTNERS", 1)[1]
    line = line.split("\n", 1)[0]
    line = line.split(":", 1)[-1]
    return [part.strip() for part in line.split(",") if part.strip()]


def _must_targets(user: str) -> list[str]:
    if "MUST be one of:" not in user:
        return []
    tail = user.split("MUST be one of:", 1)[1].split("\n", 1)[0]
    return [part.strip().rstrip(".") for part in tail.split(",") if part.strip()]


def label_guess(user: str) -> str:
    if "BOYS TALK" in user or "boys talk" in user.lower():
        return "boys"
    return "girls"


def _stub_huddle_line(name: str, target: str, label: str, rng: random.Random) -> str:
    options = [
        f"Be honest, {target} — whose couple actually looks solid and who's hanging by a thread?",
        f"{target}, if recoupling was tonight I know who I'd save. Do you?",
        f"Keep this in the {label} — I don't trust what the other lot are spinning.",
        f"{target}, we need a plan for the fifty grand. Who's actually in it to win it?",
    ]
    return rng.choice(options)


def _preferred_target(name: str, others: list[str], rng: random.Random) -> str:
    return rng.choice(others) if others else name


def _stub_thought(name: str, target: str, chaos: float, loyalty: float) -> str:
    if chaos > 0.7:
        return f"If I light a fire under {target}, I stay centre of the episode."
    if loyalty > 0.7:
        return f"I need {target} to feel chosen. No games."
    return f"What's {target} actually after? Don't get played."


def _stub_line(name: str, target: str, rng: random.Random, chaos: float) -> str:
    if chaos > 0.7:
        options = [
            f"Be honest with me, {target} — is this grafting or is this a storyline?",
            f"{target}, people are talking. I thought you should hear it from me.",
            f"Don't look at me like that, {target}. You started it.",
        ]
    else:
        options = [
            f"{target}, can we actually talk? Not the group version — the real one.",
            f"I've been thinking about you all morning, {target}. That's embarrassing but it's true.",
            f"Where's your head at with us, {target}? I don't want to assume.",
            f"You good? You went quiet after last night and I noticed.",
        ]
    return rng.choice(options)


def _stub_whisper(name: str, target: str, rng: random.Random) -> str:
    options = [
        f"Don't react — but I don't trust what {target} is doing.",
        f"If recoupling happened tonight, would you still pick me?",
        f"Keep this between us. Someone's being two-faced and I think you already know who.",
        f"I'm not trying to stir, {target}, but you should clock how they look at you.",
    ]
    return rng.choice(options)


def _stub_diary(name: str, target: str | None, chaos: float, loyalty: float) -> str:
    who = target or "this lot"
    if chaos > 0.7:
        return f"I'm not here to be a background extra. {who} can keep up or get left."
    if loyalty > 0.7:
        return f"I came here for something real. If {who} isn't that, I need to know sooner not later."
    return f"Winning means being liked and being coupled. I'm tracking both. {who} is part of that maths."
