import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver,timeout =10)
    return wait


def test_is_h1_named_practica(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")
    assert driver.find_element(By.XPATH, "//h1").text == "Практика с ожиданиями в Selenium"

def test_visible_loading_sing(driver, wait):
    driver.get("https://victoretc.github.io/selenium_waits/")

    visible_after_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']")))
    visible_after_button.click()
    driver.find_element(By.XPATH, "//*[@id='login']").send_keys("login")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("password")
    driver.find_element(By.XPATH, "//*[@id='agree']").click()
    driver.find_element(By.XPATH, "//*[@id='register']").click()

    assert wait.until(EC.visibility_of_element_located((By.ID, "loader"))).is_displayed()

def test_visible_loading_message(driver, wait):
    driver.get("https://victoretc.github.io/selenium_waits/")

    visible_after_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='startTest']")))
    visible_after_button.click()
    driver.find_element(By.XPATH, "//*[@id='login']").send_keys("login")
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("password")
    driver.find_element(By.XPATH, "//*[@id='agree']").click()
    driver.find_element(By.XPATH, "//*[@id='register']").click()

    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='successMessage']")))
