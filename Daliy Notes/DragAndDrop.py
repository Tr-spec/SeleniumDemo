import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source = driver.find_element(By.ID, "box3")
target = driver.find_element(By.ID, "box103")

# we have to import class ActionChains()
action = ActionChains(driver)

action.drag_and_drop(source, target).perform()

source_2 = driver.find_element(By.ID, "box5")
target_2 = driver.find_element(By.ID, "box105")

action.drag_and_drop(source_2, target_2).perform()

time.sleep(5)




