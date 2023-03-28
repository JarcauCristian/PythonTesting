import json


def datacapture_request(datacapture_id: str, datasource_id: str, dataset_id: str, date_added: str, date_finished: str,
                        status: str, date_pattern: str, null_string: str, batch_size: int):
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


def process_post_request(i_help_id: int, gender: str, date: str, pilot_id: str, healthentia_id: str):
    return {
        "ihelpID": i_help_id,
        "gender": gender,
        "date": date,
        "pilotID": pilot_id,
        "healthentiaID": healthentia_id
    }


def tables():
    return [
        "CONDITION",
        "ENCOUNTER",
        "FPG_BASE",
        "FPG_BLOOD",
        "HEALTHENTIA_ANSWERS",
        "HEALTHENTIA_EXERCISES",
        "HEALTHENTIA_PHYSIOLOGICAL",
        "HEALTHENTIA_SUBJECTS",
        "IHELP_PERSON",
        "MEDICATION",
        "PATIENT"
    ]


def primary_keys():
    return {
        "CONDITION": [{"name": "CONDITIONID", "type": "INT"}],
        "ENCOUNTER": [{"name": "ENCOUNTERID", "type": "INT"}],
        "FPG_BASE": [{"name": "ID", "type": "INT"}],
        "FPG_BLOOD": [{"name": "ID", "type": "INT"}],
        "HEALTHENTIA_ANSWERS": [{"name": "ID", "type": "LONG"}],
        "HEALTHENTIA_EXERCISES": [{"name": "ID", "type": "LONG"}],
        "HEALTHENTIA_PHYSIOLOGICAL": [{"name": "ID", "type": "LONG"}],
        "HEALTHENTIA_SUBJECTS": [{"name": "SUBJECTIDENTIFICATIONNUMBER", "type": "STRING"}],
        "IHELP_PERSON": [{"name": "IHELPID", "type": "STRING"}, {"name": "PATIENTID", "type": "STRING"},
                         {"name": "PROVIDERID", "type": "STRING"}],
        "MEDICATION": [{"name": "MEDICATIONID", "type": "INT"}],
        "PATIENT": [{"name": "PATIENTID", "type": "STRING"}, {"name": "PROVIDERID", "type": "STRING"}]
    }


def columns():
    return {
        "CONDITION": [{"name": "CONDITIONID", "type": "INT"}, {"name": "CATEGORY", "type": "STRING"},
                      {"name": "ENCOUNTERID", "type": "INT"}, {"name": "PRACTITIONERID", "type": "INT"},
                      {"name": "PATIENTID", "type": "STRING"}, {"name": "PROVIDERID", "type": "STRING"},
                      {"name": "ABATEMENTDATETIME", "type": "TIMESTAMP"}, {"name": "ONSETDATE", "type": "TIMESTAMP"}],
        "ENCOUNTER": [{"name": "ENCOUNTERID", "type": "INT"}, {"name": "STATUS", "type": "STRING"},
                      {"name": "TYPESYSTEM", "type": "STRING"}, {"name": "TYPECODE", "type": "STRING"},
                      {"name": "TYPEDISPLAY", "type": "STRING"}, {"name": "SERVICEPROVIDERID", "type": "INT"},
                      {"name": "PRACTITIONERID", "type": "INT"}, {"name": "PATIENTID", "type": "STRING"},
                      {"name": "PROVIDERID", "type": "STRING"}, {"name": "PERIODSTART", "type": "TIMESTAMP"},
                      {"name": "PERIODEND", "type": "TIMESTAMP"}],
        "FPG_BASE": [{"name": "ID", "type": "INT"}, {"name": "PATIENT_ID", "type": "STRING"},
                     {"name": "SEX", "type": "STRING"}, {"name": "AGE", "type": "INT"},
                     {"name": "AGE_UNIT", "type": "STRING"}, {"name": "CA19_9_DIAGNOSIS_UNIT", "type": "STRING"},
                     {"name": "STAGING_P_T", "type": "INT"}, {"name": "STAGING_P_N", "type": "INT"},
                     {"name": "STAGING_P_M", "type": "INT"}, {"name": "STAGING_C_T", "type": "INT"},
                     {"name": "STAGING_C_N", "type": "INT"}, {"name": "STAGING_C_M", "type": "INT"},
                     {"name": "TUMOR_LOCATION", "type": "STRING"}, {"name": "BIOPSY_GRADING", "type": "STRING"},
                     {"name": "HISTOLOGY", "type": "STRING"}, {"name": "ASA_SCORE", "type": "INT"},
                     {"name": "BILIARY_PROSTHESIS", "type": "INT"}, {"name": "SURGERY_BOOL", "type": "STRING"},
                     {"name": "SURGERY_TYPE", "type": "STRING"}, {"name": "SURGERY_APPROACH", "type": "STRING"},
                     {"name": "SURGERY_DURATION", "type": "INT"}, {"name": "SURGERY_DURATION_UNIT", "type": "STRING"},
                     {"name": "SURGERY_INTRAOPERATIVE_BLOOD_LOSS", "type": "INT"},
                     {"name": "SURGERY_INTRAOPERATIVE_BLOOD_LOSS_UNIT", "type": "STRING"},
                     {"name": "SURGERY_GRADING", "type": "STRING"}, {"name": "NUMBER_NODES", "type": "INT"},
                     {"name": "NUMBER_NODES_UNIT", "type": "STRING"}, {"name": "NUMBER_POSITIVE_NODES", "type": "INT"},
                     {"name": "NUMBER_POSITIVE_NODES_UNIT", "type": "STRING"},
                     {"name": "NODES_RATIO_UNIT", "type": "STRING"}, {"name": "MARGIN_STATUS", "type": "STRING"},
                     {"name": "LIMPHOVASCULAR_SPACES_INVASION", "type": "STRING"},
                     {"name": "PERINEURAL_INVASION", "type": "STRING"},
                     {"name": "CA19_9_AFTER_SURGERY_UNIT", "type": "STRING"},
                     {"name": "POST_OPERATIVE_COMPLICATIONS", "type": "STRING"},
                     {"name": "PANCREATIC_FISTULA", "type": "STRING"}, {"name": "BILIARY_FISTULA", "type": "STRING"},
                     {"name": "RE_SURGERY", "type": "STRING"}, {"name": "CHEMOTHERAPY_BOOL", "type": "STRING"},
                     {"name": "CHEMOTHERAPY_TYPE", "type": "STRING"},
                     {"name": "RADIOTHERAPY_NUMBER_CICLES", "type": "INT"},
                     {"name": "RADIOTHERAPY_NUMBER_CICLES_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_TIMING", "type": "STRING"},
                     {"name": "RADIOTHERAPY_SETTING", "type": "STRING"},
                     {"name": "RADIOTHERAPY_TECHNIQUE", "type": "STRING"},
                     {"name": "RADIOTHERAPY_CTV1_DOSE_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_CTV1_FRACTIONATION_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_CTV2_DOSE_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_CTV2_FRACTIONATION_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_CTV3_DOSE_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_CTV3_FRACTIONATION_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_REASON_FOR_SUSPENSION_RT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_DAYS_OF_SUSPENSION_RT", "type": "INT"},
                     {"name": "RADIOTHERAPY_DAYS_OF_SUSPENSION_RT_UNIT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_EARLY_CLOSURE_OF_RT_TREATMENT", "type": "STRING"},
                     {"name": "RADIOTHERAPY_REASON_FOR_EARLY_CLOSURE", "type": "STRING"},
                     {"name": "ACUTE_UPPER_GI_TOXICITY", "type": "STRING"},
                     {"name": "ACUTE_UPPER_GI_TOXICITY_GRADE", "type": "STRING"},
                     {"name": "LATE_UPPER_GI_TOXICITY", "type": "STRING"},
                     {"name": "LATE_UPPER_GI_TOXICITY_GRADE", "type": "STRING"},
                     {"name": "NEED_FOR_HOSPITALIZATION", "type": "STRING"},
                     {"name": "CONCOMITANT_CHEMOTHERAPY", "type": "STRING"},
                     {"name": "CONCOMITANT_CHEMOTHERAPY_TYPE", "type": "STRING"},
                     {"name": "CONCOMITANT_CHEMOTHERAPY_CICLES", "type": "INT"},
                     {"name": "CONCOMITANT_CHEMOTHERAPY_CICLES_UNIT", "type": "STRING"},
                     {"name": "CONCOMITANT_CHEMOTHERAPY_REASON_SUSPENSION", "type": "STRING"},
                     {"name": "CONCOMITANT_CHEMOTHERAPY_DAYS_OF_SUSPENSION", "type": "INT"},
                     {"name": "CONCOMITANT_CHEMOTHERAPY_DAYS_OF_SUSPENSION_UNIT", "type": "STRING"},
                     {"name": "CHEMOTHERAPY_SCHEDULE_CHANGE", "type": "STRING"},
                     {"name": "OVERALL_SURVIVAL", "type": "STRING"},
                     {"name": "DISEASE_FREE_SURVIVAL", "type": "STRING"}, {"name": "LOCAL_CONTROL", "type": "STRING"},
                     {"name": "REGIONAL_CONTROL", "type": "STRING"}, {"name": "DISTANT_METASTASIS", "type": "STRING"},
                     {"name": "DATE_OF_BIRTH", "type": "TIMESTAMP"}, {"name": "DATE_OF_DIAGNOSIS", "type": "TIMESTAMP"},
                     {"name": "CA19_9_DIAGNOSIS", "type": "DOUBLE"},
                     {"name": "DATE_OF_DIAGNOSIS_DATE", "type": "TIMESTAMP"},
                     {"name": "SURGERY_DATE", "type": "TIMESTAMP"}, {"name": "NODES_RATIO", "type": "DOUBLE"},
                     {"name": "CA19_9_AFTER_SURGERY", "type": "DOUBLE"},
                     {"name": "CA19_9_AFTER_SURGERY_DATE", "type": "TIMESTAMP"},
                     {"name": "RADIOTHERAPY_START_DATE", "type": "TIMESTAMP"},
                     {"name": "RADIOTHERAPY_END_DATE", "type": "TIMESTAMP"},
                     {"name": "RADIOTHERAPY_CTV1_DOSE", "type": "DOUBLE"},
                     {"name": "RADIOTHERAPY_CTV1_FRACTIONATION", "type": "DOUBLE"},
                     {"name": "RADIOTHERAPY_CTV2_DOSE", "type": "DOUBLE"},
                     {"name": "RADIOTHERAPY_CTV2_FRACTIONATION", "type": "DOUBLE"},
                     {"name": "RADIOTHERAPY_CTV3_DOSE", "type": "DOUBLE"},
                     {"name": "RADIOTHERAPY_CTV3_FRACTIONATION", "type": "DOUBLE"},
                     {"name": "RADIOTHERAPY_RT_1ST_VISIT_DATE", "type": "TIMESTAMP"},
                     {"name": "RADIOTHERAPY_RT_SIMULATION_DATE", "type": "TIMESTAMP"},
                     {"name": "LAST_FOLLOW_UP_DATE", "type": "TIMESTAMP"},
                     {"name": "OVERALL_SURVIVAL_DATE", "type": "TIMESTAMP"},
                     {"name": "DISEASE_FREE_SURVIVAL_DATE", "type": "TIMESTAMP"},
                     {"name": "LOCAL_CONTROL_DATE", "type": "TIMESTAMP"},
                     {"name": "REGIONAL_CONTROL_DATE", "type": "TIMESTAMP"},
                     {"name": "DISTANT_METASTASIS_DATE", "type": "TIMESTAMP"}],
        "FPG_BLOOD": [{"name": "ID", "type": "INT"}, {"name": "PATIENT_ID", "type": "STRING"},
                      {"name": "ANALYSIS_NAME", "type": "STRING"}, {"name": "ANALYSIS_UNIT", "type": "STRING"},
                      {"name": "ANALYSIS_DATE", "type": "TIMESTAMP"}, {"name": "ANALYSIS_VALUE", "type": "DOUBLE"}],
        "HEALTHENTIA_ANSWERS": [{"name": "ID", "type": "LONG"}, {"name": "SUBJECTID", "type": "STRING"},
                                {"name": "QUESTIONNAIREID", "type": "INT"},
                                {"name": "QUESTIONNAIRETITLE", "type": "STRING"},
                                {"name": "QUESTIONNAIRECODENAME", "type": "STRING"},
                                {"name": "QUESTIONID", "type": "INT"}, {"name": "QUESTIONTITLE", "type": "STRING"},
                                {"name": "QUESTIONCODENAME", "type": "STRING"}, {"name": "ANSWER", "type": "STRING"},
                                {"name": "SCORE", "type": "INT"}, {"name": "PARENTQUESTION", "type": "STRING"},
                                {"name": "DATE", "type": "TIMESTAMP"}, {"name": "SENTDATE", "type": "TIMESTAMP"}],
        "HEALTHENTIA_EXERCISES": [{"name": "ID", "type": "LONG"}, {"name": "SUBJECTID", "type": "STRING"},
                                  {"name": "TITLE", "type": "STRING"}, {"name": "CALORIES", "type": "INT"},
                                  {"name": "SPEED", "type": "INT"}, {"name": "PACE", "type": "INT"},
                                  {"name": "STEPS", "type": "INT"}, {"name": "DISTANCE", "type": "INT"},
                                  {"name": "DISTANCEUNIT", "type": "STRING"}, {"name": "ELEVATIONGAIN", "type": "INT"},
                                  {"name": "AVERAGEHEARTRATE", "type": "INT"},
                                  {"name": "OUTOFRANGEMINUTES", "type": "INT"},
                                  {"name": "FATBURNMINUTES", "type": "INT"}, {"name": "CARDIOMINUTES", "type": "INT"},
                                  {"name": "PEAKMINUTES", "type": "INT"}, {"name": "HEARTRATEZONES", "type": "STRING"},
                                  {"name": "SEDENTARYMINUTES", "type": "INT"},
                                  {"name": "LIGHTLYMINUTES", "type": "INT"}, {"name": "FAIRLYMINUTES", "type": "INT"},
                                  {"name": "VERYMINUTES", "type": "INT"}, {"name": "STARTTIME", "type": "TIMESTAMP"},
                                  {"name": "DURATION", "type": "LONG"}, {"name": "ACTIVEDURATION", "type": "LONG"}],
        "HEALTHENTIA_PHYSIOLOGICAL": [{"name": "ID", "type": "LONG"}, {"name": "SUBJECTID", "type": "STRING"},
                                      {"name": "TYPE", "type": "STRING"}, {"name": "VALUE", "type": "INT"},
                                      {"name": "TREND", "type": "INT"}, {"name": "MEANSHORT", "type": "INT"},
                                      {"name": "DATE", "type": "TIMESTAMP"}, {"name": "MEANLONG", "type": "LONG"}],
        "HEALTHENTIA_SUBJECTS": [{"name": "SUBJECTIDENTIFICATIONNUMBER", "type": "STRING"},
                                 {"name": "TIMEZONE", "type": "STRING"}, {"name": "TRACKERID", "type": "STRING"},
                                 {"name": "STATUS", "type": "STRING"}, {"name": "SEX", "type": "STRING"},
                                 {"name": "HEIGHT", "type": "INT"}, {"name": "WEIGHT", "type": "INT"},
                                 {"name": "DISEASE", "type": "STRING"}, {"name": "SEVERITY", "type": "STRING"},
                                 {"name": "QTROBOTID", "type": "STRING"},
                                 {"name": "BASELINEDATE", "type": "TIMESTAMP"}],
        "IHELP_PERSON": [{"name": "IHELPID", "type": "STRING"}, {"name": "PATIENTID", "type": "STRING"},
                         {"name": "PROVIDERID", "type": "STRING"}],
        "MEDICATION": [{"name": "MEDICATIONID", "type": "INT"}, {"name": "STATUS", "type": "STRING"},
                       {"name": "MEDICATIONSYSTEM", "type": "STRING"}, {"name": "MEDICATIONCODE", "type": "STRING"},
                       {"name": "MEDICATIONDISPLAY", "type": "STRING"}, {"name": "ENCOUNTERID", "type": "INT"},
                       {"name": "PRACTITIONERID", "type": "INT"}, {"name": "PATIENTID", "type": "STRING"},
                       {"name": "PROVIDERID", "type": "STRING"}, {"name": "EFFECTIVEPERIODSTART", "type": "TIMESTAMP"},
                       {"name": "EFFECTIVEPERIODEND", "type": "TIMESTAMP"}, {"name": "DOSAGE", "type": "DOUBLE"}],
        "PATIENT": [{"name": "PATIENTID", "type": "STRING"}, {"name": "PROVIDERID", "type": "STRING"},
                    {"name": "ACTIVE", "type": "BOOLEAN"}, {"name": "GENDER", "type": "STRING"},
                    {"name": "BIRTHDATE", "type": "TIMESTAMP"}]
    }


def indexes():
    return {
        "CONDITION": [],
        "ENCOUNTER": [],
        "FPG_BASE": [],
        "FPG_BLOOD": [],
        "HEALTHENTIA_ANSWERS": [],
        "HEALTHENTIA_EXERCISES": [],
        "HEALTHENTIA_PHYSIOLOGICAL": [],
        "HEALTHENTIA_SUBJECTS": [],
        "IHELP_PERSON": [{"name": "FK_IHELP-APP-IHELP_PERSON_PATIENTID", "unique": False,
                          "fields": [{"name": "PATIENTID", "type": "STRING"}]},
                         {"name": "FK_IHELP-APP-IHELP_PERSON_PROVIDERID", "unique": False,
                          "fields": [{"name": "PROVIDERID", "type": "STRING"}]}],
        "MEDICATION": [],
        "PATIENT": []
    }
