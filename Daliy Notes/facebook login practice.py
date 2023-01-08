import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.facebook.com")

driver.maximize_window()

time.sleep(2)
emailElement = driver.find_element(By.ID, "email")
emailElement.send_keys("www.shastrakar123@reddiff.com")

time.sleep(2)

passElement = driver.find_element(By.ID, "pass")
passElement.send_keys("121121")

time.sleep(2)
logElement = driver.find_element(By.NAME ,"login")
logElement.click()

time.sleep(2)
driver.back()
















































