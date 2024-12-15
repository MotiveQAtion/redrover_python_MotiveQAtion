import requests


# URL = "http://localhost:5173/"
URL = "http://localhost:8000/testcases/"


def get_all_test_cases():
    """
    Делает GET запрос и возвращает id всех бронирований.

    :return: Response, объект с ответом сервера
    """

    return requests.get(URL)


def create_test_case(data):


    return requests.post(URL, json=data)


def get_test_cases_by_id(id_):
    """
    Делает GET запрос и возвращает бронирование по его id.

    :param id_: int, id бронирования
    :return: Response, объект с ответом сервера
    """

    return requests.get(URL + f"/{id_}")