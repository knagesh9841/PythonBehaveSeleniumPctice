from pages.Home_Page import HomePage
from pages.Login_Page import LoginPage


class PageObjectManager:

    def __init__(self, driver):
        self.driver = driver
        self.LoginPage_object = None
        self.Homepage_object = None

    def getLoginPage(self):
        return self.LoginPage_object if self.LoginPage_object is not None else LoginPage(self.driver)

    def getHomePage(self):
        return self.Homepage_object if self.Homepage_object is not None else HomePage(self.driver)

