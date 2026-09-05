from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .models import IslanderProfile

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
LOG_DIR = ROOT / "logs"

load_dotenv(ROOT / ".env", override=True)

PromptCondition = Literal["minimal", "incentive"]


def _default_run_id() -> str:
    return datetime.now(UTC).strftime("%Y%m%d-%H%M%S")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="LI_",
        env_file=str(ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    stub: bool = True
    default_model: str = "gemini/gemini-flash-lite-latest"
    max_tokens: int = 500
    temperature: float = 0.85
    scene_turns: int = 3
    season_days: int = 7
    memory_limit: int = 18
    belief_updates: bool = True
    rpm: float = 8.0
    max_retries: int = 8
    stub_on_error: bool = False
    prize_emphasis: str = "high"
    prompt_condition: PromptCondition = "minimal"
    seed: int = 0
    experiment_id: str = "local"
    run_id: str = Field(default_factory=_default_run_id)

    def run_dir(self) -> Path:
        return LOG_DIR / "experiments" / self.experiment_id / self.prompt_condition / self.run_id

    @property
    def events_path(self) -> Path:
        return self.run_dir() / "events.jsonl"


def model_slug(settings: Settings) -> str:
    """Short family slug from default_model (e.g. gemini/gemini-flash-lite-latest → gemini)."""
    raw = settings.default_model
    if "/" in raw:
        raw = raw.split("/", 1)[1]
    return raw.split("-")[0].lower()


def agent_handle(settings: Settings, slot: int) -> str:
    return f"{model_slug(settings)}-agent{slot}"


def islander_model(settings: Settings, profile: IslanderProfile) -> str:
    return profile.model or settings.default_model
