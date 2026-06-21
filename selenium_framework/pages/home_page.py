"""Home page object for OTT landing content and carousel checks."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage


class HomeLocators:
    TRENDING_SECTION = (By.CSS_SELECTOR, "[data-testid='trending-row']")
    TRENDING_CARDS = (By.CSS_SELECTOR, "[data-testid='trending-card']")
    CATEGORY_ROWS = (By.CSS_SELECTOR, "[data-testid='category-row']")
    BANNER_SLIDER = (By.CSS_SELECTOR, "[data-testid='hero-banner']")
    NEXT_BANNER = (By.CSS_SELECTOR, "[data-testid='banner-next']")


class HomePage(BasePage):
    @allure.step("Navigate to home page")
    def load(self) -> None:
        self.open("/home")

    @allure.step("Check trending movies")
    def trending_movies_count(self) -> int:
        return len(self.wait.all_visible(HomeLocators.TRENDING_CARDS))

    @allure.step("Check category rows")
    def category_count(self) -> int:
        return len(self.wait.all_visible(HomeLocators.CATEGORY_ROWS))

    @allure.step("Move banner slider")
    def move_banner_slider(self) -> None:
        self.click(HomeLocators.NEXT_BANNER)

    def is_banner_visible(self) -> bool:
        return self.is_visible(HomeLocators.BANNER_SLIDER)
