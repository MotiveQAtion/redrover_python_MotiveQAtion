import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


# 1. С использованием Explicit waits и Expected Conditions
@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options)
    return browser


@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, timeout=10)
    return wait


def test_check_h1(browser):
    browser.get("https://victoretc.github.io/selenium_waits/")
    h1 = browser.find_element(By.TAG_NAME, 'h1')

    assert h1.text == "Практика с ожиданиями в Selenium"


def test_registration(browser, wait):
    browser.get("https://victoretc.github.io/selenium_waits/")
    btn = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))
    btn.click()
    login = browser.find_element(By.ID, "login").send_keys('login')
    password = browser.find_element(By.ID, "password").send_keys('password')
    agree = browser.find_element(By.ID, "agree").click()
    register = browser.find_element(By.ID, "register").click()

    # loader = wait.until(EC.visibility_of_element_located((By.ID, "loader")))
    # text = wait.until(EC.visibility_of_element_located((By.ID, "successMessage")))
    #
    # print(loader)
    # print(text)

    assert wait.until(EC.visibility_of_element_located((By.ID, "loader"))).is_displayed()
    assert wait.until(
        EC.visibility_of_element_located((By.ID, "successMessage"))).text == "Вы успешно зарегистрированы!"


# 2. С использованием Implicit waits

def test_registration2(browser):
    browser.implicitly_wait(10)
    browser.get("https://victoretc.github.io/selenium_waits/")
    btn = browser.find_element(By.ID, 'startTest')
    btn.click()
    login = browser.find_element(By.ID, "login").send_keys('login')
    password = browser.find_element(By.ID, "password").send_keys('password')
    agree = browser.find_element(By.ID, "agree").click()
    register = browser.find_element(By.ID, "register").click()

    assert browser.find_element(By.ID, "loader").is_displayed()
    time.sleep(5)
    assert browser.find_element(By.ID, "successMessage").text == "Вы успешно зарегистрированы!"
