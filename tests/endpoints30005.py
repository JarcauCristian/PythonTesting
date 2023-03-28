import requests
from data_requests.Schemas import *
from data_requests.ihelp_request import *

url = "http://147.102.230.182:30005/ihelp"
headers = {"Content-Type": "application/json; charset=utf-8"}


def test_metainfo_returns_200():
    response = requests.get(url + "/metainfo")
    assert response.status_code == 200


def test_metainfo_returns_correct_body():
    response = requests.get(url + "/metainfo")
    body = ""
    if response.status_code == 200:
        body = response.content.decode("utf-8")
    assert body == '["ENCOUNTER","MEDICATION","CONDITION","IHELP_PERSON","PATIENT","FPG_BASE","FPG_BLOOD","HEALTHENTIA_SUBJECTS","HEALTHENTIA_ANSWERS","HEALTHENTIA_EXERCISES","HEALTHENTIA_PHYSIOLOGICAL"]'


def test_process_returns_200():
    response = requests.get(url + "/process?query=something")
    assert response.status_code == 200


def test_process_returns_correct_body():
    response = requests.get(url + "/process?query=something")
    body = ""
    if response.status_code == 200:
        body = response.content.decode("utf-8")
    assert check(process_schema(), body)


def test_process_post_returns_200():
    response = requests.post(url + "/process", headers=headers, json=process_post_request(1, "male", "25-03-2023", "22", "22"))
    assert response.status_code == 200


def test_test_returns_200():
    response = requests.get(url + "/test")
    assert response.status_code == 200


def test_test_returns_correct_body():
    response = requests.get(url + "/test")
    body = ""
    if response.status_code == 200:
        body = response.content.decode("utf-8")
    assert "Hello world!" in body


def test_test_name_returns_200():
    response = requests.get(url + "/test/john")
    assert response.status_code == 200


def test_test_name_returns_correct_body():
    response = requests.get(url + "/test/john")
    body = ""
    if response.status_code == 200:
        body = response.content.decode("utf-8")
    assert "Hello john!" in body


def test_metainfo_primary_key_returns_200():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/primarykey")
        if response.status_code != 200:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/primarykey returned status code different then 200.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_primary_key_returns_correct_body():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/primarykey")
        body = json.loads(response.content.decode("utf-8"))
        if body != primary_keys()[table]:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/primarykey returned wrong body.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_primary_key_returns_correct_schema():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/primarykey")
        body = json.loads(response.content.decode("utf-8"))
        if not check(metainfo_primarykey_columns_schema(), body):
            errors.append("The endpoint " + url + "/metainfo/" + table + "/primarykey doesn't match the schema.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_columns_returns_200():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/columns")
        if response.status_code != 200:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/columns returned status code different then 200.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_columns_returns_correct_body():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/columns")
        body = json.loads(response.content.decode("utf-8"))
        if body != columns()[table]:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/columns returned wrong body.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_columns_returns_correct_schema():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/columns")
        body = json.loads(response.content.decode("utf-8"))
        if not check(metainfo_primarykey_columns_schema(), body):
            errors.append("The endpoint " + url + "/metainfo/" + table + "/columns doesn't match the schema.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_indexes_returns_200():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/indexes")
        if response.status_code != 200:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/indexes returned status code different then 200.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_indexes_returns_correct_body():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/indexes")
        body = json.loads(response.content.decode("utf-8"))
        if body != indexes()[table]:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/indexes returned wrong body.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_indexes_returns_correct_schema():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/indexes")
        body = json.loads(response.content.decode("utf-8"))
        if not check(metainfo_indexes_schema(), body):
            errors.append("The endpoint " + url + "/metainfo/" + table + "/indexes doesn't match the schema.")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
