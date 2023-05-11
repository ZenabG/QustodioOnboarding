from appium.webdriver.common.mobileby import MobileBy


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.welcome_text = (MobileBy.ID, "com.qustodio.qustodioapp:id/titleText")
        self.protect_this_device_button = (MobileBy.ID, "com.qustodio.qustodioapp:id/kidsButton")

    def get_welcome_text(self):
        return self.driver.find_element(*self.welcome_text).get_attribute("text")

    def click_protect_this_device(self):
        self.driver.find_element(*self.protect_this_device_button).click()

