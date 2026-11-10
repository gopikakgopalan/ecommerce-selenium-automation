from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_logout(driver):
    login = LoginPage(driver)
        
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.logout()

    assert login.is_username_field_visible()

