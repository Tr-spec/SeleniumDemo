import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")

# # ActionChains
# # widgets = driver.find_element(By.XPATH, "//a[normalize-space()='More']")
# # datePicker = driver.find_element(By.XPATH, "//a[normalize-space()='File Download']")
# #
# # ac = ActionChains(driver)
# #
# # ac.move_to_element(widgets).move_to_element(datePicker).click().perform()
# # time.sleep(10)
# # ===================================
#
# # dropdown
# skills = driver.find_element(By.XPATH, "//select[@id='Skills']")
# dropDown1 = Select(skills)
#
# # dropDown.select_by_visible_text('CSS')
# # time.sleep(10)
#
# print(len(dropDown1.options))
#
# for i in dropDown1.options:
#     print(i.text)
#
# # ===================================
# # Boostrap dropdown
# driver.find_element(By.XPATH, "//span[@role='combobox']").click()
# countries = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
#
# print(len(countries))
#
# for i in countries:
#     print(i.text)
#
# for c in countries:
#     if c.text == 'Denmark':
#         c.click()
#         break
#
# # time.sleep(5)
# ===================================

cookie = driver.get_cookies()
print(len(cookie))

driver.add_cookie({"name": "__test"})
cookie = driver.get_cookies()
print(len(cookie))

for c in cookie:
    print(c)






