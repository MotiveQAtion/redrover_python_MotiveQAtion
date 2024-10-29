from lesson1.api_tests.utils.api_client import client


def create_case(json=None):
    if json is None:
        json = {}
    response = client.make_request(handle="/testcases", method="POST", json=json)
    return response
