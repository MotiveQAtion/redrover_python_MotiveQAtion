import pytest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://victoretc.github.io/selenium_waits/')
    driver.refresh()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

