"""Selenium search module tests."""

from __future__ import annotations

import allure
import pytest

from selenium_framework.pages.search_page import SearchPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.search
@pytest.mark.smoke
@allure.feature("Search")
@allure.story("Search returns matching movie")
def test_search_movie_returns_result(selenium_driver, base_url, test_movies):
    search_page = SearchPage(selenium_driver, base_url)
    search_page.load()
    search_page.search_movie(test_movies["expected_movie"]["title"])

    assert any(test_movies["expected_movie"]["title"] in title for title in search_page.results())


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.search
@pytest.mark.regression
@allure.feature("Search")
@allure.story("Autocomplete suggestions")
@pytest.mark.parametrize("search_term", ["Stranger", "The", "Wed"])
def test_search_autocomplete_suggestions(selenium_driver, base_url, search_term):
    search_page = SearchPage(selenium_driver, base_url)
    search_page.load()
    search_page.search_movie(search_term)

    assert len(search_page.suggestions()) > 0


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.search
@pytest.mark.regression
@allure.feature("Search")
@allure.story("No result handling")
def test_search_no_results_message(selenium_driver, base_url, test_movies):
    search_page = SearchPage(selenium_driver, base_url)
    search_page.load()
    search_page.search_movie(test_movies["no_result_query"])

    assert "No results" in search_page.no_results_message()
