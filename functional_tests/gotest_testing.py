import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

class LoginTest(LiveServerTestCase):

    login_username_id = "email_id"
    login_password_id = "password"
    add_login_button = "login"


    def setUp(self):
        self.driver = get_chrome_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):

        self.driver.get('https://gotest.gridlex.com/ab/ep/1300718593298325504/en/1301094509438480384/rm/m/300000/f/100002/rc')
        time.sleep(3)
        
        self.driver.find_element(By.ID, self.login_username_id).send_keys('harish.b@gridlex.com')
        self.driver.find_element(By.ID, self.login_password_id).send_keys('Harish@123')
        self.driver.find_element(By.ID, self.add_login_button).click()
        time.sleep(15)

        self.driver.find_element(By.ID, ":r9:").send_keys('Email')
        self.driver.find_element(By.ID, "input_label_field_id_sf_300008").send_keys('Selenium Test')
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//button[text()='Add Activity']").click()
        time.sleep(10)

        print("gotest_passed")

        # parent_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-field="title"]')))
        # input_element = parent_element.find_element(By.XPATH, "//input[@type='text']")
        # input_element.send_keys('Text Value 1')

        # input_element.send_keys(Keys.TAB)
        # time.sleep(1)
        # next_input_element = self.driver.switch_to.active_element
        # next_input_element.send_keys('Description Value 1')

        
        # self.driver.find_element(By.XPATH, "//button[@aria-label='Save']").click()
        # time.sleep(3)
