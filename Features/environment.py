from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json

data = json.load(open("Configuration/config.json", "r"))


def before_scenario(context, scenario):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome("./chromedriver.exe", options=chrome_options)
    context.driver.get(data["main_page"])
    context.driver.implicitly_wait(30)
    context.driver.set_window_size(1500, 800)


def after_scenario(context, scenario):
    context.driver.quit()
