from lesson1.api_tests.utils.api_client import client

case2 = {
    "id": 3,
    "name": "TC_002",
    "description": "Image not visible",
    "steps": [
        "Open page",
        "Check image"
    ],
    "expected_result": "Image damage",
    "priority": "средний"
}


def create_case(json={}):
    response = client.make_request(handle="/testcases", method="POST", json=json)
    return response
