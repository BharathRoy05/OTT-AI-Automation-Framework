"""Playwright home page object."""

from __future__ import annotations

import allure
from playwright.sync_api import expect

from playwright_framework.pages.base_page import BasePage


class HomeSelectors:
    TRENDING_CARDS = "[data-testid='trending-card']"
    CATEGORY_ROWS = "[data-testid='category-row']"
    BANNER_SLIDER = "[data-testid='hero-banner']"
    NEXT_BANNER = "[data-testid='banner-next']"


class HomePage(BasePage):
    @allure.step("Navigate to home page")
    def load(self) -> None:
        self.open("/home")

    def trending_movies_count(self) -> int:
        return self.page.locator(HomeSelectors.TRENDING_CARDS).count()

    def category_count(self) -> int:
        return self.page.locator(HomeSelectors.CATEGORY_ROWS).count()

    def move_banner_slider(self) -> None:
        self.click(HomeSelectors.NEXT_BANNER)

    def expect_banner_visible(self) -> None:
        expect(self.page.locator(HomeSelectors.BANNER_SLIDER)).to_be_visible()
