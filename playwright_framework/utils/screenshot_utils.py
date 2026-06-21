"""Playwright screenshot helpers for Allure reports."""

from __future__ import annotations

from pathlib import Path

import allure
from playwright.sync_api import Page


REPORT_DIR = Path(__file__).resolve().parents[2] / "reports" / "screenshots"


def attach_playwright_screenshot(page: Page, name: str) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    file_path = REPORT_DIR / f"playwright_{name}.png"
    page.screenshot(path=str(file_path), full_page=True)
    allure.attach.file(str(file_path), name=f"Playwright failure: {name}", attachment_type=allure.attachment_type.PNG)
    return file_path
