# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
#
# driver.find_element(By.XPATH, "//button[normalize-space()='Start']").click()
#
# # presence_of_element_located
# locator1 = By.XPATH("//div[@id='loading']")
# ele1 = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator1))
#
# # in simple words we have to wait for this h4 element
# # we have to import service WebDriverWait
# # ele = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='finish']/child::h4")))
#
# # visibility_of_element_located
# locator = (By.XPATH, "//div[@id='finish']/child::h4")
# ele = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locator))
#
#
#
# # ele = driver.find_element(By.XPATH, "//div[@id='finish']/child::h4")
# print(f"Message : {ele.get_attribute('innerHTML')}")
##--------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.find_element(By.XPATH, "//div[@id='start']/child::*").click()

locator1 = (By. XPATH, "//div[@id='loading']")
ele1 = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator1))
print(ele1.get_attribute('innerHTML'))

locator = (By.XPATH, "//div[@id='finish']/child::h4")
ele = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locator))
print(ele.get_attribute('innerHTML'))











