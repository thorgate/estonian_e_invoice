HEADER_VALIDATION_SCHEMA = {
    "date": {"type": "date", "required": True,},
    "file_id": {
        "type": "string",
        "required": True,
        "empty": False,
        "maxlength": 20,
    },
    "version": {
        "type": "string",
        "required": True,
        "empty": False,
        "maxlength": 20,
    },
    "is_test": {"type": "boolean", "required": False,},
    "app_id": {
        "type": "string",
        "required": False,
        "empty": False,
        "maxlength": 20,
    },
    "sender_id": {
        "type": "string",
        "required": False,
        "empty": False,
        "maxlength": 20,
    },
    "receiver_id": {
        "type": "string",
        "required": False,
        "empty": False,
        "maxlength": 20,
    },
    "contract_id": {
        "type": "string",
        "required": False,
        "empty": False,
        "maxlength": 20,
    },
    "payee_acc_number": {
        "type": "string",
        "required": False,
        "empty": False,
        "maxlength": 35,
        "regex": "([0-9|A-Z])*",
    },
}
