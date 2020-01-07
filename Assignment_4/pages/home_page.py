from .base_page import BasePage

class HomePage(BasePage):

    def is_browser_on_the_page(self):
        self.wait_for_partial_title_match('Free Online Courses')
        return True

    def click_signin(self):
        sign_in_button = self.find_elem('.js-user-cta a:nth-child(1)')
        sign_in_button.click()

    def click_register(self):
        sign_in_button = self.find_elem('.js-user-cta a:nth-child(2)')
        sign_in_button.click()