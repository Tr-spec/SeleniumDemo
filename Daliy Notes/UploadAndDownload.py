# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://the-internet.herokuapp.com/upload")
#
# fileInput = driver.find_element(By.ID, "file-upload")
# button = driver.find_element(By.ID, "file-submit")
#
# fileInput.send_keys(r"D:\1\upload_pc.jpg")
# button.click()
#
# time.sleep(5)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.implicitly_wait(20)

download = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
download.click()

time.sleep(5)

