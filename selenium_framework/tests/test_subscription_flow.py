"""Selenium subscription module tests."""

from __future__ import annotations

import allure
import pytest

from selenium_framework.pages.subscription_page import SubscriptionPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.subscription
@pytest.mark.regression
@allure.feature("Subscription")
@allure.story("Plan upgrade and downgrade")
@pytest.mark.parametrize("plan", ["premium", "standard"])
def test_subscription_plan_change(selenium_driver, base_url, plan):
    subscription_page = SubscriptionPage(selenium_driver, base_url)
    subscription_page.load()
    subscription_page.change_plan(plan)

    assert "updated" in subscription_page.success_message().lower()
