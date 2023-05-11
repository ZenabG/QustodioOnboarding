from appium.webdriver.common.mobileby import MobileBy


class GetStartedPage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.user_input = (MobileBy.ID, "com.qustodio.qustodioapp:id/idUserNameInputEditText")
        self.email_input = (MobileBy.ID, "com.qustodio.qustodioapp:id/idUserEmailInputEditText")
        self.password_input = (MobileBy.ID, "com.qustodio.qustodioapp:id/idUserPasswordInputEditText")
        self.privacy_policy_check = (MobileBy.ID, "com.qustodio.qustodioapp:id/privacyPolicyCheck")
        self.submit_button = (MobileBy.ID, "com.qustodio.qustodioapp:id/button")

    def enter_user_details(self, username, password, email):
        self.driver.find_element(*self.user_input).send_keys(username)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)

    def accept_privacy_policy(self):
        self.driver.find_element(*self.privacy_policy_check).click()

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()
