import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://phptravels.com/demo/")

# cookie = driver.get_cookies()
# print(f"before deleting cookies : {len(cookie)}")
#
# # driver.delete_all_cookies()
# # cookie = driver.get_cookies() # we need to capture the cookies otherwise it will not return updated values
# # print(f"after deleting cookies : {len(cookie)}") # driver.get_cookies() is mandatory
#
# for c in cookie:
#     print(c.get("name"), c.get("value"))

# ====================================
# cookie = driver.get_cookies()
# print(f"total Number of Cookies : {len(cookie)}")
#
# for c in cookie:
#     print(c.keys())

# ====================================
# how to delete cookies
cookie = driver.get_cookies()
print(f"cookies before deleting : {len(cookie)}")

driver.delete_all_cookies()
cookie = driver.get_cookies()
print(f"cookies after deleting : {len(cookie)}")

driver.switch_to.new_window('tab')
time.sleep(5)
