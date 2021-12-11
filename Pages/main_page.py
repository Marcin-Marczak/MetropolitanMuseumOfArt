from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:
    def __init__(context, driver):
        context.driver = driver
        context.main_page_sign_in_link = (By.XPATH, "//a[@title='Sign In']")

    def main_page_go_to_login_page(context):
        context.driver.find_element(*context.main_page_sign_in_link).click()
        WebDriverWait(context.driver, 10, 0.25).until(ec.url_contains, "login")
