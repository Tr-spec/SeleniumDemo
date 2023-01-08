import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()        ## driver is object of Firefox class
driver.get("https://the-internet.herokuapp.com/windows")      ## open website

driver.find_element(By.LINK_TEXT, 'Click Here').click()

h3Element = driver.find_element(By.TAG_NAME, 'h3')
print(f"H3 content : {h3Element.get_attribute('innerHTML')}")       #['79234964-48c7-403c-9233-9fc453cb48e6', 'a41dfc0b-791c-4909-9bb6-c191d534b33a']

###driver.switch_to.new_window()           ## open new tab

## need to switch to new window
print(driver.window_handles)
print("Before switch window ",driver.current_window_handle)
print("Before switch title ",driver.title)

all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])         #all_handles[-1]
print("all_handles[-1]", all_handles[-1])
print("After switch window ",driver.current_window_handle)
print("After switch title ",driver.title)

## this will switch to newly opened window
h3Element = driver.find_element(By.TAG_NAME, 'h3')
print(f"newly opened window content : {h3Element.get_attribute('innerHTML')}")

time.sleep(10)

