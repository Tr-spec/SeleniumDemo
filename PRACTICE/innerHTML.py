from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

inner = driver.find_element(By.XPATH, "//input[@id='placeholderText']")

print(inner.get_attribute('placeholder'))

green = driver.find_element(By.XPATH, "//button[@id='myButton']")

print(green.get_attribute('innerHTML'))

paragraph = driver.find_element(By.XPATH, "//p[@id='pText']")
print(paragraph.get_attribute('innerHTML'))

text = driver.find_element(By.XPATH, "//input[@id='myTextInput2']")
print(text.get_attribute('value'))


# to print links
links = driver.find_elements(By.XPATH, "//a[@class='linkClass']")
for link in links:
    print(link.get_attribute('href'))









