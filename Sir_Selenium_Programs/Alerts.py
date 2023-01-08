
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()        ## driver is object of Firefox class
driver.get("https://the-internet.herokuapp.com/javascript_alerts")      ## open website

ele = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
## Assingment : create custom xpath for this button

ele.click()

time.sleep(3)
driver.switch_to.alert.accept()         ## Ok  # click on ok button

##driver.switch_to.alert.dismiss()        ## cancel ## click on cancel button




