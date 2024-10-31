import requests

URL ='http://127.0.0.1:8000/testcases/'


def create_test(info):
    return requests.post(URL, json=info)


def read_test(test_case_id):
    return requests.get(URL + f"{test_case_id}")


def update_test(test_case_id, info2):
    return requests.put(URL + f"{test_case_id}", json= info2)


def delete_test(test_case_id):
    return requests.delete(URL + f"{test_case_id}")

