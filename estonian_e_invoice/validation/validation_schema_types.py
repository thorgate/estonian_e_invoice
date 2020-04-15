DATE_TYPE = {
    "type": "date",
    "required": False,
}

DATE_TYPE_REQUIRED = {
    **DATE_TYPE,
    "required": True,
}

STRING_TYPE = {
    "type": "string",
    "required": False,
}

STRING_TYPE_REQUIRED = {
    "type": "string",
    "required": True,
    "empty": False,
}

SHORT_STRING_TYPE = {
    **STRING_TYPE,
    "max_length": 20,
}

SHORT_STRING_TYPE_REQUIRED = {
    **SHORT_STRING_TYPE,
    "required": True,
    "empty": False,
}

NORMAL_STRING_TYPE = {
    **STRING_TYPE,
    "max_length": 100,
}

NORMAL_STRING_TYPE_REQUIRED = {
    **NORMAL_STRING_TYPE,
    "required": True,
    "empty": False,
}

LONG_STRING_TYPE = {
    **STRING_TYPE,
    "max_length": 500,
}

LONG_STRING_TYPE_REQUIRED = {
    **LONG_STRING_TYPE,
    "required": True,
    "empty": False,
}

INTEGER_TYPE = {
    "type": "integer",
}

INTEGER_TYPE_REQUIRED = {
    "type": "integer",
    "required": True,
}

DECIMAL_TYPE = {
    "type": "decimal",
}

DECIMAL_TYPE_REQUIRED = {
    "type": "decimal",
    "required": True,
}

BOOLEAN_TYPE = {"type": "boolean"}

BOOLEAN_TYPE_REQUIRED = {
    "type": "boolean",
    "required": True,
}

ACCOUNT_TYPE = {
    **STRING_TYPE,
    "max_length": 35,
    "regex": "([0-9|A-Z])*",
}

ACCOUNT_TYPE_REQUIRED = {
    **STRING_TYPE_REQUIRED,
    "max_length": 35,
    "regex": "([0-9|A-Z])*",
}

REG_TYPE = {
    **STRING_TYPE,
    "max_length": 15,
}

REG_TYPE_REQUIRED = {
    **REG_TYPE,
    "required": True,
    "empty": False,
}

CURRENCY_TYPE = {
    **STRING_TYPE,
    "max_length": 3,
    "regex": "[A-Z][A-Z][A-Z]",
}

CURRENCY_TYPE_REQUIRED = {
    **CURRENCY_TYPE,
    "required": True,
    "empty": False,
}
