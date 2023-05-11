from appium.webdriver.common.mobileby import MobileBy


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.get_started_button = (MobileBy.ID, "com.qustodio.qustodioapp:id/signupButton")
        self.login_button = (MobileBy.ID, "com.qustodio.qustodioapp:id/loginText")

    def click_get_started_button(self):
        self.driver.find_element(*self.get_started_button).click()

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()