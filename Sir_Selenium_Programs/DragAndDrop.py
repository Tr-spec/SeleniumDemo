import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source = driver.find_element(By.ID, 'box3')
target = driver.find_element(By.ID, 'box103')

action = ActionChains(driver)
action.drag_and_drop(source, target).perform()

time.sleep(10)