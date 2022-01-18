from behave import *
from Pages.main_page import MainPage
from Pages.subcategory_page import SubcategoryPage
from Pages.product_page import ProductPage
from Pages.mini_cart_page import MiniCartPage
from Pages.cart_page import CartPage


@given("User is on product page")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.main_page_navigate_to_first_category()
    main_page.main_page_navigate_to_first_subcategory()
    subcategory = SubcategoryPage(context.driver)
    subcategory.subcategory_page_write_first_product_name_into_temp_file()
    subcategory.subcategory_page_go_to_first_product_page()


@when("User adds product to cart")
def step_impl(context):
    product_page = ProductPage(context.driver)
    product_page.product_page_add_product_to_cart()


@when("User goes to cart via mini cart")
def step_impl(context):
    mini_cart = MiniCartPage(context.driver)
    mini_cart.mini_cart_page_go_to_cart()


@then("This product in cart")
def step_impl(context):
    cart = CartPage(context.driver)
    product_name_from_subcategory_page = cart.cart_read_product_name_from_temp_file()
    product_name_from_cart = cart.cart_page_get_product_name()
    assert product_name_from_subcategory_page == product_name_from_cart


@then("There's only 1 item in cart")
def step_impl(context):
    cart = CartPage(context.driver)
    number_of_products_in_cart = cart.cart_page_get_number_of_products_in_cart()
    assert 1 == number_of_products_in_cart
