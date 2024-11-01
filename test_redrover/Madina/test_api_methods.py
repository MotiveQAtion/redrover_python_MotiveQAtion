from http.client import responses

import requests
import functions
from test_redrover.Madina.functions import create_test, read_test, update_test, delete_test


def test_create_test():
    info = {
         "id": 123,
         "name": "Alex",
         "description": "Testing post method",
         "steps": [
            "1. Open the browser",
            "2. Enter the question",
            "3. Click the search button"
         ],
         "expected_result": "You got the response",
         "priority": "средний"
         }

    response = create_test(info)
    assert response.status_code == 200, f"Unexpected status code - {response.status_code}"


def test_read_test():
    info = {
        "id": 123,
        "name": "Alex",
        "description": "Testing get method",
        "steps": [
            "1. Open the browser",
            "2. Enter the question",
            "3. Click the search button"
        ],
        "expected_result": "You got the response",
        "priority": "средний"
    }

    response = create_test(info)
    test_case_id = response.json()['id']

    response2 = read_test(test_case_id)
    response_id = response2.json()['id']

    assert response_id == test_case_id, f"Unexpected result - {response_id}"


def test_update_test():

    info = {
         "id": 234,
         "name": "Alex",
         "description": "Testing update method",
         "steps": [
            "1. Open the browser",
            "2. Enter the question",
            "3. Click the search button"
         ],
         "expected_result": "You got the response",
         "priority": "средний"
         }

    info2 = {
        "id": 234,
        "name": "Alex - 2",
        "description": "Testing update method",
        "steps": [
            "1. Open the browser",
            "2. Enter the question",
            "3. Click the search button"
        ],
        "expected_result": "You got the response",
        "priority": "высокий"
    }

    response = create_test(info)
    test_case_id = response.json()['id']

    response2 = update_test(test_case_id, info2)
    assert response2.status_code == 200, f"Unexpected status code - {response.status_code}"
    assert response2.json()['name'] == info2['name'], f"Unsuccessful update - {response2.json()['name']}"


def test_delete_test():
    info = {
        "id": 123,
        "name": "Alex",
        "description": "Testing delete method",
        "steps": [
            "1. Open the browser",
            "2. Enter the question",
            "3. Click into search button"
        ],
        "expected_result": "You got the response",
        "priority": "средний"
    }

    response = create_test(info)
    test_case_id = response.json()['id']

    response2 = delete_test(test_case_id)
    assert response2.status_code == 200, f"Unexpected status code - {response.status_code}"
    assert response2.json()['detail'] == "Test case deleted.", "it is not deleted"








