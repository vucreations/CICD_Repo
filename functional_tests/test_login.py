import time
import pytest
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

    # service = Service('/usr/local/bin/chromedriver')
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

@pytest.mark.django_db
class LoginTest(LiveServerTestCase):

    add_todo_button = "//button[text()='Add Todo']"
    login_username_id = "id_username"
    login_password_id = "id_password"
    add_login_button = "//input[@value='Log in']"


    def setUp(self):
        self.driver = get_chrome_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Open the browser and go to the login page
        self.driver.get('http://localhost:8000/r/todo')
        # self.driver.get('http://54.86.83.133/r/todo')
        time.sleep(3)
        
        self.driver.find_element(By.ID, self.login_username_id).send_keys('admin')
        self.driver.find_element(By.ID, self.login_password_id).send_keys('admin')
        self.driver.find_element(By.XPATH, self.add_login_button).click()
        time.sleep(15)
        print("Logged in to the website")

        # self.driver.find_element(By.XPATH, self.add_todo_button).click()
        # time.sleep(3)

        # parent_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-field="title"]')))
        # input_element = parent_element.find_element(By.XPATH, "//input[@type='text']")
        # input_element.send_keys('Text Value 1')

        # input_element.send_keys(Keys.TAB)
        # time.sleep(1)
        # next_input_element = self.driver.switch_to.active_element
        # next_input_element.send_keys('Description Value 1')

        
        # self.driver.find_element(By.XPATH, "//button[@aria-label='Save']").click()
        # time.sleep(3)
