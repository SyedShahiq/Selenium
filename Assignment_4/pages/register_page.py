import time

from .base_page import BasePage
from selenium.webdriver.support.select import Select


class RegisterPage(BasePage):
    def is_browser_on_the_page(self):
        return self.find_elem('button[type="submit"]').is_displayed()

    def check_error(self):
        return self.find_elem('#register-email-validation-error-msg').text

    def fill_form(self):
        count = 6
        email = ''
        check_email = True
        while check_email == True:
            email_elem = self.find_elem('#register-email')
            if count == 6:
                email = 'test_6@mailinator.com'
            else:
                email = 'test_'+str(count)+'@mailinator.com'
            count += 1
            email_elem.clear()
            email_elem.send_keys(email)
            name_elem = self.find_elem('#register-name')
            name_elem.clear()
            name_elem.send_keys('TEST TEST')
            time.sleep(3)
            if self.check_error() == "":
                check_email = False
        username_elem = self.find_elem('#register-username')
        username = email.split('@')
        username_elem.send_keys(username[0])
        pwd_elem = self.find_elem('#register-password')
        pwd_elem.send_keys('mehfoozian1R!')
        country = Select(self.find_elem('#register-country'))
        country.select_by_visible_text("Antarctica")

    def submit_form(self):
        subnit_elem = self.find_elem('button[type="submit"]')
        subnit_elem.click()
