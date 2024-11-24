import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1900,1000")
    # options.add_argument("--headless")
    # options.add_argument("--incognito")
    # options.add_argument("--disable-cache")
    # options.add_argument("--start-maximized")
    # options.page_load_strategy = 'normal'
    # options.page_load_strategy = 'eager'
    # options.page_load_strategy = 'none'
    # options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(service=service, options=options)
    # driver.set_window_size(1600,900)
    # driver.maximize_window()
    yield driver
    driver.quit()