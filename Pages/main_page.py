from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
    def __init__(context, driver):
        context.driver = driver
        context.main_page_sign_in_link = (By.XPATH, "//a[@title='Sign In']")
        context.main_page_first_category = (By.CSS_SELECTOR, "[data-nav-level='nav-1']")
        context.main_page_first_category_name = (By.XPATH, "//li[@data-nav-level='nav-1']//span")
        context.main_page_first_subcategory = (By.CSS_SELECTOR, "[data-nav-level='nav-1-1-2']")
        context.main_page_first_subcategory_name = (By.XPATH, "//li[@data-nav-level='nav-1-1-2']//span")

    def main_page_go_to_login_page(context):
        context.driver.find_element(*context.main_page_sign_in_link).click()
        WebDriverWait(context.driver, 10, 0.25).until(ec.url_contains, "login")

    def main_page_navigate_to_first_category(context):
        element = context.driver.find_element(*context.main_page_first_category)
        ActionChains(context.driver).move_to_element(element).perform()

    def main_page_get_first_category_name(context):
        first_category_name = context.driver.find_element(*context.main_page_first_category_name).text
        first_category_name = first_category_name.lower()
        return first_category_name

    def main_page_navigate_to_first_subcategory(context):
        context.driver.find_element(*context.main_page_first_subcategory).click()

    def main_page_get_first_subcategory_name(context):
        first_subcategory_name = context.driver.find_element(*context.main_page_first_subcategory_name).text
        first_subcategory_name = first_subcategory_name.lower()
        return first_subcategory_name
