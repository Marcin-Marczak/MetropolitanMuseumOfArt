from selenium.webdriver.common.by import By
import json

data = json.load(open("Configuration/config.json", "r"))


class LoginPage:
    def __init__(context, driver):
        context.driver = driver
        context.login_page_email_input = (By.ID, "email")
        context.login_page_password_input = (By.ID, "pass")
        context.login_page_send_button = (By.ID, "send2")

    def login_page_enter_valid_email(context):
        context.driver.find_element(*context.login_page_email_input).send_keys(data["email"])

    def login_page_enter_valid_password(context):
        context.driver.find_element(*context.login_page_password_input).send_keys(data["password"])

    def login_page_enter_invalid_email_or_password(context, email, password):
        context.driver.find_element(*context.login_page_email_input).send_keys(email)
        context.driver.find_element(*context.login_page_password_input).send_keys(password)

    def login_page_save_the_form(context):
        context.driver.find_element(*context.login_page_send_button).click()
