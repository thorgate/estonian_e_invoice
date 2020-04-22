"""
Validation schema types for Cerberus validator.

They are based on the variable type definitions in the e-invoice document.

For further understanding and improvements on the schema types, you might
check the following references.

Reference for Cerberus: https://docs.python-cerberus.org/en/stable/
Reference for the document: https://wp.itl.ee/files/Estonian_e-invoice_description_ver1.2_eng.pdf
"""


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
    "check_with": "two_decimal_places",
}

DECIMAL_TYPE_TWO_DECIMAL_PLACES_REQUIRED = {
    **DECIMAL_TYPE_TWO_DECIMAL_PLACES,
    "required": True,
}

DECIMAL_TYPE_FOUR_DECIMAL_PLACES = {
    **DECIMAL_TYPE,
    "check_with": "four_decimal_places",
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

VAT_TYPE = {
    "type": "vat",
}

VAT_TYPE_REQUIRED = {
    **VAT_TYPE,
    "required": True,
}

LEGAL_ADDRESS_TYPE = {
    "type": "legal_address",
}

LEGAL_ADDRESS_TYPE_REQUIRED = {
    **LEGAL_ADDRESS_TYPE,
    "required": True,
}

CONTACT_DATA_TYPE = {
    "type": "contact_data",
}

CONTACT_DATA_TYPE_REQUIRED = {
    **CONTACT_DATA_TYPE,
    "required": True,
}

ACCOUNT_INFO_TYPE = {
    "type": "account_info",
}

ACCOUNT_INFO_TYPE_REQUIRED = {
    **ACCOUNT_INFO_TYPE,
    "required": True,
}

INVOICE_TYPE_TYPE = {
    "type": "invoice_type",
}

INVOICE_TYPE_TYPE_REQUIRED = {
    **INVOICE_TYPE_TYPE,
    "required": True,
}

ITEM_DETAIL_INFO_TYPE = {
    "type": "item_detail_info",
}

ITEM_DETAIL_INFO_TYPE_REQUIRED = {
    **ITEM_DETAIL_INFO_TYPE,
    "required": True,
}

ITEM_ENTRY_TYPE = {
    "type": "item_entry",
}

ITEM_ENTRY_TYPE_REQUIRED = {
    **ITEM_ENTRY_TYPE,
    "required": True,
}

INVOICE_INFORMATION_TYPE = {
    "type": "invoice_information",
}

INVOICE_INFORMATION_TYPE_REQUIRED = {
    **INVOICE_INFORMATION_TYPE,
    "required": True,
}

INVOICE_SUM_GROUP_TYPE = {
    "type": "invoice_sum_group",
}

INVOICE_SUM_GROUP_TYPE_REQUIRED = {
    **INVOICE_SUM_GROUP_TYPE,
    "required": True,
}

INVOICE_ITEM_GROUP_TYPE = {
    "type": "invoice_item_group",
}

INVOICE_ITEM_GROUP_TYPE_REQUIRED = {
    **INVOICE_ITEM_GROUP_TYPE,
    "required": True,
}

PAYMENT_INFO_TYPE = {
    "type": "payment_info",
}

PAYMENT_INFO_TYPE_REQUIRED = {
    **PAYMENT_INFO_TYPE,
    "required": True,
}

INVOICE_PARTY_TYPE = {
    "type": "invoice_party",
}

INVOICE_PARTY_TYPE_REQUIRED = {
    **INVOICE_PARTY_TYPE,
    "required": True,
}
