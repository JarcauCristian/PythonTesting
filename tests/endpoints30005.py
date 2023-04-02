import requests
from data_requests.Schemas import *
from data_requests.ihelp_request import *
import logging

url = "http://147.102.230.182:30005/ihelp"
headers = {"Content-Type": "application/json; charset=utf-8"}
logging.basicConfig(filename='endpoints30005.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def test_metainfo_returns_200():
    response = requests.get(url + "/metainfo")
    if response.status_code != 200:
        logging.error(f'The endpoint metainfo returned wrong status code: {response.status_code}')
    assert response.status_code == 200


def test_metainfo_returns_correct_body():
    response = requests.get(url + "/metainfo")
    body = ""
    if response.status_code == 200:
        body = response.content.decode("utf-8")
    if body != '["ENCOUNTER","MEDICATION","CONDITION","IHELP_PERSON","PATIENT","FPG_BASE","FPG_BLOOD","HEALTHENTIA_SUBJECTS","HEALTHENTIA_ANSWERS","HEALTHENTIA_EXERCISES","HEALTHENTIA_PHYSIOLOGICAL"]':
        logging.error(f'The endpoint metainfo returned wrong body: {body}')
    assert body == '["ENCOUNTER","MEDICATION","CONDITION","IHELP_PERSON","PATIENT","FPG_BASE","FPG_BLOOD","HEALTHENTIA_SUBJECTS","HEALTHENTIA_ANSWERS","HEALTHENTIA_EXERCISES","HEALTHENTIA_PHYSIOLOGICAL"]'


def test_process_returns_200():
    errors = []
    for table in tables():
        response = requests.get(url + "/process?query=SELECT * FROM " + table)
        if response.status_code != 200:
            errors.append(url + "/process?query=SELECT * FROM " + table + " returned status code: " + str(response.status_code))
    if errors:
        logging.error(f'For endpoint process the following errors for the status code occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_process_returns_correct_body():
    errors = []
    for table in tables():
        response = requests.get(url + "/process?query=SELECT * FROM " + table)
        body = response.content.decode("utf-8")
        if check(process_schema(), body):
            errors.append(url + "/process?query=SELECT * FROM " + table + " returned wrong body")
    if errors:
        logging.error(f'For endpoint process the following errors for the body occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_process_post_returns_200():
    response = requests.post(url + "/process", headers=headers, json=process_post_request(1, "male", "25-03-2023", "22", "22"))
    if response.status_code != 200:
        logging.error(f'The endpoint POST process returned wrong status code: {response.status_code}')
    assert response.status_code == 200


def test_test_returns_200():
    response = requests.get(url + "/test")
    if response.status_code != 200:
        logging.error(f'The endpoint test returned wrong status code: {response.status_code}')
    assert response.status_code == 200


def test_test_returns_correct_body():
    response = requests.get(url + "/test")
    body = ""
    if response.status_code == 200:
        body = response.content.decode("utf-8")
    if "Hello world!" not in body:
        logging.error(f'The endpoint test returned wrong body: {body}')
    assert "Hello world!" in body


def test_test_name_returns_200():
    response = requests.get(url + "/test/john")
    if response.status_code != 200:
        logging.error(f'The endpoint test name returned wrong status code: {response.status_code}')
    assert response.status_code == 200


def test_test_name_returns_correct_body():
    response = requests.get(url + "/test/john")
    body = ""
    if response.status_code == 200:
        body = response.content.decode("utf-8")
    if 'Hello john!' not in body:
        logging.error(f'The endpoint test name returned wrong body: {body}')
    assert "Hello john!" in body


def test_metainfo_primary_key_returns_200():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/primarykey")
        if response.status_code != 200:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/primarykey returned status code different then 200.")
    if errors:
        logging.error(f'For endpoint metainfo/primarykey the following errors for the status code occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_primary_key_returns_correct_body():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/primarykey")
        body = json.loads(response.content.decode("utf-8"))
        if body != primary_keys()[table]:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/primarykey returned wrong body.")
    if errors:
        logging.error(f'For endpoint metainfo/primarykey the following errors for the body occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_primary_key_returns_correct_schema():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/primarykey")
        body = json.loads(response.content.decode("utf-8"))
        if not check(metainfo_primarykey_columns_schema(), body):
            errors.append("The endpoint " + url + "/metainfo/" + table + "/primarykey doesn't match the schema.")
    if errors:
        logging.error(f'For endpoint metainfo/primarykey the following errors for the schema occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_columns_returns_200():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/columns")
        if response.status_code != 200:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/columns returned status code different then 200.")
    if errors:
        logging.error(f'For endpoint metainfo/columns the following errors for the status code occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_columns_returns_correct_body():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/columns")
        body = json.loads(response.content.decode("utf-8"))
        if body != columns()[table]:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/columns returned wrong body.")
    if errors:
        logging.error(f'For endpoint metainfo/columns the following errors for the body occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_columns_returns_correct_schema():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/columns")
        body = json.loads(response.content.decode("utf-8"))
        if not check(metainfo_primarykey_columns_schema(), body):
            errors.append("The endpoint " + url + "/metainfo/" + table + "/columns doesn't match the schema.")
    if errors:
        logging.error(f'For endpoint metainfo/columns the following errors for the schema occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_indexes_returns_200():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/indexes")
        if response.status_code != 200:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/indexes returned status code different then 200.")
    if errors:
        logging.error(f'For endpoint metainfo/indexes the following errors for the status code occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_indexes_returns_correct_body():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/indexes")
        body = json.loads(response.content.decode("utf-8"))
        if body != indexes()[table]:
            errors.append("The endpoint " + url + "/metainfo/" + table + "/indexes returned wrong body.")
    if errors:
        logging.error(f'For endpoint metainfo/indexes the following errors for the body occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_metainfo_indexes_returns_correct_schema():
    errors = []
    for table in tables():
        response = requests.get(url + "/metainfo/" + table + "/indexes")
        body = json.loads(response.content.decode("utf-8"))
        if not check(metainfo_indexes_schema(), body):
            errors.append("The endpoint " + url + "/metainfo/" + table + "/indexes doesn't match the schema.")
    if errors:
        logging.error(f'For endpoint metainfo/indexes the following errors for the schema occurred: {errors}')
    assert not errors, "errors occurred:\n{}".format("\n".join(errors))
