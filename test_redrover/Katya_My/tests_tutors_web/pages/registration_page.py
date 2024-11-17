from test_redrover.Katya_My.tests_tutors_web.locators import SignUp, TutorProfile
import time
signup_link = "http://195.133.27.184/signup/"


def fill_signup_form(driver, username, password, check_terms=False):
    driver.get(signup_link)
    driver.find_element(*SignUp.username).send_keys(username)
    driver.find_element(*SignUp.password).send_keys(password)
    driver.find_element(*SignUp.password_confirmation).send_keys(password)
    if check_terms:
        driver.find_element(*SignUp.checkbox).click()
    driver.find_element(*SignUp.submit_button).click()


