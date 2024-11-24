from selenium.webdriver.common.by import By


REGISTRATION_BUTTON = By.XPATH, '//a[@href="/signup/"]'
REGISTRATION_USERNAME = By.ID, 'id_username'
REGISTRATION_PASSWORD1 = By.ID, 'id_password1'
REGISTRATION_PASSWORD2 = By.ID, 'id_password2'
SUBMIT_BUTTON = By.XPATH, '//button[@type="submit"]'
LOGIN_BTN = By.XPATH, '//a[@href="/login/"]'
LOGIN_USERNAME = By.ID, 'id_username'
LOGIN_PASSWORD = By.ID, 'id_password'
SUBMIT_LOGIN_BUTTON = By.XPATH, '//button[@type="submit"]'