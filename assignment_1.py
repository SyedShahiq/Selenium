import unittest
import time

from selenium import webdriver

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        self.driver.get('https://awesomeblogposts.herokuapp.com/login/')
        username = self.driver.find_element_by_css_selector('input[id="id_username"]')
        username.send_keys('shahiq')
        password = self.driver.find_element_by_css_selector('input[id="id_password"]')
        password.send_keys('shahiq123')
        button = self.driver.find_element_by_css_selector('button[type="submit"]')
        button.click()
        time.sleep(3)
        assert 'https://awesomeblogposts.herokuapp.com/' == self.driver.current_url
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
