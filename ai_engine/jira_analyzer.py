"""Jira story analyzer with mock and live API modes."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import pytest
import requests

from ai_engine.test_selector import TestSelector


pytestmark = pytest.mark.ai


MOCK_JIRA_STORIES: dict[str, str] = {
    "OTT-101": "Add login validations for invalid passwords and empty email fields.",
    "OTT-202": "Improve video playback controls, subtitle toggle, and quality selector.",
    "OTT-303": "Support subscription upgrade and downgrade plan flows for billing users.",
}


@dataclass
class JiraConfig:
    base_url: str = os.getenv("JIRA_BASE_URL", "")
    email: str = os.getenv("JIRA_EMAIL", "")
    api_token: str = os.getenv("JIRA_API_TOKEN", "")
    use_mock: bool = os.getenv("JIRA_USE_MOCK", "true").lower() == "true"


class JiraAnalyzer:
    def __init__(self, config: JiraConfig | None = None, selector: TestSelector | None = None) -> None:
        self.config = config or JiraConfig()
        self.selector = selector or TestSelector()

    def fetch_story_text(self, ticket_id: str) -> str:
        if self.config.use_mock:
            return MOCK_JIRA_STORIES.get(ticket_id, "")

        if not all([self.config.base_url, self.config.email, self.config.api_token]):
            raise ValueError("Jira live mode requires JIRA_BASE_URL, JIRA_EMAIL, and JIRA_API_TOKEN.")

        url = f"{self.config.base_url.rstrip('/')}/rest/api/3/issue/{ticket_id}"
        response = requests.get(
            url,
            auth=(self.config.email, self.config.api_token),
            headers={"Accept": "application/json"},
            timeout=20,
        )
        response.raise_for_status()
        payload: dict[str, Any] = response.json()
        fields = payload.get("fields", {})
        summary = fields.get("summary", "")
        description = fields.get("description", "")
        return f"{summary}\n{description}"

    def analyze_ticket(self, ticket_id: str) -> list[str]:
        story_text = self.fetch_story_text(ticket_id)
        return self.selector.select_tests(story_text)


def test_jira_analyzer_selects_video_tests_from_mock_ticket() -> None:
    selected = JiraAnalyzer().analyze_ticket("OTT-202")
    assert "selenium_framework/tests/test_video_playback.py" in selected
