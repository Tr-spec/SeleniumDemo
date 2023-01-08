import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()        ## driver is object of Firefox class
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")      ## open website

driver.switch_to.frame("iframeResult")        #Switches focus to the specified frame, by index, name, or webelement.

## if you dont have name attr to iframe
## then you can find iframe by using our any previous approch , by id, by xpath, by css selector, by tag name
## and pass tha web element to frame ###driver.switch_to.frame(element)

driver.find_element(By.XPATH, '/html/body/button').click()
time.sleep(5)
driver.switch_to.alert.accept()
