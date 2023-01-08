print("Hello World")

# from selenium import webdriver      # Driver is object if Firefox class
# driver = webdriver.Firefox()        # Firefox is a default constructor
# driver.get("https://www.facebook.com")

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")          # To open Website

driver.maximize_window()                        # To Maximize window

print(f"Page Title = {driver.title}")           # Page Title = Facebook – log in or sign up
# Gives the title of the current page

print(f"Site URL = {driver.current_url}")       # Site URL = https://www.facebook.com/


driver.get("https://www.amazon.com")

driver.close()      # Close current window of browser
driver.quit()       # quits all windows opened by our script



















