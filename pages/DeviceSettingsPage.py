from appium.webdriver.common.mobileby import MobileBy
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeviceSettingsPage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.qustodio_allow_button = (MobileBy.ID, "com.qustodio.qustodioapp:id/closeButton")
        self.allow_reporting_go_to_settings = (
            MobileBy.ID, "com.qustodio.qustodioapp:id/activateAccessManufacturerButton")
        self.device_native_click = (MobileBy.ID, "android:id/summary")
        self.switch_widget_toggle = (MobileBy.ID, "android:id/switch_widget")
        self.device_alert_ok = (MobileBy.ID, "android:id/button1")
        self.usage_data_access_toggle = (MobileBy.XPATH, "//*[@accessibility-id='Qustodio Kids,34.81 MB, Off, Switch']")
        self.notification_toggle = (MobileBy.XPATH, "//*[@resource-id='android:id/title']")
        self.allow_device_location_access_while_using_app = (MobileBy.ID, "com.android.permissioncontroller:id"
                                                                          "/permission_allow_foreground_only_button")
        self.allow_permissions_button = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.activate_qustodio_button = (MobileBy.ID, "com.android.settings:id/action_button")
        self.qustodio_protection_completed = (MobileBy.ID, "com.qustodio.qustodioapp:id/deviceProtectedButton")

    def click_allow_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.qustodio.qustodioapp:id/closeButton")))
        return self.driver.find_element(*self.qustodio_allow_button).click()

    def lets_do_it_button(self):
        self.click_allow_button()

    def accept_device_alert(self):
        WebDriverWait(self.driver, 10).until(
            EC.alert_is_present())
        return self.driver.find_element(*self.device_alert_ok).click()

    def is_qustodio_protection_enabled(self):
        if self.driver.find_element(*self.qustodio_protection_completed).get_attribute("text") == "Finish":
            return True
        else:
            return False

    def allow_accessibility_tracking(self):
        self.driver.find_element(*self.allow_reporting_go_to_settings).click()
        self.driver.find_element(*self.device_native_click).click()
        self.driver.find_element(*self.device_native_click).click()
        self.driver.find_element(*self.switch_widget_toggle).click()
        self.driver.find_element(*self.device_alert_ok).click()

    def allow_usage_tracking(self, toggle_name):
        self.click_allow_button()
        self.toggle_settings_with_scroll(toggle_name, 625, 1704, 684, 793)

    def allow_notification_access(self, toggle_name):
        self.click_allow_button()
        self.toggle_settings(toggle_name)
        self.accept_device_alert()

    def scroll_page_to_element(self, start_x, start_y, end_x, end_y):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def toggle_settings_with_scroll(self, toggle_name, start_x, start_y, end_x, end_y):
        notification_toggle_elements = self.driver.find_elements(*self.notification_toggle)
        try:
            for element in notification_toggle_elements:
                if element.get_attribute("text") == toggle_name:
                    element.click()
                else:
                    self.scroll_page_to_element(start_x, start_y, end_x, end_y)
        except StaleElementReferenceException:
            print("Stale element exception occurred. Retrying...")

    def toggle_settings(self, toggle_name):
        notification_toggle_elements = self.driver.find_elements(*self.notification_toggle)
        try:
            for element in notification_toggle_elements:
                if element.get_attribute("text") == toggle_name:
                    element.click()
        except StaleElementReferenceException:
            print("Stale element exception occurred. Retrying...")

    def allow_app_display(self, toggle_name):
        self.click_allow_button()
        self.toggle_settings(toggle_name)

    def allow_permissions(self):
        self.click_allow_button()
        self.accept_device_alert()
        self.driver.find_element(*self.allow_device_location_access_while_using_app).click()
        # self.accept_device_alert()
        self.driver.find_element(*self.allow_permissions_button).click()

    def activate_device_admin(self):
        self.click_allow_button()
        self.driver.find_element(*self.activate_qustodio_button).click()

    def allow_vpn_access(self):
        self.click_allow_button()
        self.accept_device_alert()
