"""Base Playwright page with shared actions."""

from __future__ import annotations

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    @allure.step("Open path: {path}")
    def open(self, path: str = "") -> None:
        self.page.goto(f"{self.base_url}{path}", wait_until="networkidle")

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def type_text(self, selector: str, value: str) -> None:
        self.page.locator(selector).fill(value)

    def text_of(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def expect_visible(self, selector: str) -> None:
        expect(self.page.locator(selector)).to_be_visible()
