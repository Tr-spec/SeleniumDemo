import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import datetime

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://seleniumbase.io/demo_page")

driver.get_screenshot_as_file(r'C:/Development/Class/Python/CT12/SeleniumPrograms/screenshot.png')
driver.get_screenshot_as_file('/screenshots/screenshot2.png')

#
driver.save_screenshot(f'screenshot3_{datetime.datetime.now()}.png')
