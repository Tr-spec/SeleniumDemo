import time
from selenium import webdriver
from FacebookPageObjectModel import FacebookLogin

class TestLogin:

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

        self.lp = FacebookLogin(self.driver)

        self.lp.setUsername("www.solution@gmail.com")
        self.lp.setPassword("1212121")
        self.lp.click()
        print(self.driver.title)
        time.sleep(5)



