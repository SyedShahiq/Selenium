from .base_page import BasePage
from .dashboard_page import DashboardPage


class LoginPage(BasePage):

    def is_browser_on_page(self):
        return self.find_elem('button[type="submit"]').is_displayed()

    def fill_form(self, user_email, user_password):
        email_elem = self.find_elem('#login-email')
        email_elem.send_keys(user_email)
        pwd_elem = self.find_elem('#login-password')
        pwd_elem.send_keys(user_password)

    def submit_form(self):
        submit_elem = self.find_elem('button[type="submit"]')
        submit_elem.click()
        return DashboardPage(self.driver).wait_for_page()
