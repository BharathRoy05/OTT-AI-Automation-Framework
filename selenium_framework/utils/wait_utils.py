"""Explicit wait helpers for stable Selenium tests."""

from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WaitUtils:
    def __init__(self, driver: WebDriver, timeout: int = 15) -> None:
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def all_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def url_contains(self, text: str) -> bool:
        return self.wait.until(EC.url_contains(text))
