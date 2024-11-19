import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest

from test_redrover.Tanya.Homeworks.locators.locators import *


def check_login(username, password):
    with webdriver.Chrome() as browser:
        browser.get("http://195.133.27.184/")
        login_btn = browser.find_element(LOGIN_BTN)
        login_btn.click()

        browser.find_element(LOGIN_USERNAME).send_keys(username)
        browser.find_element(LOGIN_PASSWORD).send_keys(password)

        submit_btn = browser.find_element(SUBMIT_BTN)
        submit_btn.click()

        