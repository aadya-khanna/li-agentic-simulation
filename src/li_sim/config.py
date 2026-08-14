from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
LOG_DIR = ROOT / "logs"

load_dotenv(ROOT / ".env", override=True)


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
    rpm: float = 8.0
    max_retries: int = 8
    stub_on_error: bool = False

    model_maya: str | None = None
    model_luca: str | None = None
    model_zara: str | None = None
    model_theo: str | None = None
    model_nia: str | None = None
    model_kai: str | None = None

    log_path: Path = Field(default_factory=lambda: LOG_DIR / "run.jsonl")


def islander_model(settings: Settings, name: str) -> str:
    attr = f"model_{name.lower()}"
    override = getattr(settings, attr, None)
    return override or settings.default_model
