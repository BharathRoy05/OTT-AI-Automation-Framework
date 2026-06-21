"""Rule-based MVP for selecting automation tests from story text.

The class is intentionally transparent: QA engineers can tune keywords and mapped
test files without needing a model service. It can later be swapped for an LLM or
embedding-based classifier while preserving the public API.
"""

from __future__ import annotations

from dataclasses import dataclass

import pytest


pytestmark = pytest.mark.ai


@dataclass(frozen=True)
class SelectionRule:
    keywords: tuple[str, ...]
    test_files: tuple[str, ...]


class TestSelector:
    DEFAULT_RULES: tuple[SelectionRule, ...] = (
        SelectionRule(("login", "signin", "sign in", "authentication", "password"), ("selenium_framework/tests/test_login_valid.py",)),
        SelectionRule(("home", "landing", "dashboard", "trending", "category", "banner"), ("selenium_framework/tests/test_home_load.py",)),
        SelectionRule(("search", "autocomplete", "suggestion", "no result", "movie title"), ("selenium_framework/tests/test_search_movie.py",)),
        SelectionRule(("video", "player", "playback", "pause", "subtitle", "quality", "seek"), ("selenium_framework/tests/test_video_playback.py",)),
        SelectionRule(("payment", "subscription", "plan", "upgrade", "downgrade", "billing"), ("selenium_framework/tests/test_subscription_flow.py",)),
    )

    def __init__(self, rules: tuple[SelectionRule, ...] | None = None) -> None:
        self.rules = rules or self.DEFAULT_RULES

    def select_tests(self, story_text: str) -> list[str]:
        normalized_story = story_text.lower()
        selected: list[str] = []

        for rule in self.rules:
            if any(keyword in normalized_story for keyword in rule.keywords):
                selected.extend(rule.test_files)

        if not selected:
            return ["selenium_framework/tests"]

        return sorted(set(selected))


def select_tests_for_story(story_text: str) -> list[str]:
    return TestSelector().select_tests(story_text)


def test_selector_maps_login_story_to_login_tests() -> None:
    selected = select_tests_for_story("As a user, I want login validation for incorrect passwords.")
    assert "selenium_framework/tests/test_login_valid.py" in selected


def test_selector_maps_video_story_to_player_tests() -> None:
    selected = select_tests_for_story("Improve video player quality controls and subtitle toggle.")
    assert "selenium_framework/tests/test_video_playback.py" in selected
