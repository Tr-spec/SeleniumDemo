import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.implicitly_wait(10)  # implicitly_wait belongs to selenium

driver.find_element(By.XPATH, "//button[normalize-space()='Start']").click()

# time.sleep(10)    # time.sleep belongs to selenium

ele = driver.find_element(By.XPATH, "//div[@id='finish']/child::h4")
print(f"Message : {ele.get_attribute('innerHTML')}")

time.sleep(5)