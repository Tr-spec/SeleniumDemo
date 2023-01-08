import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Windows.html")

ele = driver.find_element(By.XPATH, "(//a[@class='dropdown-toggle'])[1]").click()

ele = Select(ele)
ele.select_by_visible_text("Alerts")