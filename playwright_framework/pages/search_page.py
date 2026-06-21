"""Playwright search page object."""

from __future__ import annotations

import allure

from playwright_framework.pages.base_page import BasePage


class SearchSelectors:
    SEARCH_INPUT = "[data-testid='search-input']"
    AUTOCOMPLETE_ITEMS = "[data-testid='autocomplete-item']"
    RESULT_CARDS = "[data-testid='search-result-card']"
    NO_RESULTS = "[data-testid='no-results']"


class SearchPage(BasePage):
    @allure.step("Navigate to search page")
    def load(self) -> None:
        self.open("/search")

    @allure.step("Search movie: {title}")
    def search_movie(self, title: str) -> None:
        self.type_text(SearchSelectors.SEARCH_INPUT, title)

    def suggestions(self) -> list[str]:
        return self.page.locator(SearchSelectors.AUTOCOMPLETE_ITEMS).all_inner_texts()

    def results(self) -> list[str]:
        return self.page.locator(SearchSelectors.RESULT_CARDS).all_inner_texts()

    def no_results_message(self) -> str:
        return self.text_of(SearchSelectors.NO_RESULTS)
