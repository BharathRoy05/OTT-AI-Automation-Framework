"""Login page object with separated locators and actions."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage


class LoginLocators:
    EMAIL = (By.CSS_SELECTOR, "[data-testid='login-email']")
    PASSWORD = (By.CSS_SELECTOR, "[data-testid='login-password']")
    SUBMIT = (By.CSS_SELECTOR, "[data-testid='login-submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-testid='login-error']")
    PROFILE_AVATAR = (By.CSS_SELECTOR, "[data-testid='profile-avatar']")


class LoginPage(BasePage):
    @allure.step("Navigate to login page")
    def load(self) -> None:
        self.open("/login")

    @allure.step("Login with email: {email}")
    def login(self, email: str, password: str) -> None:
        self.type_text(LoginLocators.EMAIL, email)
        self.type_text(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.SUBMIT)

    @allure.step("Read login error")
    def error_message(self) -> str:
        return self.text_of(LoginLocators.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        return self.is_visible(LoginLocators.PROFILE_AVATAR)
