from behave import *
from Pages.cart_page import CartPage


@then("User sees first product from first category/first subcategory in cart")
def step_impl(context):
    cart = CartPage(context.driver)
    product_quantity_in_cart = cart.cart_page_get_product_quantity()
    assert product_quantity_in_cart == "1"
    product_name_from_subcategory_page = cart.cart_read_product_name_from_temp_file()
    product_name_from_cart = cart.cart_page_get_product_name()
    assert product_name_from_subcategory_page == product_name_from_cart
