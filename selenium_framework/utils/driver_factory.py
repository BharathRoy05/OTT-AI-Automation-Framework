"""Selenium WebDriver factory for local and CI browser sessions."""

from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class SeleniumDriverFactory:
    @staticmethod
    def create_driver(browser: str = "chromium", headed: bool = False) -> webdriver.Remote:
        browser_name = browser.lower()

        if browser_name in {"chrome", "chromium"}:
            options = ChromeOptions()
            if not headed:
                options.add_argument("--headless=new")
            options.add_argument("--window-size=1440,1000")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if not headed:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif browser_name == "edge":
            options = EdgeOptions()
            if not headed:
                options.add_argument("--headless=new")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(f"Unsupported Selenium browser: {browser}")

        driver.implicitly_wait(2)
        return driver
