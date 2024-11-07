from test_redrover.Katya_My.tests_tutors_web.locators import Login

login_link = "http://195.133.27.184/login/"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def sign_in(self, username, password):
        self.driver.get(login_link)
        title = self.driver.find_element(*Login.title)
        assert title.is_displayed(), 'Page Incorrect'
        self.driver.find_element(*Login.username).send_keys(username)
        self.driver.find_element(*Login.password).send_keys(password)
        self.driver.find_element(*Login.submit_button).click()

    def get_login_error_text(self):
        return self.driver.find_element(*Login.alert_required_field_login).text

    def get_password_error_text(self):
        return self.driver.find_element(*Login.alert_required_filed_password).text
