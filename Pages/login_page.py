from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(context, driver):
        context.driver = driver
        context.login_page_email_input = (By.ID, "email")
        context.login_page_password_input = (By.ID, "pass")
        context.login_page_send_button = (By.ID, "send2")

    def login_page_enter_valid_email(context):
        context.driver.find_element(*context.login_page_email_input).send_keys("kowalski.2021@o2.pl")

    def login_page_enter_valid_password(context):
        context.driver.find_element(*context.login_page_password_input).send_keys("Mar1234!")

    def login_page_enter_invalid_email_or_password(context, username, password):
        context.driver.find_element(*context.login_page_email_input).send_keys(username)
        context.driver.find_element(*context.login_page_password_input).send_keys(password)

    def login_page_save_the_form(context):
        context.driver.find_element(*context.login_page_send_button).click()
