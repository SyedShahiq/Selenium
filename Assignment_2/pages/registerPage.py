import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class RegisterPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,15)
        self.check_email = True

    def is_register_visible(self):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Register')))
        return True

    def click_register(self):
        sign_in_button = self.driver.find_element_by_link_text('Register')
        sign_in_button.click()

    def is_browser_on_the_page(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

    def check_error(self):
        return self.driver.find_element_by_css_selector('#register-email-validation-error-msg').text

    def fill_form(self):
        count = 0
        email = ''
        while self.check_email == True:
            email_elem = self.driver.find_element_by_css_selector('#register-email')
            if count == 0:
                email = 'test@mailinator.com'
            else:
                email = 'test_'+str(count)+'@mailinator.com'
            count+=1
            email_elem.clear()
            email_elem.send_keys(email)
            name_elem = self.driver.find_element_by_css_selector('#register-name')
            name_elem.clear()
            name_elem.send_keys('Syed Shahiq')
            time.sleep(3)
            if self.check_error() == "":
                self.check_email = False
        username_elem = self.driver.find_element_by_css_selector('#register-username')
        username = email.split('@')
        username_elem.send_keys(username[0])
        pwd_elem = self.driver.find_element_by_css_selector('#register-password')
        pwd_elem.send_keys('mehfoozian1R!')
        country = Select(self.driver.find_element_by_css_selector('#register-country'))
        country.select_by_visible_text("Antarctica")

    def submit_form(self):
        subnit_elem = self.driver.find_element_by_css_selector('button[type="submit"]')
        subnit_elem.click()
