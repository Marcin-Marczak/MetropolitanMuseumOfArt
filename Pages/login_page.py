from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(context, driver):
        context.driver = driver
        context.login_page_sign_in_link = (By.XPATH, "//a[@title='Sign In']")
        context.login_page_email_input = (By.ID, "email")
        context.login_page_password_input = (By.ID, "pass")
        context.login_page_send_button = (By.ID, "send2")

    def go_to_login_page(context):
        context.driver.find_element(*context.login_page_sign_in_link).click()
        WebDriverWait(context.driver, 10, 0.25).until(ec.url_contains, "login")

    def login_page_enter_valid_email(context):
        context.driver.find_element(*context.login_page_email_input).send_keys("kowalski.2021@o2.pl")

    def login_page_enter_valid_password(context):
        context.driver.find_element(*context.login_page_password_input).send_keys("Mar1234!")

    def login_page_enter_invalid_email_or_password(context, username, password):
        context.driver.find_element(*context.login_page_email_input).send_keys(username)
        context.driver.find_element(*context.login_page_password_input).send_keys(password)

    def login_page_save_the_form(context):
        context.driver.find_element(*context.login_page_send_button).click()
