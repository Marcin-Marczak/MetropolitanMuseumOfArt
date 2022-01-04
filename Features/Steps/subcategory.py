from behave import *
from Pages.main_page import MainPage
from Pages.subcategory_page import SubcategoryPage


@then("User is on first subcategory page")
def step_impl(context):
    main_page = MainPage(context.driver)
    assert main_page.main_page_get_first_category_name() in context.driver.current_url
    assert main_page.main_page_get_first_subcategory_name() in context.driver.current_url


@when("User opens product page of first product")
def step_impl(context):
    subcategory = SubcategoryPage(context.driver)
    subcategory.subcategory_page_write_first_product_name_into_temp_file()
    subcategory.subcategory_page_go_to_first_product_page()
