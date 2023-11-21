import pytest


class TestLoginReports:
    def test_launch_browser(self, browser_setup):
        self.driver = browser_setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        expected_title = "OrangeHRM"
        assert self.driver.title.__eq__(expected_title)
        self.driver.close()
