import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from test_redrover.Tanya.practice.functions import get_root_path

download_path = get_root_path("data/download")

@pytest.fixture()
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_path
    }
    options.add_argument("--window-size=1600,1000")
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--headless")
    # options.add_argument("--incognito")
    # options.add_argument("--disable-cache")
    # options.add_argument("--start-maximized")
    # options.add_argument("--ignore-certificate-errors")
    # options.page_load_strategy = 'normal'
    # options.page_load_strategy = 'eager'
    # options.page_load_strategy = 'none'
    browser = webdriver.Chrome(service=service, options=options)
    # driver.maximize_window() - не рекомендуется использовать
    yield browser
    browser.quit()
