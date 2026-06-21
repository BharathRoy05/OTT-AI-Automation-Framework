"""Playwright browser factory for fast cross-browser UI tests."""

from __future__ import annotations

from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright


class PlaywrightDriverFactory:
    def __init__(self, browser_name: str = "chromium", headed: bool = False) -> None:
        self.browser_name = browser_name
        self.headed = headed
        self.playwright: Playwright | None = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None

    def start(self) -> Page:
        self.playwright = sync_playwright().start()
        browser_launcher = getattr(self.playwright, self.browser_name)
        self.browser = browser_launcher.launch(headless=not self.headed)
        self.context = self.browser.new_context(viewport={"width": 1440, "height": 1000})
        return self.context.new_page()

    def stop(self) -> None:
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
