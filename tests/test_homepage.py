from  selenium.webdriver.common.by import By


def test_homepage_title(driver):

    

    assert driver.title == "Swag Labs"