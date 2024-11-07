import requests

URL = "http://127.0.0.1:8000/testcases"

def read_test_case(test_case_id):
    return requests.get(URL + f'/{test_case_id}')

def delete_test_case(test_case_id):
    return requests.delete(URL + f'/{test_case_id}')

def create_test_case(data):
    return requests.post(URL, json=data)

def update_test_case(test_case_id, data2):
    return requests.put((URL + f'/{test_case_id}'), json=data2)

def test_create_test_case():
    data = {
        "id":25,
        "name": "Zaya",
        "description": "create test",
        "steps": [
            "to create first test"
        ],
        "expected_result": "test was created",
        "priority": "низкий"
    }

    test_case = create_test_case(data)  # создали test case
    test_case_id = test_case.json()['id']  # получили id

    # Проверка
    assert test_case.status_code == 200, "Код ответа 200!"  # Используем уже созданный test_case
    assert test_case_id == data['id']

def test_update_test_case():
    data1 = {
        "id": 25,
        "name": "Zaya",
        "description": "create test",
        "steps": [
            "to create first test"
        ],
        "expected_result": "test was created",
        "priority": "низкий"
    }

    data2 = {
        "id": 25,
        "name": "Zaya_update",
        "description": "create test",
        "steps": [
            "to create first test"
        ],
        "expected_result": "test was created",
        "priority": "высокий"
    }

    test_case = create_test_case(data1)  # создали test case
    test_case_id = test_case.json()['id']  # получили id
    update_case = update_test_case(test_case_id, data2) # обновили тест-кейс

    assert update_case.status_code == 200, "Код ответа 200!"
    assert update_case.json()['name'] == data2['name']

def test_delete_test_case():
    data = {
        "id": 25,
        "name": "Zaya_updated",
        "description": "create test",
        "steps": [
            "to create first test"
        ],
        "expected_result": "test was created",
        "priority": "низкий"
    }

    test_case = create_test_case(data)  # создали test case
    test_case_id = test_case.json()['id']  # получили id

    assert delete_test_case(test_case_id).status_code == 200, "Код ответа 200!"
