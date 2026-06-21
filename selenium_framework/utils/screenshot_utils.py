"""Screenshot helpers that attach artifacts to Allure reports."""

from __future__ import annotations

from pathlib import Path

import allure
from selenium.webdriver.remote.webdriver import WebDriver


REPORT_DIR = Path(__file__).resolve().parents[2] / "reports" / "screenshots"


def attach_selenium_screenshot(driver: WebDriver, name: str) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    file_path = REPORT_DIR / f"selenium_{name}.png"
    driver.save_screenshot(str(file_path))
    allure.attach.file(str(file_path), name=f"Selenium failure: {name}", attachment_type=allure.attachment_type.PNG)
    return file_path
