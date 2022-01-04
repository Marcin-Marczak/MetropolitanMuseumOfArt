from behave import *
from Pages.product_page import ProductPage


@then("User is on product page")
def step_impl(context):
    assert "Description" in context.driver.page_source


@when("User adds product to cart")
def step_impl(context):
    product_page = ProductPage(context.driver)
    product_page.product_page_add_product_to_cart()
