import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test1():
    driver.get("http://195.133.27.184/")
    url =driver.current_url
    assert url == "http://195.133.27.184/"


def test2():
    driver.get("http://195.133.27.184/")
    title = driver.title
    assert title == "Объявления"

def test3():
    driver.get("http://195.133.27.184/")
    locator = "(//div/a[@href='/list/'])[1]"
    check = driver.find_element(By.XPATH, locator)
    check.click()
    driver.back()
    driver.forward()
    driver.refresh()
    assert driver.current_url == "http://195.133.27.184/list/"









