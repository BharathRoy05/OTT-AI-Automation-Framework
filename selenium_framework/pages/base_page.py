"""Base Selenium page with shared browser actions."""

from __future__ import annotations

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_framework.utils.wait_utils import WaitUtils


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str) -> None:
        self.driver = driver
        self.base_url = base_url
        self.wait = WaitUtils(driver)

    @allure.step("Open path: {path}")
    def open(self, path: str = "") -> None:
        self.driver.get(f"{self.base_url}{path}")

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.clickable(locator).click()

    def type_text(self, locator: tuple[str, str], value: str) -> None:
        element = self.wait.visible(locator)
        element.clear()
        element.send_keys(value)

    def text_of(self, locator: tuple[str, str]) -> str:
        return self.wait.visible(locator).text

    def is_visible(self, locator: tuple[str, str]) -> bool:
        return self.wait.visible(locator).is_displayed()
