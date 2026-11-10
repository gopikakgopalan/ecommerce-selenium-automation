#product page and logout actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    #locators
    inventory_title = (By.CLASS_NAME, "title")
    inventory_items = (By.CLASS_NAME, "inventory_item")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")

    def get_inventory_title(self):
        inventory_element = self.wait_for_element(self.inventory_title).text

        return inventory_element

    def get_inventory_count(self):
        inventory_items_elements = self.wait_for_element(
        self.inventory_items
    )

        return len(self.driver.find_elements(*self.inventory_items))


    def logout(self):
        self.wait_for_element(self.menu_button).click()

        self.wait_for_element(self.logout_button).click()

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
    
        return wait.until(EC.visibility_of_element_located(locator))