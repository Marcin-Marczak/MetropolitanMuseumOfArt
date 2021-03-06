from behave import *
from Pages.main_page import MainPage
from Pages.login_page import LoginPage


@given("User is on login page")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.main_page_go_to_login_page()


@when("User enters valid email in email field")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.login_page_enter_valid_email()


@when("User enters valid password in password field")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.login_page_enter_valid_password()


@when("User clicks on SignIn button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.login_page_save_the_form()


@when("User enters invalid '{email}' and/or invalid '{password}'")
def step_impl(context, email, password):
    login_page = LoginPage(context.driver)
    login_page.login_page_enter_invalid_email_or_password(email, password)


@then("User is logged in")
def step_impl(context):
    assert "My Account" == context.driver.title


@then("User is not logged in")
def step_impl(context):
    assert "My Account" != context.driver.title
