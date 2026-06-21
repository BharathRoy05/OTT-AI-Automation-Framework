"""Subscription page object for plan changes."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage


class SubscriptionLocators:
    BASIC_PLAN = (By.CSS_SELECTOR, "[data-testid='plan-basic']")
    STANDARD_PLAN = (By.CSS_SELECTOR, "[data-testid='plan-standard']")
    PREMIUM_PLAN = (By.CSS_SELECTOR, "[data-testid='plan-premium']")
    CONFIRM_PLAN = (By.CSS_SELECTOR, "[data-testid='confirm-plan']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, "[data-testid='subscription-success']")


class SubscriptionPage(BasePage):
    PLAN_LOCATORS = {
        "basic": SubscriptionLocators.BASIC_PLAN,
        "standard": SubscriptionLocators.STANDARD_PLAN,
        "premium": SubscriptionLocators.PREMIUM_PLAN,
    }

    @allure.step("Navigate to subscription page")
    def load(self) -> None:
        self.open("/account/subscription")

    @allure.step("Select subscription plan: {plan}")
    def select_plan(self, plan: str) -> None:
        self.click(self.PLAN_LOCATORS[plan.lower()])

    @allure.step("Confirm subscription plan")
    def confirm_plan(self) -> None:
        self.click(SubscriptionLocators.CONFIRM_PLAN)

    @allure.step("Change subscription plan to: {plan}")
    def change_plan(self, plan: str) -> None:
        self.select_plan(plan)
        self.confirm_plan()

    def success_message(self) -> str:
        return self.text_of(SubscriptionLocators.SUCCESS_TOAST)
