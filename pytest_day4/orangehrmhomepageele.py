import time

from selenium.webdriver.common import by
from selenium import webdriver
from selenium.webdriver.common.by import By


class OrangeHRMHomeElements:
    text_dashboard_xpath = "//h6[normalize-space()='Dashboard']"

    def __init__(self, driver):
        self.driver = driver

    def checkDashboardDisplayed(self):
        time.sleep(5)
        self.dashboard_ele = self.driver.find_element(by=By.XPATH, value=self.text_dashboard_xpath)
        self.dashboard_status = self.dashboard_ele.is_displayed()
        return self.dashboard_status
