import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.PageHome import setUp
from pageobjects.PageHome import navigate_login_page

class LoginTest(unittest.TestCase):


    def test_login_succesfull(self):
        self.setUp(driver)
        self.navigate_login_page(driver)
    
    def validate_login_page_loaded(self):
        #self.element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "navbar-brand"))))
        assert "Automation Example" in driver.title

        self.driver.quit()
