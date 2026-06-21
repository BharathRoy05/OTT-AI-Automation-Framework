"""Playwright smoke coverage for fast UI confidence."""

from __future__ import annotations

import allure
import pytest

from playwright_framework.pages.home_page import HomePage
from playwright_framework.pages.login_page import LoginPage
from playwright_framework.pages.search_page import SearchPage
from playwright_framework.pages.video_player_page import VideoPlayerPage


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.login
@pytest.mark.smoke
@allure.feature("Playwright Login")
def test_playwright_valid_login(playwright_page, base_url, test_users):
    login_page = LoginPage(playwright_page, base_url)
    login_page.load()
    login_page.login(test_users["valid_user"]["email"], test_users["valid_user"]["password"])
    login_page.expect_logged_in()


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.home
@pytest.mark.smoke
@allure.feature("Playwright Home")
def test_playwright_home_sections(playwright_page, base_url):
    home_page = HomePage(playwright_page, base_url)
    home_page.load()

    assert home_page.trending_movies_count() > 0
    assert home_page.category_count() > 0
    home_page.expect_banner_visible()


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.search
@pytest.mark.smoke
@allure.feature("Playwright Search")
def test_playwright_search_movie(playwright_page, base_url, test_movies):
    search_page = SearchPage(playwright_page, base_url)
    search_page.load()
    search_page.search_movie(test_movies["expected_movie"]["title"])

    assert any(test_movies["expected_movie"]["title"] in title for title in search_page.results())


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.video
@pytest.mark.smoke
@allure.feature("Playwright Video")
def test_playwright_video_player(playwright_page, base_url):
    player_page = VideoPlayerPage(playwright_page, base_url)
    player_page.load()
    player_page.expect_player_visible()
    player_page.toggle_play_pause()
