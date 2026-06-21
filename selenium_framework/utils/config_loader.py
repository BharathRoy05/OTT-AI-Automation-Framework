"""Configuration loader for local, CI, and environment-driven runs."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class AppConfig:
    base_url: str = os.getenv("BASE_URL", "https://ott-demo.example.com")
    browser: str = os.getenv("BROWSER", "chromium")
    default_timeout: int = int(os.getenv("DEFAULT_TIMEOUT", "15"))


def get_config() -> AppConfig:
    return AppConfig()
