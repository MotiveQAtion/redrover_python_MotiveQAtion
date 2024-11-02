import time
from selenium.webdriver.common.by import By
from lib2to3.fixes.fix_input import context

def test_ui(driver):
    driver.get("https://the-internet.herokuapp.com/")
    # driver.get("https://expired.badssl.com/")
    time.sleep(5)

def test_strategy(driver):
    print()
    start_time = time.time()
    driver.get("https://letcode.in/test")
    end_time = time.time()
    print(f"Time: {end_time - start_time}")

def test(driver):
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(5)

def test1(driver):
    print()
    locator = "ul>li:first-child>a"
    locator1 = "a[href='/abtest']"
    locator2 = "//a[@href='/abtest']"
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)
    print(f"Front page:{driver.current_url}")
    driver.find_element(By.XPATH, locator2).click()
    time.sleep(2)
    print(f"AB test:{driver.current_url}")
    driver.back()
    print(f"Front page:{driver.current_url}")
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    print(f"AB test:{driver.current_url}")
    driver.refresh()

def test2(driver):
    print()
    driver.get("https://the-internet.herokuapp.com/")
    url =driver.current_url
    print(url)
    assert url == "https://the-internet.herokuapp.com/"
    title = driver.title
    print(title)
    assert title == "The Internet"

def test3(driver):
    username_loc = "input[data-test='username']"
    password_loc = "input[data-test='password']"
    login_loc = "input[data-test='login-button']"
    username = "standard_user"
    password = "secret_sauce"
    check_url = "https://www.saucedemo.com/inventory.html"
    check_title = "Swag Labs"
    driver.get("https://www.saucedemo.com")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, username_loc).send_keys(username)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, password_loc).send_keys(password)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, login_loc).click()
    time.sleep(2)
    assert driver.title == check_title
    assert driver.current_url == check_url

def test4(driver):
    locator = "div[id='selectable']"
    driver.get("https://letcode.in/selectable")
    context = driver.find_elements(By.CSS_SELECTOR, locator)
    for i in context:
        if i.text == "Appium":
            print(i.text)
            i.click()
            time.sleep(2)
            break
    print(context)