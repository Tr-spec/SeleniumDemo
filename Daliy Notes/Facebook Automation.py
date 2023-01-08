

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")


print(f"Site URL : {driver.current_url}")

print(f"Page details : {driver.title}")


emailElement = driver.find_element(By.ID, "email")
emailElement.send_keys("swapnl45@gmail.com")

emailElement = driver.find_element(By.ID, "pass")
emailElement.send_keys("132424")

loginElement = driver.find_element(By.NAME, "login")
loginElement.click()


driver.back()


# Create New Account

# createElement = driver.find_element(By.NAME, "Create New Account")
# createElement.click()
#
#
# firstElement = driver.find_element(By.NAME, "First name")
# firstElement.send_keys("sagar")
#
# surnameElement = driver.find_element(By.NAME, "Surname")
# surnameElement.send_keys("sarade")
#
# mobElement = driver.find_element(By.NAME, "Mobile number or email address")
# mobElement.send_keys("www.swapnil4883@gmail.com")
#
# mobElement = driver.find_element(By.NAME, "New password")
# mobElement.send_keys("3424324")
#
# mobElement = driver.find_element(By.NAME, "day")
# mobElement.send_keys("12")
#
# mobElement = driver.find_element(By.NAME, "month")
# mobElement.send_keys("Aug")
#
# mobElement = driver.find_element(By.NAME, "year")
# mobElement.send_keys("2019")
#
# mobElement = driver.find_element(By.NAME, "websubmit")
# mobElement.click()
