from appium.webdriver.common.mobileby import MobileBy


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.email_input = (MobileBy.ID, "com.qustodio.qustodioapp:id/idUserEmailInputEditText")
        self.password_input = (MobileBy.ID, "com.qustodio.qustodioapp:id/idUserPasswordInputEditText")
        self.login_button = (MobileBy.ID, "com.qustodio.qustodioapp:id/button")

    def user_login(self, username, password):
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()