from selenium.webdriver.common.by import By

from util import WaitUtilities, ExcelUtils, PropertyManager, Logger


class LoginPage:

    # ********* Constructor *********

    def __init__(self, driver):
        self.driver = driver

    # ********** WebElements **********

    obj_signin = (By.XPATH, "//a[text()='Sign in']")
    obj_username = (By.XPATH, "//input[@id='session_email']")
    obj_password = (By.XPATH, "//input[@id='session_password']")
    obj_loginbtn = (By.XPATH, "//input[@name='commit']")

    # ********* Page Methods *********

    def logintoapplication(self):
        log = Logger.getlogger()
        try:
            self.driver.get(PropertyManager.getconfigdata("basicurl"))
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            credentials = ExcelUtils.readdata("Testdata.xlsx", "Credentials", 2)
            userNames = ExcelUtils.getdata(credentials, "Username")
            passwords = ExcelUtils.getdata(credentials, "Password")
            WaitUtilities.waitforpagetitleis(self.driver, "Address Book - Sign In", 5)
            signinbtn = self.driver.find_element(*LoginPage.obj_signin)

            WaitUtilities.waitForElementVisible(self.driver, LoginPage.obj_signin, 5)
            signinbtn.click()
            username = self.driver.find_element(*LoginPage.obj_username)
            password = self.driver.find_element(*LoginPage.obj_password)
            loginbtn = self.driver.find_element(*LoginPage.obj_loginbtn)
            WaitUtilities.waitForElementVisible(self.driver, LoginPage.obj_username, 5)
            username.send_keys(userNames)
            password.send_keys(passwords)
            loginbtn.click()

            flag = WaitUtilities.waitforpagetitleis(self.driver, "Address Book", 5)

            assert flag, "should be Login to Application.::Successfully Login to Application."

            log.info("Successfully Login to Application.")

        except Exception as e:
            log.error("Failed to Login to Application.", exc_info=True)


