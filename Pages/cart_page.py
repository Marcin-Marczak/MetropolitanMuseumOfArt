from selenium.webdriver.common.by import By


class CartPage:
    def __init__(context, driver):
        context.driver = driver
        context.cart_page_qty_input = (By.CSS_SELECTOR, "[data-role='cart-item-qty']")
        context.cart_page_product_name = (By.XPATH, "//strong[@class='product-item-name']//a")

    def cart_page_get_product_quantity(context):
        return context.driver.find_element(*context.cart_page_qty_input).get_attribute("value")

    def cart_page_get_product_name(context):
        return context.driver.find_element(*context.cart_page_product_name).get_attribute("textContent")

    @staticmethod
    def cart_read_product_name_from_temp_file():
        with open("./temp_product_name_use_for_assert.txt", "r") as file:
            product_name_to_assert = file.readline()
        return product_name_to_assert
