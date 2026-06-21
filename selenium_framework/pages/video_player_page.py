"""Video player page object for playback controls."""

from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage


class VideoPlayerLocators:
    PLAYER = (By.CSS_SELECTOR, "[data-testid='video-player']")
    PLAY_PAUSE = (By.CSS_SELECTOR, "[data-testid='play-pause']")
    SEEK_FORWARD = (By.CSS_SELECTOR, "[data-testid='seek-forward']")
    SEEK_BACKWARD = (By.CSS_SELECTOR, "[data-testid='seek-backward']")
    SUBTITLE_TOGGLE = (By.CSS_SELECTOR, "[data-testid='subtitle-toggle']")
    QUALITY_MENU = (By.CSS_SELECTOR, "[data-testid='quality-menu']")
    QUALITY_1080 = (By.CSS_SELECTOR, "[data-testid='quality-1080p']")


class VideoPlayerPage(BasePage):
    @allure.step("Open movie player: {movie_id}")
    def load(self, movie_id: str = "stranger-things") -> None:
        self.open(f"/watch/{movie_id}")

    @allure.step("Toggle play/pause")
    def toggle_play_pause(self) -> None:
        self.click(VideoPlayerLocators.PLAY_PAUSE)

    @allure.step("Seek forward")
    def seek_forward(self) -> None:
        self.click(VideoPlayerLocators.SEEK_FORWARD)

    @allure.step("Seek backward")
    def seek_backward(self) -> None:
        self.click(VideoPlayerLocators.SEEK_BACKWARD)

    @allure.step("Toggle subtitles")
    def toggle_subtitles(self) -> None:
        self.click(VideoPlayerLocators.SUBTITLE_TOGGLE)

    @allure.step("Change quality to 1080p")
    def change_quality_to_1080p(self) -> None:
        self.click(VideoPlayerLocators.QUALITY_MENU)
        self.click(VideoPlayerLocators.QUALITY_1080)

    def is_player_visible(self) -> bool:
        return self.is_visible(VideoPlayerLocators.PLAYER)
