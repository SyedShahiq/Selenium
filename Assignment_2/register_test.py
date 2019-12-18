import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.registerPage import RegisterPage
from pages.dashboard import DashboardPage

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.register = RegisterPage(self.driver)
        self.dashboard = DashboardPage(self.driver)

    def test_register(self):
        self.driver.get('http://stage.edx.org/')
        self.assertTrue(self.register.is_register_visible())
        self.register.click_register()
        self.assertTrue(self.register.is_browser_on_the_page())
        self.register.fill_form()
        self.register.submit_form()
        self.assertTrue(self.dashboard.check_dashboard_title())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()