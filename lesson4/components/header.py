from selene import by, be, have, browser
from core.settings import settings


def visit():
    browser.open('/')


def should_be_opened():
    browser.should(have.url(settings.base_url))


def open_registration_component():
    browser.element(by.text('Регистрация')).click()


def create_post_button_should_be_visible():
    browser.element(by.text('Создать объявление')).should(be.visible)
