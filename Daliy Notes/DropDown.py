import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")     # to open website
#
# # to find drop down
# # importing Select class for Drop Down
# obj1 = driver.find_element(By.XPATH, "//select[@id='mySelect']")
#
# dropdown = Select(obj1)     # creating object of select
#
# # 1) select_by_index
# # time.sleep(2)
# # dropdown.select_by_index(2)
#
# # time.sleep(2)
# # dropdown.select_by_index(3)
#
# ##==================================================================
#
# # 2) select_by_value
# # time.sleep(2)
# # dropdown.select_by_value("50%")
#
# # time.sleep(2)
# # dropdown.select_by_value("100%")
#
# ##==================================================================
#
#
# # 3) select_by_visible_text
# # time.sleep(2)
# dropdown.select_by_visible_text("Set to 75%")
#
# ##==================================================================
#
#
# # count how many options in drop down
# print(f"Total Options in Drop Down : {len(dropdown.options)}") ##Returns a list of all options belonging to this select tag
#
# ##==================================================================
#
#
# # find how many options exist in drop down
# for option in dropdown.options:
#     print(option.text)
#
# driver.find_element(By.LINK_TEXT, "")


##==================================================================
##==================================================================

driver.get("https://demo.automationtesting.in/Register.html")

dropDown = driver.find_element(By.XPATH, "//select[@id='Skills']")
dropDownList = Select(dropDown)
dropDownList.select_by_visible_text('Analytics')

print(len(dropDownList.options))

for option in dropDownList.options:
    print(option.text)

time.sleep(5)






