import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
def test1():
    print()
    locator1 = "a[href='/blog/']"
    locator2 = "/html/body/main/div/div[2]/div[1]/div/div/a"
    driver.get("http://195.133.27.184/")
    time.sleep(2)
    print(f"Front page:{driver.current_url}")
    driver.find_element(By.CSS_SELECTOR, locator1).click()
    time.sleep(2)
    print(f"BLOG:{driver.current_url}")
    driver.find_element(By.XPATH, locator2).click()
    time.sleep(2)
    print(f"Read:{driver.current_url}")
    driver.back()
    print(f"BLOG:{driver.current_url}")
    time.sleep(2)
    driver.back()
    print(f"Front page:{driver.current_url}")
    time.sleep(5)