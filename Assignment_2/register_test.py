import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.registerPage import RegisterPage

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.register = RegisterPage(self.driver)

    def test_register(self):
        self.driver.get('http://stage.edx.org/')
        self.assertTrue(self.register.is_register_visible())
        self.register.click_register()
        self.assertTrue(self.register.is_browser_on_the_page())
        self.register.fill_form()
        # self.register.submit_form()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()