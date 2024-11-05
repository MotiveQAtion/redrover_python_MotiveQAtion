from test_redrover.Tanya.practice import func_HW1 as func


# 1 - GET - Read Cases
# def test_read_cases():
#     assert func.read_cases().status_code == 200, "Код ответа 200!"


# 2 - POST - Create Test Case

def test_create_test_case():
    data = {
        "id": 10,
        "name": "Tanya_test",
        "description": "crate test",
        "steps": [
            "to crate test"
        ],
        "expected_result": "test was created",
        "priority": "низкий"
    }

    test_case = func.create_test_case(data)  # создали test case
    test_case_id = test_case.json()['id']  # получили id

    # Проверка
    assert test_case.status_code == 200, "Код ответа 200!"  # Используем уже созданный test_case
    assert test_case_id == data['id'] # проверяем равны ли id

# 3 - GET - Read Test Case
def test_read_test_case():
    data = {
        "id": 11,
        "name": "Tanya_test",
        "description": "crate test",
        "steps": [
            "to crate test"
        ],
        "expected_result": "test was created",
        "priority": "низкий"
    }

    test_case = func.create_test_case(data)  # создали test case
    test_case_id = test_case.json()['id']  # получили id
    check_by_id = func.read_test_case(test_case_id) # отправили запрос по id

    assert check_by_id.status_code == 200, "Код ответа 200!"

# 4 - PUT - Update Case
def test_update_test_case():
    data1 = {
        "id": 11,
        "name": "Tanya_test",
        "description": "crate test",
        "steps": [
            "to crate test"
        ],
        "expected_result": "test was created",
        "priority": "низкий"
    }

    data2 = {
        "id": 11,
        "name": "Tanya_update",
        "description": "crate test",
        "steps": [
            "to crate test"
        ],
        "expected_result": "test was created",
        "priority": "высокий"
    }

    test_case = func.create_test_case(data1)  # создали test case
    test_case_id = test_case.json()['id']  # получили id
    update_case = func.update_test_case(test_case_id, data2) # обновили тест-кейс

    assert update_case.status_code == 200, "Код ответа 200!"
    assert update_case.json()['name'] == data2['name']

# 5 - DELETE - Delete Test Case
def test_delete_test_case():
    data = {
        "id": 11,
        "name": "Tanya_test",
        "description": "crate test",
        "steps": [
            "to crate test"
        ],
        "expected_result": "test was created",
        "priority": "низкий"
    }

    test_case = func.create_test_case(data)  # создали test case
    test_case_id = test_case.json()['id']  # получили id

    assert func.delete_test_case(test_case_id).status_code == 200, "Код ответа 200!"