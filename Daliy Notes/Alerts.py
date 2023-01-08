import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# for = click for js alert
ele = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
# innerHTML = ele.get_attribute('innerHTML')
# print(innerHTML)

ele.click()
time.sleep(2)
driver.switch_to.alert.accept()

# for  = Click for JS Confirm
ele = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
time.sleep(2)
driver.switch_to.alert.accept()

# for  = Click for JS Prompt
ele = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(3)
driver.switch_to.alert.dismiss()


