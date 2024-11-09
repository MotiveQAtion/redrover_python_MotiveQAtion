from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_expected_conditions(driver, wait):
    title_page = driver.find_element(By.TAG_NAME, 'h1').text
    assert title_page == 'Практика с ожиданиями в Selenium'

    wait.until(EC.visibility_of_element_located((By.ID, 'startTest'))).click()
    driver.find_element(By.ID, 'login').send_keys('login')
    driver.find_element(By.ID, 'password').send_keys('password')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()

    loader_btn = wait.until(EC.visibility_of_element_located((By.ID, 'loader')))
    assert loader_btn.is_displayed()

    mms = wait.until(EC.visibility_of_element_located((By.ID, 'successMessage'))).text
    assert mms == 'Вы успешно зарегистрированы!'


def test_implicit_wait(driver):
    driver.implicitly_wait(10)
    title_page = driver.find_element(By.TAG_NAME, 'h1').text
    assert title_page == 'Практика с ожиданиями в Selenium'

    driver.find_element(By.ID, 'startTest').click()
    driver.find_element(By.ID, 'login').send_keys('login')
    driver.find_element(By.ID, 'password').send_keys('password')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()

    loader_btn = driver.find_element(By.ID, 'loader')
    assert loader_btn.is_displayed()

    """В этом случае, неявное ожидание (implicitly_wait) не сработало на последнем элементе (successMessage) 
    потому что оно ждало только того, что элемент будет найден, но не ждало того, что текст элемента будет доступен."""
    # mms_0 = driver.find_element(By.ID, 'successMessage').text

    """Если вы хотите получить только текстовое содержимое элемента, 
        без HTML - тегов и атрибутов, используйте  get_attribute('textContent')"""

    mms = driver.find_element(By.ID, 'successMessage')
    assert mms.get_attribute('textContent') == 'Вы успешно зарегистрированы!'

    # assert mms.get_attribute('innerHTML') == 'Вы успешно зарегистрированы!'
