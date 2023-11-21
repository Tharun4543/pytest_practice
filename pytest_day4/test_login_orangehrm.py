from selenium import webdriver

from loginpageelements import LoginPageElementsPOM
from orangehrmhomepageele import OrangeHRMHomeElements


class TestValidateLogin:
    def test_check_login_orangehrm(self, browser_setup):
        self.driver = browser_setup
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login_page_ele = LoginPageElementsPOM(self.driver)
        self.login_page_ele.setUsername("Admin")
        self.login_page_ele.setPassword("admin123")
        self.login_page_ele.clickLoginbtn()
        self.orangehrm_home_page_ele = OrangeHRMHomeElements(self.driver)
        try:

            self.dashboard_status_value = self.orangehrm_home_page_ele.checkDashboardDisplayed()
            self.driver.close()
            assert self.dashboard_status_value == True
        except:
            self.driver.close()
            assert False
