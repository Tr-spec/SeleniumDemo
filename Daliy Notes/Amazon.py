import time

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.facebook.com")          # To open Website

driver.maximize_window()                        # To Maximize window

print(f"Page Title = {driver.title}")           # Page Title = Facebook – log in or sign up
# Gives the title of the current page

print(f"Site URL = {driver.current_url}")       # Site URL = https://www.facebook.com/

time.sleep(3)
driver.get("https://www.amazon.com")

time.sleep(3)
driver.back()

time.sleep(3)
driver.forward()























# driver.close()      # Close current window of browser
# driver.quit()       # quits all windows opened by our script




































