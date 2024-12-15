from test_redrover.EgorAlekhno.hw1 import functions as func
from pprint import pprint


def test_get_all_test_cases():
    response = func.get_all_test_cases()

    assert response.status_code == 200, "Код статуса не равен 200!"


def test_create_test_case():
    data = {
        "id": 0,
        "name": "Egor",
        "description": "description",
        "steps": [
            "step1",
            " step 2"
        ],
        "expected_result": "expected result",
        "priority": "высокий"
    }

    # Создаем test case и получаем его id из ответа
    created_test_case = func.create_test_case(data)

    pprint(created_test_case.json())

    id_ = created_test_case.json()["id"]
    print(f'id: {id_}')

    # Получаем наш test case по его id
    response = func.get_test_cases_by_id(id_)
    response_data = response.json()

    print(response_data)

    # assert response_data["name"] == data["name"]
    # assert response_data["priority"] == data["priority"]
    assert response_data["description"] == data["description"]