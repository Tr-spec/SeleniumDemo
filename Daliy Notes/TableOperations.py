
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro")
#
# driver.switch_to.frame("iframeResult")
#
# rows = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr"))
# cols = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th"))
#
# print(rows)
# print(cols)
#
# print("company" + ' ' + "contact" + ' ' + "country")
#
# for r in range(2, rows + 1):
#     for c in range(1, cols + 1):
#         value = driver.find_element(By.XPATH, "/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(value, end=" ")
#     print()



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")


rows = len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr'))

cols = len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th'))

print(f"Total Rows in Table : {rows}")
print(f"Total Columns in Table = {cols}")

print("Company" + ' ' + "Contact" + ' ' + "Country")

Z








# for i in range(1, 11):
#     if i == 5:
#         break
#     print(f"10 * {i} = {10 * i}")












