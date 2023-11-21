import pytest


class TestLoginCLI:
    def test_launch_browser(self, browser_setup_cli):
        self.driver = browser_setup_cli
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        expected_title = "OrangeHRM"
        assert self.driver.title.__eq__(expected_title)
        self.driver.close()
