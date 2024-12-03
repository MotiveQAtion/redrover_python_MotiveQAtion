import time

from test_redrover.Katya_My.tests_tutors_web.conftest import driver
from test_redrover.Zarina.project.data.urls import *
from test_redrover.Zarina.project.locators.project_locators import *


class TestProject():
    def test_open(self,driver):
        driver.get(BASE_URL)

    def test_registration(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*REGISTRATION_BUTTON).click()
        driver.find_element(*REGISTRATION_USERNAME).send_keys('ZarUmb')
        driver.find_element(*REGISTRATION_PASSWORD1).send_keys('Miras110589')
        driver.find_element(*REGISTRATION_PASSWORD2).send_keys('Miras110589')
        driver.find_element(*SUBMIT_BUTTON).click()
        time.sleep(5)
        # assert driver.current_url == LOGIN_URL

