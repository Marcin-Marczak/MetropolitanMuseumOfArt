from behave import *
from Pages.mini_cart_page import MiniCartPage


@when('User goes to cart')
def step_impl(context):
    mini_cart = MiniCartPage(context.driver)
    mini_cart.mini_cart_page_go_to_cart()
