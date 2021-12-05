from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@given('User is on login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@title='Sign In']").click()
    WebDriverWait(context.driver, 10, 0.25).until(ec.url_contains, "login")


@when('User enter valid username "kowalski.2021@o2.pl" in username field')
def step_impl(context):
    context.driver.find_element(By.ID, "email").send_keys("kowalski.2021@o2.pl")


@when('User enter valid password "Mar1234!" in password field')
def step_impl(context):
    context.driver.find_element(By.ID, "pass").send_keys("Mar1234!")


@when('User enter invalid "{username}" and/or invalid "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "email").send_keys(username)
    context.driver.find_element(By.ID, "pass").send_keys(password)


@when('User clicks on SignIn button')
def step_impl(context):
    context.driver.find_element(By.ID, "send2").click()


@then('User is not logged in')
def step_impl(context):
    assert "My Account" != context.driver.title
