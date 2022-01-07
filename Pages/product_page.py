from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(context, driver):
        context.driver = driver
        context.product_page_add_to_cart_button = (By.ID, "product-addtocart-button")

    def product_page_add_product_to_cart(context):
        context.driver.find_element(*context.product_page_add_to_cart_button).click()
