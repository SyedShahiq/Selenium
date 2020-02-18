import unittest

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from selenium import webdriver


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.register = RegisterPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.dashboard = DashboardPage(self.driver)

    def test_register(self):
        self.driver.get('http://stage.edx.org/')
        self.assertTrue(self.homepage.is_browser_on_the_page())
        self.homepage.click_register()
        self.assertTrue(self.register.is_browser_on_the_page())
        self.register.fill_form()
        self.register.submit_form()
        self.assertTrue(self.dashboard.is_browser_on_the_page())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
