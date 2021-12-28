from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MiniCartPage:
    def __init__(context, driver):
        context.driver = driver
        context.mini_cart_button = (By.CSS_SELECTOR, "[title='My Bag']")
        context.mini_cart_go_to_checkout_button = (By.ID, "top-cart-btn-checkout")

    def mini_cart_page_go_to_cart(context):
        ActionChains(context.driver).move_to_element(context.driver.find_element(*context.mini_cart_button)).click(context.driver.find_element(*context.mini_cart_go_to_checkout_button)).perform()
