import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.alert import Alert
import pytest


# def test_broken_image():
#     with webdriver.Chrome() as browser:
#         browser.get("https://the-internet.herokuapp.com/broken_images")
#         image_list = browser.find_elements(By.TAG_NAME, 'img')
#
#         for img in image_list:
#             response = requests.get(img.get_attribute('src'))
#             if (response.status_code != 200):
#                 print(img.get_attribute('outerHTML') + " - broken")


def test_add_delete_element():
    with webdriver.Chrome() as browser:
        browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
        add_element = browser.find_element(By.XPATH, '//button[@onclick="addElement()"]')
        add_element.click()
        delete_element = browser.find_element(By.XPATH, '//button[@onclick="deleteElement()"]')
        delete_element.click()

        assert len(browser.find_elements(By.XPATH, '//div[@onclick="deleteElement()"]')) == 0