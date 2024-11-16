import time
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from test_redrover.Katya_My.tests_the_internet_web.locators import *
from test_redrover.Katya_My.tests_the_internet_web.data import *


def test_add_remove_elements(driver, wait):
    driver.find_element(*add_delete_menu_btn).click()
    driver.find_element(*add_btn).click()
    driver.find_element(*delete_btn).click()
    try:
        # Try to find the delete button again
        driver.find_element(*delete_btn)
        # If it still exists, the test should fail
        assert False, 'element not deleted'
    except NoSuchElementException:
        # If NoSuchElementException is raised, the element has been deleted
        pass

    assert not driver.find_elements(*delete_btn), 'Unexpected element found on the page.'


def test_basic_auth(driver, wait):
    driver.find_element(*btn_auth).click()
    driver.get(url)
    mms_reg = driver.find_element(*mms_registration).text
    assert mms_reg == "Congratulations! You must have the proper credentials."
    #  Проверка-страница полностью прогрузилась
    assert driver.execute_script("return document.readyState;") == "complete", "Page did not load completely."


def test_check_broken_images(driver, wait):
    driver.find_element(*broken_btn_menu).click()
    # Находим все изображения на странице
    images = driver.find_elements(By.TAG_NAME, "img")

    for image in images:
        src = image.get_attribute("src")
        if src:  # Проверяем, если у изображения есть ссылка
            response = requests.head(src)  # Отправляем запрос HEAD
            # (позволяет получить только заголовки ответа от сервера,
            # без тела содержимого. Это полезно для того, чтобы узнать
            # метаинформацию о ресурсе, например, его статус или размер, не загружая сам файл.)
            if response.status_code != 200:
                print(f"Broken image found: {src} (Status: {response.status_code})")
                # эта проверка - если есть сломанные изображения, то тест падает
                # assert False, f"Broken image found: {src} (Status: {response.status_code})"


def test_checkbox(driver, wait):
    driver.find_element(*checkbox_menu).click()
    checkboxes = driver.find_elements(*check_box_btn_1)
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()  # Выбираем, если не выбрано
        else:
            checkbox.click()


def test_checkbox_second(driver, wait):
    driver.find_element(*checkbox_menu).click()
    checkboxes = driver.find_elements(*check_box_btn_1)
    for checkbox in checkboxes:
        initial_state = checkbox.is_selected()
        checkbox.click()
        assert checkbox.is_selected() != initial_state, "The checkbox state has not changed"
