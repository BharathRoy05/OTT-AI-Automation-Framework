"""Selenium video player module tests."""

from __future__ import annotations

import allure
import pytest

from selenium_framework.pages.video_player_page import VideoPlayerPage


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.video
@pytest.mark.smoke
@allure.feature("Video Player")
@allure.story("Playback controls")
def test_video_play_pause_and_seek(selenium_driver, base_url):
    player_page = VideoPlayerPage(selenium_driver, base_url)
    player_page.load()

    assert player_page.is_player_visible()
    player_page.toggle_play_pause()
    player_page.seek_forward()
    player_page.seek_backward()
    player_page.toggle_play_pause()


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.video
@pytest.mark.regression
@allure.feature("Video Player")
@allure.story("Subtitle and quality controls")
def test_video_subtitle_and_quality_controls(selenium_driver, base_url):
    player_page = VideoPlayerPage(selenium_driver, base_url)
    player_page.load()

    player_page.toggle_subtitles()
    player_page.change_quality_to_1080p()
    assert player_page.is_player_visible()
