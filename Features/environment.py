from selenium import webdriver
import json

data = json.load(open("Configuration/config.json", "r"))


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome("./chromedriver.exe")
    context.driver.get(data["main_page"])
    context.driver.implicitly_wait(30)
    context.driver.set_window_size(1500, 800)


def after_scenario(context, scenario):
    context.driver.quit()
