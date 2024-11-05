import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from conftest import Zaya

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test_login_logout(Zaya):
    username_loc = "//*[@id='id_username']"
    password_loc = "//*[@id='id_password']"
    login_loc = "/html/body/main/div/div/div/form/button"
    username = "ZarinaUmb"
    password = "Miras110589"
    print()
    locator1 = "a[href='/login/']"
    driver.get("http://195.133.27.184/")
    time.sleep(2)
    print(f"Front page:{driver.current_url}")
    driver.find_element(By.CSS_SELECTOR, locator1).click()
    time.sleep(2)
    driver.find_element(By.XPATH, username_loc).send_keys(username)
    time.sleep(2)
    driver.find_element(By.XPATH, password_loc).send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, login_loc).click()
    time.sleep(2)
    locator2 = "a[href='/logout/']"
    driver.get("http://195.133.27.184/list/")
    time.sleep(2)
    print(f"Login page:{driver.current_url}")
    driver.find_element(By.CSS_SELECTOR, locator2).click()
    time.sleep(2)
    print(f"Front page:{driver.current_url}")
