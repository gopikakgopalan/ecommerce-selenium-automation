from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_error_disappears_on_successful_login(driver):
    login = LoginPage(driver)

    login.login("standard_user", "sdgdfg")

    error = login.get_error_message()

    assert len(error) != 0, ("error is there")

    login.login("standard_user", "secret_sauce")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Verify previous error message is no longer visible
    assert login.wait_for_element_to_disappear(login.error_message_field), (
        "Error message is still visible after successful login"
    )