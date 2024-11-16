import allure
import pytest
import logging

from test_redrover.Katya_My.tests_tutors_web.locators import SignUp, TutorProfile
from test_redrover.Katya_My.tests_tutors_web.pages.registration_page import fill_signup_form
from test_redrover.Katya_My.tests_tutors_web.config import WEB_USERNAME, WEB_PASSWORD, T_PASSWORD, T_NAME
from test_redrover.Katya_My.tests_tutors_web.data import *


# Настроим логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# links
signup_link = "http://195.133.27.184/signup/"
login_link = "http://195.133.27.184/login/"
main_page_link = "http://195.133.27.184/list/"


@allure.title("Create account for user")
def test_create_acc_user(driver, wait):
    fill_signup_form(driver, username=WEB_USERNAME, password=WEB_PASSWORD)
    error_msg_elements = driver.find_elements(*SignUp.error_msg)
    # Checking if an error message appears
    if error_msg_elements and mms_error in error_msg_elements[0].text:
        assert True, f"User {WEB_USERNAME} is already registered."
    else:
        # If there is no error message, check for successful registration
        btn_out = driver.find_elements(*SignUp.btn_logout)
        assert btn_out[0].is_displayed(), 'Registration is failed'


@allure.title("Create account for teacher")
def test_create_acc_teacher(driver, wait):
    fill_signup_form(driver, username=T_NAME, password=T_PASSWORD, check_terms=True)
    error_msg_elements = driver.find_elements(*SignUp.error_msg)
    if error_msg_elements:
        # If the error message is related to an existing user, skip the test
        if mms_error in error_msg_elements[0].text:
            logger.info(f"User {T_NAME} is already registered.")
            pytest.skip(f"User {T_NAME} already exists.")
        else:
            # If other mistake check mmg
            assert mms_error in error_msg_elements[0].text, f"Unexpected error message: {error_msg_elements[0].text}"
    else:
        # If there is no error, check successful registration
        btn_out = driver.find_elements(*SignUp.btn_logout)
        assert btn_out[0].is_displayed(), 'Registration is failed'
