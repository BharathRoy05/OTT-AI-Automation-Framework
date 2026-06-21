"""Shared pytest fixtures for Selenium, Playwright, reporting, and test data."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Generator

import allure
import pytest

from selenium_framework.utils.driver_factory import SeleniumDriverFactory
from selenium_framework.utils.screenshot_utils import attach_selenium_screenshot
from playwright_framework.utils.driver_factory import PlaywrightDriverFactory
from playwright_framework.utils.screenshot_utils import attach_playwright_screenshot


ROOT_DIR = Path(__file__).parent
TEST_DATA_DIR = ROOT_DIR / "test_data"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default=os.getenv("BROWSER", "chromium"))
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL", "https://ott-demo.example.com"))
    parser.addoption("--headed", action="store_true", default=os.getenv("HEADED", "false").lower() == "true")
    parser.addoption("--run-ui", action="store_true", help="Run browser tests against the configured OTT app.")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if config.getoption("--run-ui"):
        return

    skip_ui = pytest.mark.skip(reason="UI tests require --run-ui and a reachable --base-url.")
    for item in items:
        if "ui" in item.keywords:
            item.add_marker(skip_ui)


@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config) -> str:
    return str(pytestconfig.getoption("--base-url")).rstrip("/")


@pytest.fixture(scope="session")
def test_users() -> dict[str, Any]:
    with (TEST_DATA_DIR / "users.json").open(encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def test_movies() -> dict[str, Any]:
    with (TEST_DATA_DIR / "movies.json").open(encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture()
def selenium_driver(pytestconfig: pytest.Config) -> Generator[Any, None, None]:
    driver = SeleniumDriverFactory.create_driver(
        browser=pytestconfig.getoption("--browser"),
        headed=pytestconfig.getoption("--headed"),
    )
    yield driver
    driver.quit()


@pytest.fixture()
def playwright_page(pytestconfig: pytest.Config) -> Generator[Any, None, None]:
    factory = PlaywrightDriverFactory(
        browser_name=pytestconfig.getoption("--browser"),
        headed=pytestconfig.getoption("--headed"),
    )
    page = factory.start()
    yield page
    factory.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[Any]) -> Generator[None, None, None]:
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    selenium_driver = item.funcargs.get("selenium_driver")
    playwright_page = item.funcargs.get("playwright_page")

    if selenium_driver:
        attach_selenium_screenshot(selenium_driver, item.name)
    if playwright_page:
        attach_playwright_screenshot(playwright_page, item.name)

    allure.dynamic.description("Failure artifacts were attached automatically by pytest hook.")
