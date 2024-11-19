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


def test_check_title_h1(browser, wait):
    browser.get("https://victoretc.github.io/selenium_waits/")
    text_h1 = browser.find_element(By.XPATH, '//h1').text

    assert text_h1 == 'Практика с ожиданиями в Selenium'


def test_check_success_registration(browser, wait):
    browser.get("https://victoretc.github.io/selenium_waits/")
    button = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))
    button.click()
    browser.find_element(By.ID, "login").send_keys('login')
    browser.find_element(By.ID, "password").send_keys('password')
    browser.find_element(By.ID, "agree").click()
    browser.find_element(By.ID, "register").click()

    assert wait.until(EC.visibility_of_element_located((By.ID, "loader"))).is_displayed()
    assert wait.until(
        EC.visibility_of_element_located((By.ID, "successMessage"))).text == "Вы успешно зарегистрированы!"


# 2. С использованием Implicit waits

@pytest.fixture
def browser_imp(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_check_success_registration_2(browser_imp):
    browser_imp.get("https://victoretc.github.io/selenium_waits/")
    button = browser_imp.find_element(By.ID, 'startTest')
    button.click()
    browser_imp.find_element(By.ID, "login").send_keys('login')
    browser_imp.find_element(By.ID, "password").send_keys('password')
    browser_imp.find_element(By.ID, "agree").click()
    browser_imp.find_element(By.ID, "register").click()

    loader = browser_imp.find_element(By.ID, "loader")
    # success_message = browser_imp.find_element(By.ID, "successMessage")

    assert loader.is_displayed()
    # assert success_message.text == "Вы успешно зарегистрированы!"
