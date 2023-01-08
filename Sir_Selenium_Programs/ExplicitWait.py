import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()        ## driver is object of Firefox class
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")      ## open website

driver.find_element(By.XPATH, "//button[text() = 'Start']").click()


##elementLoding = driver.find_element(By.XPATH, '//*[@id="loading"]')
locator = By.XPATH, '//*[@id="loading"]'
elementLoding = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locator))
print(elementLoding.get_attribute('innerHTML'))


##time.sleep(10)          # it is belonging to python
locator = (By.XPATH, '//*[@id="finish"]/h4')
element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator))
### element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')

print(f"Message : {element.get_attribute('innerHTML')}")

## DOM => Document object model

## Presense => code is available in HTML
## Visibility => visible to users  on page/screen as end user. html may or may not presnet

time.sleep(10)