from selenium import webdriver
from selenium.webdriver.common.by import By

class FacebookLogin:

    # locators
    txtbox_username_id = "email"
    txtbox_password_id = "pass"
    button_login_xpath = "(//button[normalize-space()='Log in'])[1]"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions
    def setUsername(self, username):
        usernametxt = self.driver.find_element(By.ID, self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.txtbox_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def click(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()













