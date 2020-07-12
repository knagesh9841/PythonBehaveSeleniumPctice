from behave import then


@then("user logout from application")
def user_logout_from_application(context):
    Homepage_object = context.pageObject.getHomePage()
    Homepage_object.logoutfromapplication()

