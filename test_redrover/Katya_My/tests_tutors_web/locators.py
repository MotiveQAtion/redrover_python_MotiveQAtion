from selenium.webdriver.common.by import By


# locators
class SignUp:
    username = By.ID, 'id_username'
    password = By.ID, 'id_password1'
    password_confirmation = By.ID, 'id_password2'
    submit_button = By.CSS_SELECTOR, '[type="submit"]'
    btn_logout = By.XPATH, '//a[@href="/logout/"]'


class Login:
    username = By.ID, 'id_username'
    password = By.ID, 'id_password'
    submit_button = By.CSS_SELECTOR, '[type="submit"]'
    title = By.XPATH, '//*[@class="welcome-section text-center bg-dark text-white py-5"]'
    alert_mms = By.XPATH, '//ul[@class="errorlist nonfield"]/li'
    alert_required_field_login = By.XPATH, "//div[@class='form-group']//li"
    alert_required_filed_password = By.XPATH, "//div[@class='form-group mt-3']//li"
