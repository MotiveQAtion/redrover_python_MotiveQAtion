import requests

URL='http://127.0.0.1:8000/testcases'

def get_case():
    return requests.get(URL)