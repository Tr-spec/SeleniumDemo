import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

couTries = driver.find_elements(By.XPATH, '//*[@id="select2-billing_country-results"]/li')

print(len(couTries))


# for r in couTries:
#     print(r.text)

for country in couTries:
    if country.text == 'Austria':
        country.click()
        break

driver.save_screenshot(os.getcwd() + "//screenshot.png")

time.sleep(5)


