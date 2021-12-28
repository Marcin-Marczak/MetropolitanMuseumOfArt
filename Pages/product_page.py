from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage:
    def __init__(context, driver):
        context.driver = driver
        context.product_page_add_to_cart_button = (By.ID, "product-addtocart-button")

    def product_page_add_product_to_cart(context):
        WebDriverWait(context.driver, 15, 0.25).until(ec.element_to_be_clickable, context.driver.find_element(*context.product_page_add_to_cart_button))
        context.driver.find_element(*context.product_page_add_to_cart_button).click()
