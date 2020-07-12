from behave import given, then, when
from util import BrowserFactory, Logger


@given("User is able to login to application with valid credentials")
def User_is_able_to_login_to_application(context):
    logger = Logger.getlogger()
    logger.info("User is able to login to application with valid credentials Step is called.")


@when("User Enters Login Details")
def User_Enters_Login_Details(context):
    LoginPage_object = context.pageObject.getLoginPage()
    LoginPage_object.logintoapplication()




