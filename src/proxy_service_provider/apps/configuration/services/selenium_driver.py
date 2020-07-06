from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import unittest
import os
import time
from datetime import datetime


class SeleniumDriver():
    def __init__(self):
        options = Options()
        # options.add_argument("--window-size=1920x1080")
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        print(os.getcwd())
        chrome_driver = os.getcwd() + "/driver/chromedriver"
        self.selenium = webdriver.Chrome(options=options, executable_path=chrome_driver)

    def tearDown(self):
        self.selenium.quit()

    def extract_url(self,url):
        # self.sign_in()
        selenium = self.selenium
        # # Opening the link we want to test
        selenium.get(url)
        html = None
        try:
            WebDriverWait(selenium,10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'table')))
            # button = selenium.find_element_by_tag_name('table')[0]
            # button.click()
            html = selenium.page_source
            selenium.quit()
            return  html
        except Exception as ex:
            print('Loading Timeout')
            selenium.quit()
            return html


