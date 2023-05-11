from appium.webdriver.common.mobileby import MobileBy


class DeviceNamePage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.device_name_text_field = (MobileBy.ID, "com.qustodio.qustodioapp:id/idDeviceNameInputEditText")
        self.click_next_button = (MobileBy.ID, "com.qustodio.qustodioapp:id/button")

    def enter_device_name(self, device_name):
        self.driver.find_element(*self.device_name_text_field).clear()
        self.driver.find_element(*self.device_name_text_field).send_keys(device_name)

    def click_next(self):
        self.driver.find_element(*self.click_next_button).click()

