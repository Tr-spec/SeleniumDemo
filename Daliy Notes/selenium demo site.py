
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://seleniumbase.io/demo_page")


# ATTRIBUTE NAME = Pre-Filled Text Field:
element = driver.find_element(By.ID, "myTextInput2")
result = element.get_attribute("type")

print(f"type = {result}")
print(f"id = {element.get_attribute('id')}")
print(f"value = {element.get_attribute('value')}")
print(f"name = {element.get_attribute('name')}")


# innerHTML for a value which doesn't hve any attribute
buttonElement = driver.find_element(By.ID, "myButton")
code = buttonElement.get_attribute('innerHTML')
print(code)



# Attribute Name = Text Input Field
# We are going to find type & id

ele1 = driver.find_element(By.ID, 'myTextInput')
result = ele1.get_attribute('type')

print(f"type = {result}")
print(f"id = {ele1.get_attribute('id')}")



# Attribute Name = Read-Only Text Field
# We are going to find type & id

ele2 = driver.find_element(By.ID, 'readOnlyText')
ele2.get_attribute('type')

print(f'id = {ele2.get_attribute("id")}')
print(f'type = {ele2.get_attribute("type")}')
print(f'value = {ele2.get_attribute("value")}')



## Testing Begins
texElement = driver.find_element(By.ID, 'myTextInput')
texElement.send_keys('12345456')

areaElement = driver.find_element(By.ID, 'myTextarea')
areaElement.send_keys('www.swapnil@rediffmail.com')

buttonEle = driver.find_element(By.ID, 'myButton')
buttonEle.click()

# text read only
ele1 = driver.find_element(By.ID, 'myTextInput2')
result_pre = ele1.get_attribute('value')
print(f"prefilled text value = {result_pre}")

ele2 = driver.find_element(By.ID, 'readOnlyText')
result_2 = ele2.get_attribute('value')
print(f"value = {result_2}")

# innerHTML
ele3 = driver.find_element(By.ID, 'pText')
result_3 = ele3.get_attribute('innerHTML')
print(f"innerHTMl = {result_3}")

ele4 = driver.find_element(By.ID, 'placeholderText')
ele4.send_keys('HDFC BANK')
























