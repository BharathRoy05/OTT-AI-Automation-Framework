"""Playwright login page object."""

from __future__ import annotations

import allure

from playwright_framework.pages.base_page import BasePage


class LoginSelectors:
    EMAIL = "[data-testid='login-email']"
    PASSWORD = "[data-testid='login-password']"
    SUBMIT = "[data-testid='login-submit']"
    ERROR_MESSAGE = "[data-testid='login-error']"
    PROFILE_AVATAR = "[data-testid='profile-avatar']"


class LoginPage(BasePage):
    @allure.step("Navigate to login page")
    def load(self) -> None:
        self.open("/login")

    @allure.step("Login with email: {email}")
    def login(self, email: str, password: str) -> None:
        self.type_text(LoginSelectors.EMAIL, email)
        self.type_text(LoginSelectors.PASSWORD, password)
        self.click(LoginSelectors.SUBMIT)

    def error_message(self) -> str:
        return self.text_of(LoginSelectors.ERROR_MESSAGE)

    def expect_logged_in(self) -> None:
        self.expect_visible(LoginSelectors.PROFILE_AVATAR)
