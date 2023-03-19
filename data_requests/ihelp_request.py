import json


def datacapture_request(datacapture_id: str, datasource_id: str, dataset_id: str, date_added: str, date_finished: str, status: str, date_pattern: str, null_string: str, batch_size: int):
    request_body = dict()
    request_body["id"] = datacapture_id
    request_body["datasourceID"] = datasource_id
    request_body["datasetID"] = dataset_id
    request_body["dateAdded"] = date_added
    request_body["dateFinished"] = date_finished
    request_body["status"] = status
    request_body["connectorArguments"] = {"datePattern": date_pattern, "nullString": null_string}
    request_body["convertorArguments"] = {"datePattern": date_pattern}
    request_body["batchSize"] = batch_size

    return json.dumps(request_body)


def datacapture_combo_request():
    request_body = {
        "id": "string",
        "name": "string",
        "status": "string",
        "dateAdded": "string",
        "dateFinished": "string",
        "jobs": [
            {
                "order": 0,
                "job": {
                    "id": "string",
                    "datasourceID": "string",
                    "datasetID": "string",
                    "dateAdded": "string",
                    "dateFinished": "string",
                    "status": "string",
                    "connectorArguments": {
                        "datePattern": "string",
                        "nullString": "string"
                    },
                    "converterArguments": {
                        "datePattern": "string"
                    },
                    "batchSize": 0
                }
            }
        ]
    }
    return json.dumps(request_body)
