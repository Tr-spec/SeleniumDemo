

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.ID, "small-searchterms").send_keys("Apple MacBook Pro 13-inch")
driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()





























