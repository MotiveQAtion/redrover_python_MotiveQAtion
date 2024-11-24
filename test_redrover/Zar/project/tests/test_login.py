import time
from test_redrover.Zar.project.data.urls import *
from test_redrover.Zar.project.locators.project_locators import *


class TestLogin:
    def test_login(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*LOGIN_BTN).click()
        driver.find_element(*LOGIN_USERNAME).send_keys('ZarUmb')
        driver.find_element(*LOGIN_PASSWORD).send_keys('Miras110589')
        driver.find_element(*SUBMIT_LOGIN_BUTTON).click()
        time.sleep(5)
        assert driver.current_url == LOGIN_URL