import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()        ## driver is object of Firefox class
driver.get("https://seleniumbase.io/demo_page")      ## open website

driver.maximize_window()

ele = driver.find_element(By.ID, 'myTextInput2')

result = ele.get_attribute('value')
print(f"Value : {result}")
print(f"type : {ele.get_attribute('type')}")
print(f"name : {ele.get_attribute('name')}")
print(f"id : {ele.get_attribute('id')}")

'innerHTML'






