import time

from selenium import webdriver

driver = webdriver.Firefox()        ## driver is object of Firefox class
driver.get("https://www.facebook.com")      ## open website

driver.maximize_window()            ## to maximize window

print(f"Page Title : {driver.title}")       ## gives title of page

print(f"Page URL : {driver.current_url}")       ## Gets the URL of the current page.

time.sleep(3)

driver.get("https://www.amazon.com")
print(f"Page Title : {driver.title}")       ## gives title of page
print(f"Page URL : {driver.current_url}")       ## Gets the URL of the current page.

time.sleep(3)
driver.back()           ## 1 step back

time.sleep(3)
driver.forward()        ## 1 step ahead




# driver.close()          ## close current window of browser
# driver.quit()           #quits all windows opened by our script