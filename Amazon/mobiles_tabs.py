from selenium.webdriver.common.by import By


class MobilesPage:
    # Constructor to initialize the driver
    def __init__(self, driver):
        self.driver = driver

    # Locators (By.ID, By.XPATH, etc.)
    Mobile_BUTTON = (By.XPATH, '//a/img[@alt="iphone 13"]')

    def click_example_button(self):
        self.driver.find_element(*self.Mobile_BUTTON).click()
        print('iphone 13 link was clicked')

