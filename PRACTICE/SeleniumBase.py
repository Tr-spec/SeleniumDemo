
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://seleniumbase.io/demo_page/")


driver.find_element(By.ID, "myTextInput").send_keys("Avengers")
driver.find_element(By.ID, "myTextarea").send_keys("EndGame")

# Get attribute name & id
# Text Input Field:
type = driver.find_element(By.ID, "myTextInput").get_attribute("type")
id = driver.find_element(By.ID, "myTextInput").get_attribute("id")
print(f"type = {type}")
print(f"id = {id}")

# Get attribute name & id
# Textarea:
id = driver.find_element(By.ID, "myTextarea").get_attribute("id")
name = driver.find_element(By.NAME, "textareaName").get_attribute("name")
print(f"id = {id}")
print(f"name = {name}")

# Text...
text = driver.find_element(By.ID, "myTextInput2").get_attribute("value")
print(f"value = {text}")


# innerHTMl for text which dos not have any attribute
innerHTML = driver.find_element(By.ID, "myButton").get_attribute("innerHTML")
print(f"innerHTML = {innerHTML}")


# 27-12-2022
# Radio Button
# ele = driver.find_element(By.ID, "radioButton1")
# print("Is Button 1 Selected = ", ele.is_selected())
#
#
# driver.find_element(By.ID, "radioButton2").click()

# check box
check1 = driver.find_element(By.ID, "checkBox2")
check2 = driver.find_element(By.ID, "checkBox3")
check3 = driver.find_element(By.ID, "checkBox4")

print("Is Check Box 1 Selected : ", check1.is_selected())
print("Is Check Box 2 Selected : ", check2.is_selected())
print("Is Check Box 3 Selected : ", check3.is_selected())

# Drop Down













# driver.close()
