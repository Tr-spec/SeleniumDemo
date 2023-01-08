import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()         ## c has to be C capital
###driver = webdriver.Chrome(r"c:\chromedriver.exe")
driver.get("https://facebook.com/")

time.sleep(10)





# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# s=Service('C:/chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get('https://www.google.com')

time.sleep(10)