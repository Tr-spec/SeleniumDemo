import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://seleniumbase.io/demo_page")     # to open website

# elements = driver.find_elements(By.TAG_NAME, "a")

# for links in elements:
#     print(links.get_attribute("href"))

driver.find_element(By.LINK_TEXT, "seleniumbase.com").click()
driver.back()

# driver.find_element(By.PARTIAL_LINK_TEXT, "seleniumbase")
# driver.back()



