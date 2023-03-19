import random

import requests
from data_requests.ihelp_request import *

url = "http://147.102.230.182:30007/ihelp/"


def t_datacapture_request():
    return datacapture_request("1", "1", "1", "19-03-2023", "19-03-2023", "Ready", "dd-mm-yyyy", "", 0)


def t_datacapture_combo_request():
    return datacapture_combo_request()


def test_datacapture_test_returns_200():
    response = requests.get(url + "datacapture/test")
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_test_returns_correct_body():
    response = requests.get(url + "datacapture/test")
    body = response.content.decode("utf-8")
    assert "Hello from the test resource!" in body


def test_datacapture_get_returns_200():
    response = requests.get(url + "datacapture")
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_get_returns_correct_body():
    response = requests.get(url + "datacapture")
    body = json.dumps(response.content.decode("utf-8"))
    assert body in json.dumps('[]')


def test_datacapture_post_returns_200():
    response = requests.post(url + "datacapture", json=t_datacapture_request())
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_id_returns_200():
    my_id = random.randint(0, 100)
    response = requests.get(url + "datacapture/" + str(my_id))
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_id_returns_correct_body():
    my_id = random.randint(0, 100)
    response = requests.get(url + "datacapture/" + str(my_id))
    body = json.dumps(response.content.decode("utf-8"))
    assert body in t_datacapture_request()


def test_datacapture_combo_test_returns_200():
    response = requests.get(url + "datacapture/combo/test")
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_combo_test_returns_correct_body():
    response = requests.get(url + "datacapture/combo/test")
    body = response.content.decode("utf-8")
    assert "Hello from the test resource!" in body


def test_datacapture_combo_returns_200():
    response = requests.get(url + "datacapture/combo")
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_combo_returns_correct_body():
    response = requests.get(url + "datacapture/combo")
    body = json.dumps(response.content.decode("utf-8"))
    assert body in json.dumps('[]')


def test_datacapture_combo_post_returns_200():
    response = requests.post(url + "datacapture/combo", json=t_datacapture_combo_request())
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_combo_id_returns_200():
    my_id = random.randint(0, 100)
    response = requests.get(url + "datacapture/combo" + str(my_id))
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_combo_id_returns_correct_body():
    my_id = random.randint(0, 100)
    response = requests.get(url + "datacapture/combo" + str(my_id))
    body = json.dumps(response.content.decode("utf-8"))
    assert body in t_datacapture_combo_request()


def test_datacapture_combo_schedule_test_returns_200():
    response = requests.get(url + "datacapture/combo/schedule/test")
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_combo_schedule_test_returns_correct_body():
    response = requests.get(url + "datacapture/combo/schedule/test")
    body = response.content.decode("utf-8")
    assert "Hello from the test resource!" in body


def test_datacapture_combo_schedule_returns_200():
    response = requests.get(url + "datacapture/combo/schedule")
    status_code = response.status_code
    assert status_code == 200


def test_datacapture_combo_schedule_returns_correct_body():
    response = requests.get(url + "datacapture/combo/schedule")
    body = json.dumps(response.content.decode("utf-8"))
    assert body in json.dumps('[]')
