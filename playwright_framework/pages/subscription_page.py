"""Playwright subscription page object."""

from __future__ import annotations

import allure

from playwright_framework.pages.base_page import BasePage


class SubscriptionSelectors:
    BASIC_PLAN = "[data-testid='plan-basic']"
    STANDARD_PLAN = "[data-testid='plan-standard']"
    PREMIUM_PLAN = "[data-testid='plan-premium']"
    CONFIRM_PLAN = "[data-testid='confirm-plan']"
    SUCCESS_TOAST = "[data-testid='subscription-success']"


class SubscriptionPage(BasePage):
    PLAN_SELECTORS = {
        "basic": SubscriptionSelectors.BASIC_PLAN,
        "standard": SubscriptionSelectors.STANDARD_PLAN,
        "premium": SubscriptionSelectors.PREMIUM_PLAN,
    }

    @allure.step("Navigate to subscription page")
    def load(self) -> None:
        self.open("/account/subscription")

    @allure.step("Select subscription plan: {plan}")
    def select_plan(self, plan: str) -> None:
        self.click(self.PLAN_SELECTORS[plan.lower()])

    def confirm_plan(self) -> None:
        self.click(SubscriptionSelectors.CONFIRM_PLAN)

    def change_plan(self, plan: str) -> None:
        self.select_plan(plan)
        self.confirm_plan()

    def success_message(self) -> str:
        return self.text_of(SubscriptionSelectors.SUCCESS_TOAST)
