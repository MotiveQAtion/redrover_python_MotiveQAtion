# utils.py

from jsonschema import validate, ValidationError
import pytest
import requests

def validate_json_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match the expected schema: {e.message}")

def create_case(case_data, base_url, path):
    payload = case_data.dict()
    response = requests.post(f"{base_url}/{path}/", json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    return response.json()

def get_id_of_created_case(case_data, base_url, path):
    return create_case(case_data, base_url, path).get("id")


