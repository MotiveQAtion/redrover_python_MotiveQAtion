import requests
import func as func

URL = "http://127.0.0.1:8000/testcases"

def test_create_test_case():
    data ={
        "id": 16,
        "name": "Test1",
        "description": "new test",
        "steps": [
            "to create test"
        ],
        "expected_result": "created test",
        "priority": "низкий"
    }
    test_case = requests.post(URL, json=data)

    assert test_case.status_code == 200

    test_case_id = test_case.json()['id']
    print(test_case_id)

    assert test_case.status_code == 200
    assert test_case_id == data['id']


def test_negative():
    data = {
        "id": 10
    }

    test_case = requests.post(URL, json=data)

    assert test_case.status_code == 422, "Код ответа 422!"

def test_get_case():
    assert func.get_case().status_code == 200





