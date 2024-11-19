from playwright.sync_api import Page, expect
from core.data import base_url
import allure


class Register:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем компонент регистрации")
    def should_be_opened(self):
        expect(self.page).to_have_url(f"{base_url}/signup/")

    @allure.step("Заполняем поле никнейм")
    def fill_nick(self, nick):
        self.page.get_by_placeholder("Придумайте никнейм").fill(nick)

    @allure.step("Заполняем поле пароль")
    def fill_password(self, password):
        self.page.get_by_placeholder("Придумайте пароль").fill(password)

    @allure.step("Заполняем поле подтверждения пароля")
    def fill_confirm_password(self, password):
        self.page.get_by_placeholder("Подтвердите пароль").fill(password)

    @allure.step("Нажимаем на кнопку стать учителем")
    def click_on_become_a_teacher_button(self):
        self.page.locator("#id_is_tutor").check()

    @allure.step("Нажимаем на кнопку регистрации")
    def click_on_registration_button(self):
        self.page.get_by_test_id("submit-button").click()