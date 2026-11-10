# E-Commerce Selenium Automation Framework

A Python-based web UI automation framework built using **Selenium WebDriver and Pytest**, designed to automate login and session-management workflows for the SauceDemo e-commerce application.

This project demonstrates practical test automation skills, reusable Page Object Model (POM) design, cross-browser execution, parallel testing, and preparation for CI/CD integration.

## Tech Stack

- **Programming Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Test Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** pytest-html
- **Parallel Execution:** pytest-xdist
- **Browsers:** Google Chrome, Mozilla Firefox
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions (planned)

## Application Under Test

[SauceDemo](https://www.saucedemo.com/)

A demo e-commerce application used to practise web automation scenarios.

## Project Structure

```text
Ecommerce_Automation/
│
├── config/
│   └── test_data.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   ├── test_logout.py
│   └── test_session.py
│
├── screenshots/
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Automated Test Scenarios

### Login functionality
- Verify successful login with valid credentials.
- Verify login with invalid username.
- Verify login with invalid password.
- Verify validation for empty username and password.
- Verify locked-out user behaviour.
- Verify appropriate error messages.

### Inventory and session management
- Verify inventory page after successful login.
- Validate the number of products displayed.
- Verify successful logout.
- Verify login page is displayed after logout.
- Verify logged-out users cannot directly access the inventory page.
- Verify error messages disappear after successful login.

## Framework Features

### Page Object Model (POM)
- Separate page classes for login and inventory pages.
- Centralised element locators.
- Reusable page actions and methods.
- Improved maintainability and reduced code duplication.

### Explicit Waits
- Uses Selenium WebDriverWait.
- Uses expected conditions to synchronise interactions with dynamic elements.
- Waits for elements to become visible or disappear.

### Parameterized Testing
- Uses Pytest parameterization to execute multiple login scenarios.
- Reuses test functions with different test data and expected results.

### Screenshot Capture
- Automatically captures screenshots when test execution fails.
- Stores screenshots in the `screenshots/` directory.

### HTML Test Reports
- Generates execution reports using pytest-html.

### Cross-Browser Testing
- Supports Google Chrome and Mozilla Firefox.
- Browser selection through command-line arguments.

### Headless Execution
- Supports Chrome and Firefox headless execution.

### Parallel Execution
- Uses pytest-xdist to execute tests across multiple worker processes.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/gopikakgopalan/ecommerce-selenium-automation.git
```

### 2. Navigate to the project directory

```bash
cd ecommerce-selenium-automation
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure the selected browser is installed. Selenium Manager handles browser driver management for supported Selenium versions.

## Running Tests

### Run all tests using Chrome

```bash
pytest -v --browser=chrome
```

### Run tests using Firefox

```bash
pytest -v --browser=firefox
```

### Run tests in headless mode

```bash
pytest -v --browser=chrome --headless
```

### Run tests in parallel

```bash
pytest -n 2 --browser=chrome -v
```

### Generate HTML report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

## Test Reporting

The framework generates HTML test execution reports and captures screenshots for failed tests.

- HTML reports: `reports/`
- Failure screenshots: `screenshots/`

## Future Enhancements

- Integrate the framework with GitHub Actions for automated CI/CD execution.
- Publish test execution reports as GitHub Actions artifacts.
- Expand coverage to product selection, cart and checkout workflows.
- Add structured logging.
- Integrate API testing with the UI automation framework.

## Learning Objectives

This project is part of my hands-on learning and portfolio development in Software Development Engineer in Test (SDET).

It demonstrates practical implementation of:
- Python automation.
- Selenium WebDriver.
- Pytest test design.
- Page Object Model.
- Cross-browser automation.
- Test execution and reporting.
- Parallel testing.
- CI/CD fundamentals.

## Author

Developed as a hands-on Selenium automation portfolio project.

