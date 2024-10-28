import pytest
import requests
from selenium import webdriver
from loguru import logger 

@pytest.fixture(scope="session")
def login():
    session = requests.Session()
    get_url = "http://195.133.27.184/1/"
    response = session.get(get_url)
    response.raise_for_status()

    csrf_token = session.cookies.get("csrftoken")

    login_url = "http://195.133.27.184/login/"
    login_data = {
        "username": "TestUser",
        "password": "Passwordfortestuser*",
        "csrfmiddlewaretoken": csrf_token,
    }

    logger.info("Собираем данные. ")
    
    login_response = session.post(login_url, data=login_data)
    login_response.raise_for_status()

    return {"csrftoken": csrf_token, "sessionid": session.cookies.get("sessionid")}


@pytest.fixture(scope="function")
def driver(login):
    driver = webdriver.Chrome()
    driver.get("http://195.133.27.184/")

    # Используем CSRF-токен и sessionid, полученные из фикстуры login
    driver.add_cookie(
        {
            "name": "csrftoken",
            "value": login["csrftoken"],
            "path": "/",
            "domain": "195.133.27.184",
        }
    )
    driver.add_cookie(
        {
            "name": "sessionid",
            "value": login["sessionid"],
            "path": "/",
            "domain": "195.133.27.184",
        }
    )

    driver.refresh()

    yield driver

    driver.quit()
