from appium.webdriver.common.mobileby import MobileBy


class AvatarPage:
    def __init__(self, driver):
        self.driver = driver

        # Define locators using Appium's MobileBy class
        self.avatar_pig = (MobileBy.ID, "com.qustodio.qustodioapp:id/avatar1")
        self.avatar_owl = (MobileBy.ID, "com.qustodio.qustodioapp:id/avatar2")
        self.avatar_mouse = (MobileBy.ID, "com.qustodio.qustodioapp:id/avatar3")
        self.avatar_cow = (MobileBy.ID, "com.qustodio.qustodioapp:id/avatar4")
        self.avatar_pigeon = (MobileBy.ID, "com.qustodio.qustodioapp:id/avatar5")
        self.avatar_cat = (MobileBy.ID, "com.qustodio.qustodioapp:id/avatar6")

    def pick_avatar_pig(self):
        self.driver.find_element(*self.avatar_pig).click()

    def pick_avatar_owl(self):
        self.driver.find_element(*self.avatar_owl).click()

    def pick_avatar_mouse(self):
        self.driver.find_element(*self.avatar_mouse).click()

    def pick_avatar_cow(self):
        self.driver.find_element(*self.avatar_cow).click()

    def pick_avatar_pigeon(self):
        self.driver.find_element(*self.avatar_pigeon).click()

    def pick_avatar_cat(self):
        self.driver.find_element(*self.avatar_cat).click()


