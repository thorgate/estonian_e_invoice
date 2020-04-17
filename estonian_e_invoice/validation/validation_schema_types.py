STRING_TYPE = {
    "type": "string",
    "empty": False,
}

STRING_TYPE_REQUIRED = {
    **STRING_TYPE,
    "required": True,
}

SHORT_STRING_TYPE = {
    **STRING_TYPE,
    "maxlength": 20,
}

SHORT_STRING_TYPE_REQUIRED = {
    **SHORT_STRING_TYPE,
    "required": True,
}

NORMAL_STRING_TYPE = {
    **STRING_TYPE,
    "maxlength": 100,
}

NORMAL_STRING_TYPE_REQUIRED = {
    **NORMAL_STRING_TYPE,
    "required": True,
}

LONG_STRING_TYPE = {
    **STRING_TYPE,
    "maxlength": 500,
}

LONG_STRING_TYPE_REQUIRED = {
    **LONG_STRING_TYPE,
    "required": True,
}

DATE_STRING_TYPE = {
    **SHORT_STRING_TYPE,
    "check_with": "date_string",
}

DATE_STRING_TYPE_REQUIRED = {
    **DATE_STRING_TYPE,
    "required": True,
}

INTEGER_TYPE = {
    "type": "integer",
}

INTEGER_TYPE_REQUIRED = {
    **INTEGER_TYPE,
    "required": True,
}

DECIMAL_TYPE = {
    "type": "decimal",
}

DECIMAL_TYPE_REQUIRED = {
    **DECIMAL_TYPE,
    "required": True,
}

DECIMAL_TYPE_TWO_DECIMAL_PLACES = {
    **DECIMAL_TYPE,
    "coerce": "two_decimal_places",
}

DECIMAL_TYPE_TWO_DECIMAL_PLACES_REQUIRED = {
    **DECIMAL_TYPE_TWO_DECIMAL_PLACES,
    "required": True,
}

DECIMAL_TYPE_FOUR_DECIMAL_PLACES = {
    **DECIMAL_TYPE,
    "coerce": "four_decimal_places",
}

DECIMAL_TYPE_FOUR_DECIMAL_PLACES_REQUIRED = {
    **DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
    "required": True,
}

ACCOUNT_TYPE = {
    **STRING_TYPE,
    "maxlength": 35,
    "regex": "([0-9|A-Z])*",
}

ACCOUNT_TYPE_REQUIRED = {
    **ACCOUNT_TYPE,
    "required": True,
}

REG_TYPE = {
    **STRING_TYPE,
    "maxlength": 15,
}

REG_TYPE_REQUIRED = {
    **REG_TYPE,
    "required": True,
}

CURRENCY_TYPE = {
    **STRING_TYPE,
    "maxlength": 3,
    "regex": "[A-Z][A-Z][A-Z]",
}

CURRENCY_TYPE_REQUIRED = {
    **CURRENCY_TYPE,
    "required": True,
}

NODE_TYPE = {
    "type": "node",
}

NODE_TYPE_REQUIRED = {
    **NODE_TYPE,
    "required": True,
}
