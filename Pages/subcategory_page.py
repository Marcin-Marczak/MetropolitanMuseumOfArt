from selenium.webdriver.common.by import By


class SubcategoryPage:
    def __init__(context, driver):
        context.driver = driver
        context.subcategory_page_first_product_link = (By.CSS_SELECTOR, ".product-item-link")

    def subcategory_page_write_first_product_name_into_temp_file(context):
        with open("./temp_product_name_use_for_assert.txt", "w+") as file:
            product_name = context.driver.find_element(*context.subcategory_page_first_product_link).get_attribute("textContent")
            file.write(product_name)

    def subcategory_page_go_to_first_product_page(context):
        context.driver.find_element(*context.subcategory_page_first_product_link).click()
