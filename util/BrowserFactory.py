
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from util import OptionsManager, Utilities, Logger

driver = None


def setdriver(browser_name):
    try:
        global driver
        Utilities.killbrowserdriver(browser_name)
        if browser_name == "Chrome":
            print(browser_name+" Browser option is selected")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=OptionsManager.getchromeoptions())
        elif browser_name == "Firefox":
            print(browser_name + " Browser option is selected")
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=OptionsManager.getfirefoxoptions())
        else:
            print("Entered Wrong Browser name")

    except Exception as e:
        print("Exception Occurred")


def getdriver():
    return driver

