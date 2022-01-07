from selenium.webdriver.common.by import By


class MiniCartPage:
    def __init__(context, driver):
        context.driver = driver
        context.mini_cart_go_to_checkout_button = (By.ID, "top-cart-btn-checkout")

    def mini_cart_page_go_to_cart(context):
        context.driver.find_element(*context.mini_cart_go_to_checkout_button).click()
