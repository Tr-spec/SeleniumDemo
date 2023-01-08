

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/tables")

rows = len(driver.find_elements(By.XPATH, '//*[@id="table1"]/tbody/tr'))
cols = len(driver.find_elements(By.XPATH, '//*[@id="table1"]/thead/tr/th'))

print(rows)
print(cols)

print("Last Name" + ' ' + "First Name" + ' ' + "Email" + ' ' + "Due" + ' ' + "Web Site" + ' ' + "Action")

for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element(By.XPATH, "//*[@id='table1']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end=' ')
    print()

