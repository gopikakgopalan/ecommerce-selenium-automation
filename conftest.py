#browser setup and tear down fixtures
import pytest
import os
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )



@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()

    # Disable Google Password Manager popups
        options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        )

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(
            f"Unsupported browser: {browser}. Use chrome or firefox."
        )

    if not headless:
        driver.maximize_window()

    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()

#automatically capture screenshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            test_name = re.sub(r"[^A-Za-z0-9_.-]", "_", item.nodeid)

            screenshot_path = os.path.join("screenshots", f"{test_name}.png")

            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")