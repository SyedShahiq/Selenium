import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.home_page import HomePage

class EdxLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login = LoginPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.dashboard = DashboardPage(self.driver)

    def test_login(self):
        self.driver.get('https://stage.edx.org/')
       self.assertTrue(self.homepage.is_browser_on_the_page())
        self.homepage.click_signin()
        self.assertTrue(self.login.is_browser_on_the_page())
        self.login.fill_form()
        self.login.submit_form()
        self.dashboard.is_browser_on_the_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
