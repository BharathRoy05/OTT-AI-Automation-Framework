"""Selenium home page module tests."""

from __future__ import annotations

import allure
import pytest

from selenium_framework.pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.home
@pytest.mark.smoke
@allure.feature("Home")
@allure.story("Home page content loads")
def test_home_page_loads_core_sections(selenium_driver, base_url):
    home_page = HomePage(selenium_driver, base_url)
    home_page.load()

    assert home_page.trending_movies_count() > 0
    assert home_page.category_count() > 0
    assert home_page.is_banner_visible()


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.home
@pytest.mark.regression
@allure.feature("Home")
@allure.story("Banner slider")
def test_banner_slider_can_advance(selenium_driver, base_url):
    home_page = HomePage(selenium_driver, base_url)
    home_page.load()
    home_page.move_banner_slider()

    assert home_page.is_banner_visible()
