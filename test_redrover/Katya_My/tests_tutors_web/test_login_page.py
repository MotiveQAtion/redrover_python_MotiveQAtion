import allure

from test_redrover.Katya_My.tests_tutors_web.locators import Login, TutorProfile
from test_redrover.Katya_My.tests_tutors_web.data import *
from test_redrover.Katya_My.tests_tutors_web.pages.page_login import LoginPage
from test_redrover.Katya_My.tests_tutors_web.config import WEB_USERNAME, WEB_PASSWORD, T_PASSWORD, T_NAME

# links
signup_link = "http://195.133.27.184/signup/"
login_link = "http://195.133.27.184/login/"
main_page_link = "http://195.133.27.184/list/"


@allure.title("Login_user")
def test_login_user(driver):
    login_page = LoginPage(driver)
    login_page.sign_in(WEB_USERNAME, WEB_PASSWORD)
    assert driver.current_url == main_page_link, 'Login Failed'


@allure.title("Login_tutor")
def test_login_tutor(driver):
    login_page = LoginPage(driver)
    login_page.sign_in(T_NAME, T_PASSWORD)
    btn_create_case = driver.find_elements(*TutorProfile.create_case)
    assert btn_create_case[0].is_displayed(), 'Login is Failed'


@allure.title('Incorrect password-user not found')
@allure.description('Positive test--MMS element is displayed')
def test_incorrect_password(driver, wait):
    login_page = LoginPage(driver)
    login_page.sign_in(WEB_USERNAME, incorrect_password)
    assert driver.current_url == main_page_link, 'User not found'


@allure.title('Incorrect login-MMS element is displayed')
@allure.description('Positive test--MMS element is displayed')
def test_incorrect_login_mms(driver, wait):
    login_page = LoginPage(driver)
    login_page.sign_in(incorrect_username, WEB_PASSWORD)
    element = driver.find_element(*Login.alert_mms).text
    assert element == mms_login_alert, "Alert MMS element is not displayed"
    assert driver.current_url == main_page_link, 'User not found'


def test_empty_filed_validation(driver, wait):
    login_page = LoginPage(driver)
    login_page.sign_in('', '')
    alert_mms_login = login_page.get_login_error_text()
    alert_mms_password = login_page.get_password_error_text()
    assert alert_mms_login == mms_empty_login, "The login error message is not as expected"
    assert alert_mms_password == mms_empty_password, "The password error message is not as expected"
