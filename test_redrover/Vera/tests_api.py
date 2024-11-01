import requests

from test_redrover.Vera.utils import validate_json_schema, get_id_of_created_case
from test_redrover.Vera.json_schemas import *


def test_post_case_all_fields_fullfiled_200_created(case_data, base_url, path):
    payload = case_data.dict()
    response = requests.post(f"{base_url}/{path}/", json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json().get("name") == case_data.name, f"Case name does not match"
    assert response.json().get("priority") == case_data.priority.value, "Case priority does not match"

    response_data = response.json()
    validate_json_schema(response_data, post_response_schema)

    assert response_data["name"] == case_data.name, "Case name does not match"
    assert response_data["priority"] == case_data.priority.value, "Case priority does not match"


def test_get_case_200_ok(case_data, base_url, path):
    case_id = get_id_of_created_case(case_data, base_url, path)
    response = requests.get(f"{base_url}/{path}/{case_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json()["id"] == case_id
    response_data = response.json()
    validate_json_schema(response_data, get_by_id_json_schema)


def test_delete_case_200_ok(case_data, base_url, path):
    case_id = get_id_of_created_case(case_data, base_url, path)
    response = requests.delete(f"{base_url}/{path}/{case_id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_data = response.json()
    validate_json_schema(response_data, delete_response_schema)


def test_post_empty_case_422(base_url, path):
    payload = {}
    response = requests.post(f"{base_url}/{path}/", json=payload)
    assert response.status_code == 422, f"Unexpected status code: {response.status_code}"
