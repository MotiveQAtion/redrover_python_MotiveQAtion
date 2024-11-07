import allure
from test_redrover.Katya_My.tests_tutors_web.locators import SignUp


# links
signup_link = "http://195.133.27.184/signup/"
login_link = "http://195.133.27.184/login/"
main_page_link = "http://195.133.27.184/list/"


@allure.title("Create account and login")
def test_create_acc(driver, wait):
    driver.get(signup_link)
    driver.find_element(*SignUp.username).send_keys("TestUser_1")
    driver.find_element(*SignUp.password).send_keys("test5test78")
    driver.find_element(*SignUp.password_confirmation).send_keys("test5test78")
    driver.find_element(*SignUp.submit_button).click()
    btn_out = driver.find_elements(*SignUp.btn_logout)
    # assert len(btn_out) == 1, 'Registration is failed'
    assert btn_out[0].is_displayed(), 'Registration is failed'





