import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
from test_redrover.Tanya.Homeworks.locators.locators import *
from test_redrover.Tanya.Homeworks.data.urls import *


# 1. С использованием Explicit waits и Expected Conditions
# @pytest.fixture
# def chrome_options():
#     options = Options()
#     options.add_argument('--start-maximized')
#     return options


#
#
# @pytest.fixture
# def browser(chrome_options):
#     browser = webdriver.Chrome(options=chrome_options)
#     return browser


#
#
# @pytest.fixture
# def wait(browser):
#     wait = WebDriverWait(browser, timeout=10)
#     return wait
#
#
# def test_check_h1(browser):
#     browser.get("https://victoretc.github.io/selenium_waits/")
#     h1 = browser.find_element(By.TAG_NAME, 'h1')
#
#     assert h1.text == "Практика с ожиданиями в Selenium"
#
#
# def test_registration(browser, wait):
#     browser.get("https://victoretc.github.io/selenium_waits/")
#     btn = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))
#     btn.click()
#     login = browser.find_element(By.ID, "login").send_keys('login')
#     password = browser.find_element(By.ID, "password").send_keys('password')
#     agree = browser.find_element(By.ID, "agree").click()
#     register = browser.find_element(By.ID, "register").click()
#
#     # loader = wait.until(EC.visibility_of_element_located((By.ID, "loader")))
#     # text = wait.until(EC.visibility_of_element_located((By.ID, "successMessage")))
#     #
#     # print(loader)
#     # print(text)
#
#     assert wait.until(EC.visibility_of_element_located((By.ID, "loader"))).is_displayed()
#     assert wait.until(
#         EC.visibility_of_element_located((By.ID, "successMessage"))).text == "Вы успешно зарегистрированы!"
#
#
# # 2. С использованием Implicit waits
#
# def test_registration2(browser):
#     browser.implicitly_wait(10)
#     browser.get("https://victoretc.github.io/selenium_waits/")
#     btn = browser.find_element(By.ID, 'startTest')
#     btn.click()
#     login = browser.find_element(By.ID, "login").send_keys('login')
#     password = browser.find_element(By.ID, "password").send_keys('password')
#     agree = browser.find_element(By.ID, "agree").click()
#     register = browser.find_element(By.ID, "register").click()
#
#     assert browser.find_element(By.ID, "loader").is_displayed()
#     time.sleep(5)
#     assert browser.find_element(By.ID, "successMessage").text == "Вы успешно зарегистрированы!"

# def test_basic_auth1():
#     with webdriver.Chrome() as browser:
#         browser.get(f"http://admin:admin@the-internet.herokuapp.com/basic_auth")
#
#         assert browser.find_element(By.TAG_NAME, 'p').text == "Congratulations! You must have the proper credentials."

# def test_basic_auth2():
#     with webdriver.Chrome() as browser:
#         browser.get("https://the-internet.herokuapp.com/basic_auth")
#         time.sleep(2)
#         alert = browser.switch_to.alert()
#         time.sleep(5)
#         alert.send_keys("admin")
#         time.sleep(5)
#         alert.accept()
#
#         assert browser.find_element(By.TAG_NAME, 'p').text == "Congratulations! You must have the proper credentials."

# def test_broken_images():
#     with webdriver.Chrome() as browser:
#         browser.get("https://the-internet.herokuapp.com/broken_images")
#
#         image_list = browser.find_elements(By.TAG_NAME, "img")
#
#         for img in image_list:
#             response = requests.get(img.get_attribute('src'))
#             if (response.status_code != 200):
#                 print(img.get_attribute('outerHTML') + " is broken.")

# def test_add_delete_element():
#     with webdriver.Chrome() as browser:
#         browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
#         add_element = browser.find_element(By.XPATH, "//button[@onclick='addElement()']")
#         add_element.click()
#         time.sleep(2)
#         delete_element = browser.find_element(By.XPATH, "//button[@onclick='deleteElement()']")
#         delete_element.click()
#         time.sleep(2)
#
#         assert len(browser.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")) == 0

# registration PythonProject

# def test_check_registration():
#     with webdriver.Chrome() as browser:
#         browser.get("http://195.133.27.184/")
#
#         registration_btn = browser.find_element(By.XPATH, '//a[@href="/signup/"]')
#         registration_btn.click()
#
#         username = browser.find_element(By.ID, 'id_username').send_keys('usernameTest3')
#         password1 = browser.find_element(By.ID, 'id_password1').send_keys('12345test')
#         password2 = browser.find_element(By.ID, 'id_password2').send_keys('12345test')
#
#         submit_btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
#         submit_btn.click()
#
#         assert browser.find_element(By.XPATH, '//a[@href="/logout/"]').is_displayed()

def test_check_login(browser):
    # with webdriver.Chrome() as browser:
    browser.get(BASE_URL)
    login_btn = browser.find_element(LOGIN_BTN)
    login_btn.click()

    browser.find_element(*LOGIN_USERNAME).send_keys('usernameTest3')
    browser.find_element(*LOGIN_PASSWORD).send_keys('12345test')

    submit_btn = browser.find_element(*SUBMIT_BTN)
    submit_btn.click()

    assert browser.find_element(*LOGOUT_BTN).is_displayed()
