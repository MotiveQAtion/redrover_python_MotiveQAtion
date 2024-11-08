from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from test_LoginPage import *

signup_button = '//div//a[@href="/signup/"]'
login_textbox = '//div/input[@id = "id_username"]'
password_textbox = '//div/input[@id = "id_password1"]'
confirm_password_textbox = '//div/input[@id = "id_password2"]'
submit_button = '//button[@type = "submit"]'
checkbox_button = '//div/input[@id="id_is_tutor"]'
announcements = '//div[@class="col-md-4 col-sm-6"]'

login_button = '//div//a[@href="/login/"]'
login_password_textbox = '//div/input[@id = "id_password"]'

create_advertisement_button = '//div//a[@href="/create/"]'
tutor_name_textbox = '//div/input[@id = "id_name"]'
upload_file_button = '//div//input[@id = "photo"]'
categories_dropdown = '//div//select[@id="id_category"]/option[@value =3]'
experience_textbox = '//div/input[@id = "id_years_of_experience"]'
price_textbox = '//div/input[@id = "id_price"]'
description_textbox = '//div/textarea[@id="id_description"]'


#################### SignUp Methods #################

def goToSignupPage(driver):
    driver.find_element(By.XPATH, signup_button).click()

def setUserName(driver, username):
    driver.find_element(By.XPATH, login_textbox).send_keys(username)


def setPassword(driver,password):
    driver.find_element(By.XPATH, password_textbox).send_keys(password)


def setConfirmPassword(driver,password):
    driver.find_element(By.XPATH,confirm_password_textbox).send_keys(password)

def clickCheckbox(driver):
    driver.find_element(By.XPATH, checkbox_button).click()

def clickSubmit(driver):
    driver.find_element(By.XPATH, submit_button).click()

def  announcementsPage (driver):
    page = driver.find_element(By.XPATH, announcements)
    if page.is_displayed():
       print("Login successfuly done")
    else:
        print("Could not login")


#################### Login Methods #################

def goToLoginPage(driver):
    driver.find_element(By.XPATH, login_button).click()

def setLoginPassword(driver,password):
    driver.find_element(By.XPATH, login_password_textbox).send_keys(password)



#################### Create Advertisement Methods #################

def goToCreatePage(driver):
    driver.find_element(By.XPATH, create_advertisement_button).click()

def setTutorsFullName(driver, tutorName):
    driver.find_element(By.XPATH, tutor_name_textbox).send_keys(tutorName)

def setDescription(driver):
    driver.find_element(By.XPATH, description_textbox).send_keys("Your future math teacher")

def uploadFile(driver, fileAddress):
    driver.find_element(By.XPATH, upload_file_button).send_keys(fileAddress)

def chooseCategories(driver):
    driver.find_element(By.XPATH, categories_dropdown).click()

def setExperience(driver):
    driver.find_element(By.XPATH, experience_textbox).send_keys(13)

def setPrice(driver):
    driver.find_element(By.XPATH, price_textbox).send_keys(1000)









