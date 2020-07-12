import logging
import os

from behave import fixture, use_fixture

from pages.PageObjectManager import PageObjectManager
from util import BrowserFactory, Logger, Utilities, OptionsManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

path = os.getcwd()

path = path+"\\resources\config\Logger.conf"


@fixture
def selenium_browser_setdriver(context):
    # -- SETUP-FIXTURE PART:
    logger = Logger.getlogger()
    browser_name = context.config.userdata.get('BrowserName')
    Utilities.killbrowserdriver(browser_name)
    if browser_name == "Chrome":
        logger.info(browser_name + " Browser option is selected")
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=OptionsManager.getchromeoptions())
    elif browser_name == "Firefox":
        logger.info(browser_name + " Browser option is selected")
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=OptionsManager.getfirefoxoptions())
    else:
        logger.info("Entered Wrong Browser name")

    yield context.driver
    # -- CLEANUP-FIXTURE PART:

    #context.driver.quit()


def before_all(context):
    use_fixture(selenium_browser_setdriver, context)
    context.config.setup_logging()
    context.pageObject = PageObjectManager(context.driver)
    log = Logger.getlogger()
    log.info("before all is called")



def after_all(context):
    logger = Logger.getlogger()
    logger.info("After all is called")
    context.driver.quit()


def before_step(context, step):
    logger = Logger.getlogger()
    logger.info(f"Before Step {step} is called")


def after_step(context, step):
    logger = Logger.getlogger()
    logger.info(f"After Step {step} is called")


def before_scenario(context, scenario):
    logger = Logger.getlogger()
    logger.info(f"Before Scenario {scenario} is called")


def after_scenario(context, scenario):
    logger = Logger.getlogger()
    logger.info(f"After Scenario {scenario} is called")


def before_feature(context, feature):
    logger = Logger.getlogger()
    logger.info(f"Before Feature {feature} is called")


def after_feature(context, feature):
    logger = Logger.getlogger()
    logger.info(f"After scenario {feature} is called")

