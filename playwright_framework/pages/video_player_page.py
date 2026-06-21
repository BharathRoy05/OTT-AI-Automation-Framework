"""Playwright video player page object."""

from __future__ import annotations

import allure

from playwright_framework.pages.base_page import BasePage


class VideoPlayerSelectors:
    PLAYER = "[data-testid='video-player']"
    PLAY_PAUSE = "[data-testid='play-pause']"
    SEEK_FORWARD = "[data-testid='seek-forward']"
    SEEK_BACKWARD = "[data-testid='seek-backward']"
    SUBTITLE_TOGGLE = "[data-testid='subtitle-toggle']"
    QUALITY_MENU = "[data-testid='quality-menu']"
    QUALITY_1080 = "[data-testid='quality-1080p']"


class VideoPlayerPage(BasePage):
    @allure.step("Open movie player: {movie_id}")
    def load(self, movie_id: str = "stranger-things") -> None:
        self.open(f"/watch/{movie_id}")

    def toggle_play_pause(self) -> None:
        self.click(VideoPlayerSelectors.PLAY_PAUSE)

    def seek_forward(self) -> None:
        self.click(VideoPlayerSelectors.SEEK_FORWARD)

    def seek_backward(self) -> None:
        self.click(VideoPlayerSelectors.SEEK_BACKWARD)

    def toggle_subtitles(self) -> None:
        self.click(VideoPlayerSelectors.SUBTITLE_TOGGLE)

    def change_quality_to_1080p(self) -> None:
        self.click(VideoPlayerSelectors.QUALITY_MENU)
        self.click(VideoPlayerSelectors.QUALITY_1080)

    def expect_player_visible(self) -> None:
        self.expect_visible(VideoPlayerSelectors.PLAYER)
