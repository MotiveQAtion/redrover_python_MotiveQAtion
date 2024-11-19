from selenium.webdriver.common.by import By

username = (By.ID, 'id_username')
password1 = (By.ID, 'id_password1')
password2 = By.ID, 'id_password2'

LOGIN_USERNAME = By.ID, 'id_username'
LOGIN_PASSWORD = By.ID, 'id_password'
LOGIN_BTN = (By.XPATH, '//a[@href="/login/"]')
SUBMIT_BTN = By.XPATH, '//button[@type="submit"]'
LOGOUT_BTN = By.XPATH, '//a[@href="/logout/"]'

