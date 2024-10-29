from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check_heading():
    with webdriver.Chrome() as browser:
        browser.get("http://195.133.27.184/")

        heading = browser.find_element(By.XPATH, "//h1").text

        assert heading == "Добро пожаловать на нашу платформу!"