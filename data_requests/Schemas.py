from schema import Schema, And, Use, SchemaError


def check(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError:
        return False


def datacapture_list_schema():
    return Schema(
        [
            {
                "id": And(Use(str)),
                "datasourceID": And(Use(str)),
                "datasetID": And(Use(str)),
                "dateAdded": And(Use(str)),
                "dateFinished": And(Use(str)),
                "status": And(Use(str)),
                "connectorArguments": {
                    "datePattern": And(Use(str)),
                    "nullString": And(Use(str))
                },
                "convertorArguments": {
                    "datePattern": And(Use(str))
                },
                "batchSize": And(Use(int))
            }
        ]
    )


def datacapture_schema():
    return Schema(
        {
            "id": And(Use(str)),
            "datasourceID": And(Use(str)),
            "datasetID": And(Use(str)),
            "dateAdded": And(Use(str)),
            "dateFinished": And(Use(str)),
            "status": And(Use(str)),
            "connectorArguments": {
                "datePattern": And(Use(str)),
                "nullString": And(Use(str))
            },
            "convertorArguments": {
                "datePattern": And(Use(str))
            },
            "batchSize": And(Use(int))
        }
    )


def datacapture_combo_list_schema():
    return Schema(
        [
            {
                "id": And(Use(str)),
                "name": And(Use(str)),
                "status": And(Use(str)),
                "dateAdded": And(Use(str)),
                "dateFinished": And(Use(str)),
                "jobs": [
                    {
                        "order": And(Use(int)),
                        "job": {
                            "id": And(Use(str)),
                            "datasourceID": And(Use(str)),
                            "datasetID": And(Use(str)),
                            "dateAdded": And(Use(str)),
                            "dateFinished": And(Use(str)),
                            "status": And(Use(str)),
                            "connectorArguments": {
                                "datePattern": And(Use(str)),
                                "nullString": And(Use(str))
                            },
                            "converterArguments": {
                                "datePattern": And(Use(str))
                            },
                            "batchSize": And(Use(int))
                        }
                    }
                ]
            }
        ]
    )


def datacapture_combo_schema():
    return Schema(
        {
            "id": And(Use(str)),
            "name": And(Use(str)),
            "status": And(Use(str)),
            "dateAdded": And(Use(str)),
            "dateFinished": And(Use(str)),
            "jobs": [
                {
                    "order": And(Use(int)),
                    "job": {
                        "id": And(Use(str)),
                        "datasourceID": And(Use(str)),
                        "datasetID": And(Use(str)),
                        "dateAdded": And(Use(str)),
                        "dateFinished": And(Use(str)),
                        "status": And(Use(str)),
                        "connectorArguments": {
                            "datePattern": And(Use(str)),
                            "nullString": And(Use(str))
                        },
                        "converterArguments": {
                            "datePattern": And(Use(str))
                        },
                        "batchSize": And(Use(int))
                    }
                }
            ]
        }
    )


def datacapture_combo_schedule_list_schema():
    return Schema(
        [
            {
                "schedule": {
                    "future": {
                        "time": And(Use(int)),
                        "unit": And(Use(str))
                    },
                    "periodic": {
                        "time": And(Use(int)),
                        "unit": And(Use(str))
                    }
                },
                "name": And(Use(str)),
                "id": And(Use(str)),
                "status": And(Use(str)),
                "dateFinished": And(Use(str)),
                "jobs": [
                    {
                        "order": And(Use(int)),
                        "job": {
                            "id": And(Use(str)),
                            "datasourceID": And(Use(str)),
                            "datasetID": And(Use(str)),
                            "dateAdded": And(Use(str)),
                            "dateFinished": And(Use(str)),
                            "status": And(Use(str)),
                            "connectorArguments": {
                                "datePattern": And(Use(str)),
                                "nullString": And(Use(str))
                            },
                            "converterArguments": {
                                "datePattern": And(Use(str))
                            },
                            "batchSize": And(Use(int))
                        }
                    }
                ],
                "dateAdded": And(Use(str))
            }
        ]
    )


def metainfo_primarykey_columns_schema():
    return Schema(
        [
            {
                "name": And(Use(str)),
                "type": And(Use(str))
            }
        ]
    )


def metainfo_indexes_schema():
    return Schema(
        [
            {
                "name": And(Use(str)),
                "unique": And(Use(bool)),
                "fields": [
                    {
                        "name": And(Use(str)),
                        "type": And(Use(str))
                    }
                ]
            }
        ]
    )


def process_schema():
    return Schema(
        [
            {
                "row": [
                    {
                        "name": And(Use(str))
                    }
                ]
            }
        ]
    )
