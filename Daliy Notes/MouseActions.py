import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

parentDiv = driver.find_element(By.XPATH, "//div[@id='myDropdown']")

# importing class ActionChains()
actionObj = ActionChains(driver)    # object creation for ActionChains() class

# 1) move_to_element()
ele = driver.find_element(By.XPATH, "//a[@id='dropOption1']")
actionObj.move_to_element(parentDiv).move_to_element(ele).click().perform()

ele2 = driver.find_element(By.XPATH, "//a[@id='dropOption2']")
actionObj.move_to_element(parentDiv).move_to_element(ele2).click().perform()
time.sleep(3)

# 2) double_click
double_click_obj = driver.find_element(By.XPATH, "//button[@id='myButton']")
actionObj.double_click(double_click_obj).perform()

# 3) context_click i.e right click
context_click_obj = driver.find_element(By.XPATH, "//input[@id='myTextInput2']")
actionObj.context_click(context_click_obj).perform()


time.sleep(5)
















