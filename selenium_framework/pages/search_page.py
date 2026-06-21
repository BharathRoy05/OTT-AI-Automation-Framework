"""Search page object for movie lookup and suggestions."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage


class SearchLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "[data-testid='search-input']")
    AUTOCOMPLETE_ITEMS = (By.CSS_SELECTOR, "[data-testid='autocomplete-item']")
    RESULT_CARDS = (By.CSS_SELECTOR, "[data-testid='search-result-card']")
    NO_RESULTS = (By.CSS_SELECTOR, "[data-testid='no-results']")


class SearchPage(BasePage):
    @allure.step("Navigate to search page")
    def load(self) -> None:
        self.open("/search")

    @allure.step("Search movie: {title}")
    def search_movie(self, title: str) -> None:
        self.type_text(SearchLocators.SEARCH_INPUT, title)

    @allure.step("Read autocomplete suggestions")
    def suggestions(self) -> list[str]:
        return [item.text for item in self.wait.all_visible(SearchLocators.AUTOCOMPLETE_ITEMS)]

    @allure.step("Read search results")
    def results(self) -> list[str]:
        return [item.text for item in self.wait.all_visible(SearchLocators.RESULT_CARDS)]

    def no_results_message(self) -> str:
        return self.text_of(SearchLocators.NO_RESULTS)
