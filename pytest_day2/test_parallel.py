import pytest
from selenium import webdriver


class TestParallel:
    def test_chrome_browser_launcher(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.close()

    def test_edge_browser_launcher(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.close()
