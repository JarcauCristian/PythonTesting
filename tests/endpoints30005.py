import requests

url = "http://147.102.230.182:30005/ihelp"


def test_metainfo_returns_200():
    response = requests.get(url + "/metainfo")
    assert response.status_code == 200


def test_metainfo_returns_correct_body():
    response = requests.get(url + "/metainfo")
    body = response.content.decode("utf-8")
    assert body == '["ENCOUNTER","MEDICATION","CONDITION","IHELP_PERSON","PATIENT","FPG_BASE","FPG_BLOOD","HEALTHENTIA_SUBJECTS","HEALTHENTIA_ANSWERS","HEALTHENTIA_EXERCISES","HEALTHENTIA_PHYSIOLOGICAL"]'
