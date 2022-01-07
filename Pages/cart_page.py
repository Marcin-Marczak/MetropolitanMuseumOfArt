from selenium.webdriver.common.by import By


class CartPage:
    def __init__(context, driver):
        context.driver = driver
        context.cart_page_product_name = (By.XPATH, "//strong[@class='product-item-name']//a")
        context.cart_page_qty_input = (By.CSS_SELECTOR, "[data-role='cart-item-qty']")

    def cart_page_get_product_name(context):
        return context.driver.find_element(*context.cart_page_product_name).get_attribute("textContent")

    def cart_page_get_number_of_product_in_cart(context):
        return len(context.driver.find_elements(*context.cart_page_qty_input))

    @staticmethod
    def cart_read_product_name_from_temp_file():
        with open("./temp_product_name_use_for_assert.txt", "r") as file:
            product_name_to_assert = file.readline()
        return product_name_to_assert
