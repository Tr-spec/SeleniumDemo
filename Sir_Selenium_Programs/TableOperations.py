import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import datetime

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://www.w3schools.com/html/html_tables.asp")

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[1]').get_attribute('innerHTML'))

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[2]').get_attribute('innerHTML'))

print(len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')))

print(len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td')))


### asssingment : print all table values by using loop