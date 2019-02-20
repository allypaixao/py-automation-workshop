from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PageHome:

    def __init__(self, driver):
        self.driver = driver
        LOGIN_BUTTON = (by.ID, 'btnLogin')
        USERNAME = (by.NAME, 'password')
        PASSWORD = (by.NAME, 'password')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automation-sandbox.herokuapp.com")

    def wait_page_load(self):
        self.driver.implicitly_wait(90)

    def test_page_login_loaded(self):
        self.assertIn("Login", driver.title) 
    
    def insert_login_key(self):
        self.driver.find_element.USERNAME.send_keys("demouser")
    
    def insert_password_key(self):
        self.driver.find_element.PASSWORD.send_keys("abc123")

    def click_Login(self):
        self.driver.find_element.LOGIN_BUTTON.click()