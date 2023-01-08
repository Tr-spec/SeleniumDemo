#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
#
# driver.find_element(By.XPATH, "//div[@class='example']/child::a").click()   # custom XPATH Made by SS
# # another method to find the element by clicking on the link itself by LINK_TEXT
# # driver.find_element(By.LINK_TEXT, "Click Here").click()
#
# ele1 = driver.find_element(By.XPATH, "//div[@class='example']/child::a").get_attribute("innerHTML")
# print(f"innerHTMl : {ele1}")
#
# # need to switch to new window
# # driver.switch_to.new_window()
#
# print(driver.window_handles)
# print(driver.current_window_handle) # parent window handle id : CDwindow-C6A350481054F2361A0F0DE4C8C7062D
# print(driver.title)
#
# all_handles = driver.window_handles
# driver.switch_to.window(all_handles[-1])
# print(all_handles[-1])
# print(driver.title)
#
# ele2 = driver.find_element(By.TAG_NAME, "h3").get_attribute("innerHTML")
# print(f"innerHTML : {ele2}")
#
#
# # time.sleep(3)

##--------------------------------------------------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
#
# driver.find_element(By.XPATH, "//div[@class='example']/child::a").click()   # custom XPATH Made by SS
#
# print(driver.current_window_handle) # returns id of the current window handle
# print(f"current window title : {driver.title}")
#
# all_handle = driver.window_handles
# driver.switch_to.window(all_handle[-1])
# print(f"new window handle : {driver.title}")
#
# ele2 = driver.find_element(By.TAG_NAME, "h3").get_attribute("innerHTML")
# print(f"innerHTML : {ele2}")

##--------------------------------------------------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")
#
# driver.find_element(By.XPATH, "//div[@class='example']/child::a").click()   # custom XPATH Made by SS
#
# print(driver.current_window_handle)
#
# all_handles = driver.window_handles
#
# for handle in all_handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     if driver.title == "The Internet":
#         driver.close()
#
# time.sleep(10)

##--------------------------------------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[1]").click()


print(driver.current_window_handle)
print(f"parent window title : {driver.title}")

all_handle = driver.window_handles

for handle in all_handle:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":  # it will close the parent window
        driver.close()








