from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome("./chromedriver.exe")
    context.driver.get("https://store.metmuseum.org")
    context.driver.implicitly_wait(30)
    context.driver.set_window_size(1500, 800)


def after_scenario(context, scenario):
    context.driver.quit()
