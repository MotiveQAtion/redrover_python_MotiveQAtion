import requests
from pprint import pprint

URL = "http://127.0.0.1:8000/testcases"


1 - GET
def read_cases():
    return requests.get(URL)

# 2 - POST
def create_test_case(data):  # Шаг 1. Создаем новый тест-кейс
    return requests.post(URL, json=data)

# 3 - GET - Read Test Case
def read_test_case(test_case_id):
    return requests.get(URL + f'/{test_case_id}')

# result = read_test_case(699)
# print(result.status_code)  # Выводим статус-код
# pprint(result.json())

# 4 - PUT - Update Case
def update_test_case(test_case_id, data2):
    return requests.put((URL + f'/{test_case_id}'), json=data2)

# 5 - DELETE - Delete Test Case

def delete_test_case(test_case_id):
    return requests.delete(URL + f'/{test_case_id}')