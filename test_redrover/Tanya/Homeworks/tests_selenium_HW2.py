import time

def test(driver):
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(5)


def test1(driver):
    locator_css = "ul>li:first-child>a"
    locator_xpath = "//a[@href='/abtest']"
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)
    driver.find_element("xpath", locator_xpath).click()
    time.sleep(5)


def test2(driver):
    username_loc = "input[data-test='username']"
    password_loc = "input[data-test='password']"
    login_btn_loc = "input[data-test='login-button']"
    username = "standard_user"
    password = "secret_sauce"
    driver.get("https://www.saucedemo.com")
    time.sleep(2)
    driver.find_element("css selector", username_loc).send_keys(username)
    time.sleep(2)
    driver.find_element("css selector", password_loc).send_keys(password)
    time.sleep(2)
    driver.find_element("css selector", login_btn_loc).click()
    time.sleep(2)


def test3(driver):
    locator = "div[id='selectable']"
    driver.get("https://letcode.in/selectable")
    context = driver.find_elements("css selector", locator)
    for i in context:
        if i.text == 'Appium':
            i.click()
            time.sleep(2)
            break
