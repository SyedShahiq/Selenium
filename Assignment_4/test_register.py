import unittest

from selenium import webdriver

from pages.register_page import RegisterPage
from pages.dashboard_page import DashboardPage
from pages.base_page import BasePage
from pages.home_page import HomePage

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.register = RegisterPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.dashboard = DashboardPage(self.driver)

    def test_register(self):
        self.driver.get('https://stage.edx.org/')
        self.assertTrue(self.homepage.is_browser_on_the_page())
        self.homepage.click_register()
        self.assertTrue(self.register.is_browser_on_the_page())
        self.register.fill_form()
        self.register.submit_form()
        self.assertTrue(self.dashboard.go_to_courses_page())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()