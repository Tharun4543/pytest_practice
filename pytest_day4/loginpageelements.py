import time

from selenium.webdriver.common import by
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPageElementsPOM:
    textbox_username_name = "username"
    textbox_password_name = "password"
    btn_login_xpath = "//button[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        time.sleep(4)
        self.username_ele = self.driver.find_element(by=By.NAME, value=self.textbox_username_name)
        self.username_ele.send_keys(username)

    def setPassword(self,password):
        time.sleep(4)
        self.password_ele = self.driver.find_element(by=By.NAME, value=self.textbox_password_name)
        self.password_ele.send_keys(password)

    def clickLoginbtn(self):
        time.sleep(4)
        self.driver.find_element(by=By.XPATH,value=self.btn_login_xpath).click()

