import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://ui.vision/demo/webtest/frames/")

driver.switch_to.frame("(//frame)[1]")

ele = driver.find_element(By.XPATH, "//input[@name='mytext1']").send_keys("1212")


