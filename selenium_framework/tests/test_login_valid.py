"""Selenium login module tests."""

from __future__ import annotations

import allure
import pytest

from selenium_framework.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.login
@pytest.mark.smoke
@allure.feature("Login")
@allure.story("Valid login")
def test_valid_login(selenium_driver, base_url, test_users):
    login_page = LoginPage(selenium_driver, base_url)
    login_page.load()
    login_page.login(test_users["valid_user"]["email"], test_users["valid_user"]["password"])
    assert login_page.is_logged_in()


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.login
@pytest.mark.regression
@allure.feature("Login")
@allure.story("Invalid and empty login validation")
@pytest.mark.parametrize(
    ("user_key", "expected_message"),
    [
        ("invalid_user", "Invalid email or password"),
        ("empty_user", "Email and password are required"),
    ],
)
def test_login_validation_messages(selenium_driver, base_url, test_users, user_key, expected_message):
    login_page = LoginPage(selenium_driver, base_url)
    login_page.load()
    login_page.login(test_users[user_key]["email"], test_users[user_key]["password"])
    assert expected_message in login_page.error_message()
