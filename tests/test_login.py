from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

from config.test_data import(
    INVALID_CREDENTIALS_ERROR,
    EMPTY_USERNAME_ERROR,
    EMPTY_PASSWORD_ERROR,
    LOCKED_OUT_ERROR
)


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
     ("sta_user", "secret_sauce", INVALID_CREDENTIALS_ERROR),
     ("standard_user", "secret", INVALID_CREDENTIALS_ERROR),
     ("", "secret_sauce", EMPTY_USERNAME_ERROR),
     ("standard_user", "", EMPTY_PASSWORD_ERROR),
      ("locked_out_user", "secret_sauce", LOCKED_OUT_ERROR)],
    ids=[
        "invalid_username",
        "invalid_password",
        "empty_username",
        "empty_password",
        "locked_out_user"
    ])
def test_invalid_login(driver, username, password, expected_error):
    login = LoginPage(driver)
    
    login.login(username, password)

    actual_error = login.get_error_message()
    
    assert actual_error == expected_error


def test_product_count(driver):
    login = LoginPage(driver)
        
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    assert inventory.get_inventory_count() == 6


    

