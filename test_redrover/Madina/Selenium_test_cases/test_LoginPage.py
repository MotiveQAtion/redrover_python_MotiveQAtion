from selenium import webdriver
from selenium.webdriver.common.by import By
import time



from LoginPage import *
from conftest import *



def test_create_account():
    driver = setUp()
    driver.get(base_URL())

    goToSignupPage(driver)
    title = driver.find_element(By.XPATH, "//h1[contains(text(),'Регистрация')]")
    assert title.is_displayed()

    setUserName(driver, username())
    setPassword(driver, password())
    setConfirmPassword(driver, password())
    clickCheckbox(driver)
    clickSubmit(driver)
    announcementsPage(driver)


def test_enter_as_an_authorized_account():
    driver = setUp()
    driver.get(base_URL())

    goToLoginPage(driver)
    title2 = driver.find_element(By.XPATH, "//h1[contains(text(),'Вход')]")
    assert title2.is_displayed()

    setUserName(driver, username())
    setLoginPassword(driver, password())
    clickSubmit(driver)
    announcementsPage(driver)
    return driver

def test_create_new_item():

     driver = test_enter_as_an_authorized_account()

     goToCreatePage(driver)
     setTutorsFullName(driver, tutorName())
     setDescription(driver)
     uploadFile(driver, fileAddress())
     time.sleep(2)
     chooseCategories(driver)
     setExperience(driver)
     setPrice(driver)
     clickSubmit(driver)
     time.sleep(2)

     title3 = driver.find_element(By.XPATH, "//div/h5[contains(text(),'Testov Test')]")
     assert title3.is_displayed()
















