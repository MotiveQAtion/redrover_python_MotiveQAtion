import os
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.refresh()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=100)
    return wait


@pytest.fixture(scope="session", autouse=True)
def clear_cache():
    yield
    # Очистка кэша после всех тестов
    cache_dir = 'path/to/cache'
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
