from behave import *


@then("User is logged in")
def step_impl(context):
    assert "My Account" == context.driver.title
