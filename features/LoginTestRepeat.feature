Feature: Verify user is able to login to Application.
	Description: It will Login to Application and Verify the Title of Page.
  Scenario: Login Application.
          Given User is able to login to application with valid credentials
          When User Enters Login Details
          Then user logout from application