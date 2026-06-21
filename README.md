# OTT AI Automation Framework

A production-style hybrid QA automation framework for a Netflix-like OTT web application. It combines Selenium regression testing, Playwright fast UI checks, Pytest orchestration, Page Object Model design, Allure reporting, Jira API integration, and an AI-inspired rule-based test selection MVP.

## Tech Stack

- Python
- Selenium WebDriver
- Playwright
- Pytest
- Page Object Model
- Allure Reports
- Jira REST API integration
- Rule-based AI test selector

## Project Structure

```text
OTT-AI-Automation-Framework/
|-- selenium_framework/
|   |-- pages/
|   |-- tests/
|   `-- utils/
|-- playwright_framework/
|   |-- pages/
|   |-- tests/
|   `-- utils/
|-- ai_engine/
|   |-- test_selector.py
|   `-- jira_analyzer.py
|-- test_data/
|   |-- users.json
|   `-- movies.json
|-- reports/
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
`-- README.md
```

## Application Locator Contract

The framework expects stable `data-testid` attributes in the OTT app, for example:

- Login: `login-email`, `login-password`, `login-submit`, `login-error`, `profile-avatar`
- Home: `trending-card`, `category-row`, `hero-banner`, `banner-next`
- Search: `search-input`, `autocomplete-item`, `search-result-card`, `no-results`
- Video: `video-player`, `play-pause`, `seek-forward`, `seek-backward`, `subtitle-toggle`, `quality-menu`
- Subscription: `plan-basic`, `plan-standard`, `plan-premium`, `confirm-plan`, `subscription-success`

## Setup

```bash
cd OTT-AI-Automation-Framework
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

On macOS/Linux, activate with:

```bash
source .venv/bin/activate
```

## Configuration

Set these environment variables locally or in CI:

```bash
BASE_URL=https://your-ott-app.example.com
BROWSER=chromium
HEADED=false
DEFAULT_TIMEOUT=15
```

Supported browser values:

- Selenium: `chromium`, `chrome`, `firefox`, `edge`
- Playwright: `chromium`, `firefox`, `webkit`

## Run Tests

By default, UI tests are skipped so the framework can be checked without a deployed app.

If you do not have a real OTT app URL, start the bundled local demo app:

```bash
python demo_app/server.py
```

Keep that terminal open. The demo app URL is:

```text
http://127.0.0.1:8000
```

Run AI/Jira unit checks:

```bash
pytest -m ai ai_engine
pytest ai_engine
```

Run Selenium tests:

```bash
pytest selenium_framework/tests --run-ui --base-url https://your-ott-app.example.com --browser chromium
```

Run Selenium tests against the local demo app:

```bash
pytest selenium_framework/tests --run-ui --base-url http://127.0.0.1:8000 --browser chrome
```

Run Playwright tests:

```bash
pytest playwright_framework/tests --run-ui --base-url https://your-ott-app.example.com --browser chromium
```

Run Playwright tests against the local demo app:

```bash
pytest playwright_framework/tests --run-ui --base-url http://127.0.0.1:8000 --browser chromium
```

Run smoke tests only:

```bash
pytest -m smoke --run-ui --base-url https://your-ott-app.example.com
```

Run a specific module:

```bash
pytest -m login --run-ui --base-url https://your-ott-app.example.com
pytest -m search --run-ui --base-url https://your-ott-app.example.com
pytest -m video --run-ui --base-url https://your-ott-app.example.com
pytest -m subscription --run-ui --base-url https://your-ott-app.example.com
```

## Allure Reports

The `pytest.ini` file writes Allure result files to `reports/allure-results`.

Generate and open an Allure report:

```bash
pytest --run-ui --base-url https://your-ott-app.example.com
allure serve reports/allure-results
```

Generate a static report:

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

Screenshots are automatically attached to Allure when Selenium or Playwright UI tests fail.

## AI Test Selection

The MVP selector is rule-based and transparent. It accepts Jira story text and returns relevant test files.

Example rules:

- Story contains `login`, `signin`, or `password` -> login tests
- Story contains `video`, `player`, `subtitle`, or `quality` -> video player tests
- Story contains `payment`, `subscription`, `upgrade`, or `downgrade` -> subscription tests

Example usage:

```python
from ai_engine.test_selector import select_tests_for_story

tests = select_tests_for_story("Improve video player subtitle toggle and quality selector.")
print(tests)
```

## Jira Integration

`ai_engine/jira_analyzer.py` supports mock mode by default, so it can run without Jira credentials.

Mock examples:

```python
from ai_engine.jira_analyzer import JiraAnalyzer

selected_tests = JiraAnalyzer().analyze_ticket("OTT-202")
print(selected_tests)
```

For live Jira mode, set:

```bash
JIRA_USE_MOCK=false
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=qa@example.com
JIRA_API_TOKEN=your-token
```

Then call:

```python
JiraAnalyzer().analyze_ticket("OTT-123")
```

## Design Notes

- Page Object Model keeps locators and browser actions close to each feature.
- Selenium is positioned for deeper regression coverage.
- Playwright is positioned for faster cross-browser UI confidence.
- Pytest markers let CI split smoke, regression, module, and stack-specific runs.
- Test data is externalized in JSON files for beginner-friendly maintenance.
- Allure steps and screenshot hooks improve debugging and reporting visibility.
"# OTT-AI-QA-Automation-Framework" 
