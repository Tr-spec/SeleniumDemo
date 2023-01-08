import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()        ## driver is object of Firefox class
driver.get("https://seleniumbase.io/demo_page")      ## open website

# Manual way to do this.. which creates complexity when we multiple combinations
ele = driver.find_element(By.XPATH, "//*[@id='mySelect']/option[3]")
ele.click()

## /html/body/form/table/tbody/tr[7]/td[2]/select/option[3]

###==================================================================

ele = driver.find_element(By.XPATH, "//*[@id='mySelect']")      ## driver.find_element(By.ID, "mySelect")
Select(ele)
