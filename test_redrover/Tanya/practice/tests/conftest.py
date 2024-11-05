import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1900,1000") - сразу открывает в  нужном размере окно
    # options.add_argument("--headless")
    # options.add_argument("--incognito")
    # options.add_argument("--disable-cache")
    # options.add_argument("--start-maximized")
    # options.add_argument("--ignore-certificate-errors")
    # options.page_load_strategy = 'normal'
    # options.page_load_strategy = 'eager'
    # options.page_load_strategy = 'none'
    driver = webdriver.Chrome(service=service, options=options)
    # driver.maximize_window() - не рекомендуется использовать
    yield driver