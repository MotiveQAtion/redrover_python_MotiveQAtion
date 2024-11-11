from selene import be, have, browser


def visit():
    browser.open('/signup/')


def should_be_opened():
    browser.should(have.url('/signup/'))


def type_login(login):
    browser.element('#id_username').type(login)


def type_password(password):
    browser.element('#id_password1').type(password)


def type_confirm_password(password):
    browser.element('#id_password2').type(password)


def choose_tutor_role():
    checkbox = browser.element('#id_is_tutor')
    checkbox.click()
    checkbox.should(be.selected)


def click_register_button():
    browser.element('button[type="submit"]').click()
