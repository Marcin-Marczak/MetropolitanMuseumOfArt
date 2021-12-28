from behave import *
from Pages.main_page import MainPage


@when('User navigates to first category')
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.main_page_navigate_to_first_category()


@when('User goes to first subcategory of first category')
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.main_page_navigate_to_first_subcategory()
