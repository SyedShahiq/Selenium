import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.home_page import HomePage

class EdxLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)
        self.homepage = HomePage(self.driver)

    def test_login(self):
        self.driver.get('https://stage.edx.org')
        self.assertTrue(self.homepage.is_browser_on_the_page())
        self.homepage.click_signin()
        self.login.fill_form('*****@yopmail.com', '******')
        self.login.submit_form()
        self.dashboard.go_to_courses_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

