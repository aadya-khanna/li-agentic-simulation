from __future__ import annotations

from .config import Settings
from .rng import seeded_rng


def pick_from_pool(settings: Settings, *parts: str | int, pool: list[str]) -> str:
    if not pool:
        raise ValueError("fallback pool is empty")
    rng = seeded_rng(settings.seed, "fallback", *parts)
    return rng.choice(pool)


def retry_prompt_suffix(notes: list[str]) -> str:
    lines = "\n".join(f"- {note}" for note in notes)
    return f"\n\nVALIDATION FIX REQUIRED:\n{lines}\nReply with corrected JSON."
