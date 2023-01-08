import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Slider.html")

ele = driver.find_element(By.XPATH, "//a[@class='ui-slider-handle ui-state-default ui-corner-all']").click()



