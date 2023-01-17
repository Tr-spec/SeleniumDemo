import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
userName = driver.find_element(By.XPATH, "//span[normalize-space()='Recruitment']")
passWord = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
loginBtn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

userName.send_keys("Admin")
passWord.send_keys("admin123")
loginBtn.click()
time.sleep(5)
