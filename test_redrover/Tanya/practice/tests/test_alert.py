import allure

from test_redrover.Tanya.practice.data.urls import Urls
from test_redrover.Tanya.practice.pages.alert_page import AlertPage
import pytest


class TestAlert:
    url = Urls()

    # @allure.title("Alert")
    def test_alert1(self, browser):
        page = AlertPage(browser, f"{self.url.herokuapp_base_url}javascript_alerts")
        page.open()
        alert_text = page.alert()
        assert alert_text == "I am a JS Alert"

    def test_alert2(self, browser):
        page = AlertPage(browser, f"{self.url.herokuapp_base_url}javascript_alerts")
        page.open()
        page.alert()
        text = page.get_text()
        assert text == "You successfully clicked an alert"

    @pytest.mark.parametrize("value", [("YES", "Ok"), ("NO", "Cancel")])
    def test_alert_confirm1(self, browser, value):
        page = AlertPage(browser, f"{self.url.herokuapp_base_url}javascript_alerts")
        page.open()
        page.alert_confirm(value[0])
        text = page.get_text()
        assert text == f"You clicked: {value[1]}"

    def test_alert_confirm2(self, browser):
        page = AlertPage(browser, f"{self.url.herokuapp_base_url}javascript_alerts")
        page.open()
        text = page.alert_confirm("YES")
        assert text == "I am a JS Confirm"

    def test_alert_prompt1(self, browser):
        page = AlertPage(browser, f"{self.url.herokuapp_base_url}javascript_alerts")
        page.open()
        text = page.alert_prompt("Hello")
        assert text == "I am a JS prompt"

    def test_alert_prompt2(self, browser):
        page = AlertPage(browser, f"{self.url.herokuapp_base_url}javascript_alerts")
        page.open()
        page.alert_prompt("Hello")
        text = page.get_text()
        assert text == f"You entered: Hello"

