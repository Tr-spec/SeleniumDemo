import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()        ## driver is object of Firefox class
driver.get("https://www.facebook.com")      ## open website

driver.maximize_window()            ## to maximize window

emailElement = driver.find_element(By.ID, "email")
emailElement.send_keys("sagar@gmail.com")

passElement = driver.find_element(By.ID, "pass")
passElement.send_keys("sagar@123")

loginButton = driver.find_element(By.NAME, "login")
loginButton.click()



