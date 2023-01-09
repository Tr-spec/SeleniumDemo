import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

ob = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']")
ob.send_keys("swapnil")
ob1 = driver.find_element(By.XPATH, "//input[@name='email']")
ob1.send_keys("www.111221@gmail.com")
ob3 = driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']")
ob3.send_keys("32781321732")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()
dd = driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']")
dropdown = Select(dd)
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

time.sleep(10)
