from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DashboardPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,15)

    def check_dashboard_title(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'title'),'Dashboard'))