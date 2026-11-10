# tests/test_session.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_prevent_direct_inventory_access_after_logout(driver):

    login = LoginPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    inventory.logout()

    driver.get("https://www.saucedemo.com/inventory.html")


    assert login.is_username_field_visible(), (
    "Login page was not displayed after attempting direct inventory access"
)

    assert "/inventory.html" not in driver.current_url


    