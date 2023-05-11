from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.select import Select


class ChildDetailsPage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.child_name = (MobileBy.ID, "com.qustodio.qustodioapp:id/idChildNameInputEditText")
        self.birth_year = (MobileBy.ID, "com.qustodio.qustodioapp:id/idChildYearInputEditText")
        self.gender_drop_down_menu = (MobileBy.ID, "com.qustodio.qustodioapp:id/newKidGenderDropdownLayout")
        self.birth_year = (MobileBy.ID, "com.qustodio.qustodioapp:id/idChildYearInputEditText")
        self.pick_existing_child_by_name = (MobileBy.XPATH, "//*[@resource-id='com.qustodio.qustodioapp:id/cardText']")

    def enter_child_gender(self, gender):
        dropdown_menu_element = self.driver.find_element(*self.gender_drop_down_menu)
        dropdown = Select(dropdown_menu_element)
        dropdown.select_by_index(gender)

    def enter_child_details(self, name, birth_year, gender):
        self.driver.find_element(*self.child_name).send_keys(name)
        self.driver.find_element(*self.birth_year).send_keys(birth_year)
        self.enter_child_gender(gender)

    def pick_existing_child(self, child_name):
        child_name_element = self.driver.find_element(*self.pick_existing_child_by_name)
        if child_name_element.get_attribute("text") == child_name:
            child_name_element.click()




