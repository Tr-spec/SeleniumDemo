import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("selenium")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("practice")
driver.find_element(By.XPATH, "//div[@class='col-md-8 col-xs-8 col-sm-8']/child::textarea").send_keys("Pune")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("www.selenium@gmail.com")
driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("8888888888")

# radio button
ele = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]").click()
# print(ele.is_enabled())     # true
# print(ele.is_displayed())   # true
# print(ele.is_selected())    # false

# check box
driver.find_element(By.XPATH, "//input[@id='checkbox1']").click()
driver.find_element(By.XPATH, "//input[@id='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@id='checkbox3']").click()

# drop down
obj1 = driver.find_element(By.XPATH, "//select[@id='Skills']")
dropdown = Select(obj1)

# select_by_visible_text
dropdown.select_by_visible_text("Adobe Photoshop")

# select_by_value
dropdown.select_by_value("Backup Management")

# select_by_id
dropdown.select_by_index(25)

print(f"Total options in Skills : {len(dropdown.options)}")

# print all options in skills
for option in dropdown.options:
    print(option.text)

driver.close()






