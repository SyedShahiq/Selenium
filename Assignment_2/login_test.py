import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login = LoginPage(self.driver)

    def test_login(self):
        self.driver.get('http://stage.edx.org/')
        self.assertTrue(self.login.is_signin_visible())
        self.login.click_signin()
        self.assertTrue(self.login.is_browser_on_the_page())
        self.login.fill_form()
        self.login.submit_form()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()