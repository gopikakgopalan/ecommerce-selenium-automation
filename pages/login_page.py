from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    #locators
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_field = (By.ID, "login-button")
    error_message_field = (By.CSS_SELECTOR, "[data-test='error']")


    def enter_username(self, username):
        username_element = self.driver.find_element(*self.username_field)
        username_element.clear()
        username_element.send_keys(username)
        

    def enter_password(self, password):
        password_element = self.driver.find_element(*self.password_field)
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        login_element = self.driver.find_element(*self.login_field)
        login_element.click()

    def get_error_message(self):
        error_element = self.driver.find_element(*self.error_message_field)
        return error_element.text

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 10)

        return wait.until(EC.visibility_of_element_located(locator))


    def is_username_field_visible(self):
        return self.wait_for_element(self.username_field).is_displayed()

#login workflow
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


    def wait_for_element_to_disappear(self, locator):
        wait = WebDriverWait(self.driver, 10)

        return wait.until(
        EC.invisibility_of_element_located(locator)
        )