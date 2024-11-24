import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest

from test_redrover.Tanya.Homeworks.locators.locators import *
from test_redrover.Tanya.Homeworks.pages.base_page import BasePage


class LoginPage(BasePage):

    # def click_login_btn(self):
    #     return self.click_to_element(LOGIN_BTN)

    def check_login(self):
        # login_btn = browser.find_element(LOGIN_BTN)
        # login_btn.click()

        self.browser.find_element(*LOGIN_USERNAME).send_keys('test')
        self.browser.find_element(*LOGIN_PASSWORD).send_keys('testtest')

        submit_btn = self.browser.find_element(*SUBMIT_BTN)
        submit_btn.click()

