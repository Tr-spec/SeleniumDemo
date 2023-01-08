from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://seleniumbase.io/demo_page/")

ele = driver.find_element(By.ID, 'dropOption1')
print("Is element displayed  : ", ele.is_displayed())       #Whether the element is visible to a user

ele = driver.find_element(By.ID, 'myTextInput')
print("Is element displayed  : ", ele.is_displayed())       #Whether the element is visible to a user

## ==============================================================================================

ele = driver.find_element(By.ID, 'myTextInput')
print("Is element Enabled  : ", ele.is_enabled())       #Returns whether the element is enabled.


## ==============================================================================================

#Returns whether the element is selected.
#Can be used to check if a checkbox or radio button is selected.

ele = driver.find_element(By.ID, "radioButton1")
print("Radio Button 1 is ", ele.is_selected())