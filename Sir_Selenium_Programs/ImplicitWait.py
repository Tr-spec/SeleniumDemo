import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()        ## driver is object of Firefox class
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")      ## open website
driver.implicitly_wait(10)  # Comes from selenium. It will pause maximun for given sec and min till element appears on html
## once defined it wil be applicable to all controls

driver.find_element(By.XPATH, "//button[text() = 'Start']").click()
##time.sleep(10)          # it is belonging to python



element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')

print(f"Message : {element.get_attribute('innerHTML')}")


time.sleep(10)