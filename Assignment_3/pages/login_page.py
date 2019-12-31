from .base_page import BasePage

class LoginPage(BasePage):

    def is_browser_on_the_page(self):
        self.wait_for_element_visibility('button[type="submit"]')
        return True

    def fill_form(self):
        email_elem = self.find_elem('#login-email')
        email_elem.send_keys('....')
        pwd_elem = self.find_elem('#login-password')
        pwd_elem.send_keys('....')

    def submit_form(self):
        subnit_elem = self.find_elem('button[type="submit"]')
        subnit_elem.click()


