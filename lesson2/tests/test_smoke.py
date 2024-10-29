from selenium.webdriver.common.by import By


def test_check_profile_button(driver):
    driver.find_element(By.XPATH, "//a[@href='/profile/']").click()


def test_check_create_post(driver):
    driver.find_element(By.LINK_TEXT, "Создать объявление").click()
    driver.find_element(By.XPATH, "//button[text()='Создать']").is_displayed()
