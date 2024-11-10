import os

import pytest
from selenium import webdriver


def setUp():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver



def base_URL():
    return "http://195.133.27.184/"


def username():
    return "Maddie11119"


def password():
    return "z6Imi3j33Z1g999F9"


def tutorName():
    return "Testov Test"


def fileAddress():
    #return "png.file"
     return "C:/Users/madinabonu.tosheva/Downloads/png.file.jpg"
