from estonian_e_invoice.validation.validation_schema_types import *


HEADER_VALIDATION_SCHEMA = {
    "date": DATE_TYPE_REQUIRED,
    "file_id": SHORT_STRING_TYPE_REQUIRED,
    "version": SHORT_STRING_TYPE_REQUIRED,
}

FOOTER_VALIDATION_SCHEMA = {
    "invoices_count": INTEGER_TYPE_REQUIRED,
    "total_amount": DECIMAL_TYPE_REQUIRED,
}

ACCOUNT_INFO_VALIDATION_SCHEMA = {
    "account_number": ACCOUNT_TYPE_REQUIRED,
    "iban": ACCOUNT_TYPE,
    "bic": {
        **STRING_TYPE,
        "max_length": 11,
    },
    "bank_name": NORMAL_STRING_TYPE
}

PAYMENT_INFO_VALIDATION_SCHEMA = {
    "currency": CURRENCY_TYPE_REQUIRED,
    "payment_description": {
        **STRING_TYPE_REQUIRED,
        "max_length": 210,
    },
    "payable": BOOLEAN_TYPE_REQUIRED,
    "payment_total_sum": DECIMAL_TYPE_REQUIRED,
    "payer_name": NORMAL_STRING_TYPE_REQUIRED,
    "payment_id": NORMAL_STRING_TYPE_REQUIRED,
    "pay_to_account": ACCOUNT_TYPE_REQUIRED,
    "pay_to_name": SHORT_STRING_TYPE_REQUIRED,
    "payment_due_date": DATE_TYPE,
}

ADDRESS_RECORD_VALIDATION_SCHEMA = {
    "tag": NORMAL_STRING_TYPE_REQUIRED,
    "postal_address_1": NORMAL_STRING_TYPE_REQUIRED,
    "postal_address_2": NORMAL_STRING_TYPE,
    "city": NORMAL_STRING_TYPE_REQUIRED,
    "postal_code": {
        **STRING_TYPE,
        "max_length": 10,
    }
}

CONTACT_DATA_VALIDATION_SCHEMA = {
    "contact_name": NORMAL_STRING_TYPE,
    "contact_person_code": REG_TYPE,
    "phone_number": NORMAL_STRING_TYPE,
    "fax_number": NORMAL_STRING_TYPE,
    "url": NORMAL_STRING_TYPE,
    "email_address": {
        **STRING_TYPE,
        "regex": ".+@.+",  # From the documentation, not a real good regex for emails.
    },
}

VAT_VALIDATION_SCHEMA = {
    "vat_rate": DECIMAL_TYPE_REQUIRED,
    "vat_sum": DECIMAL_TYPE_REQUIRED,
    "sum_before_vat": DECIMAL_TYPE,
    "sum_after_vat": DECIMAL_TYPE,
    "total_vat_sum": DECIMAL_TYPE,
}


SELLER_PARTY_SCHEMA = {
    "name": NORMAL_STRING_TYPE_REQUIRED,
    "reg_number": REG_TYPE_REQUIRED,
    "vat_reg_number": REG_TYPE
}

BUYER_PARTY_SCHEMA = {
    **SELLER_PARTY_SCHEMA,
    "reg_number": REG_TYPE,
}

INVOICE_INFORMATION_SCHEMA = {
    "invoice_type": {
        **STRING_TYPE_REQUIRED,
        "max_length": 3,
        "allowed": ["DEB", "CRE", ]
    },
    "invoice_number": NORMAL_STRING_TYPE_REQUIRED,
    "invoice_date": DATE_TYPE_REQUIRED,
    "document_name": NORMAL_STRING_TYPE_REQUIRED,
    "due_date": DATE_TYPE,
    "fine_rate_per_day": DECIMAL_TYPE,
}


ITEM_DETAIL_INFO_SCHEMA = {
    "item_unit": SHORT_STRING_TYPE,
    "item_amount": DECIMAL_TYPE,
    "item_price": DECIMAL_TYPE
}

ITEM_ENTRY_SCHEMA = {
    "description": LONG_STRING_TYPE_REQUIRED,
    "item_sum": DECIMAL_TYPE,
    "item_total": DECIMAL_TYPE,
}

INVOICE_SUM_GROUP_VALIDATION_SCHEMA = {
    "total_sum": DECIMAL_TYPE_REQUIRED,
    "invoice_sum": DECIMAL_TYPE,
    "currency": CURRENCY_TYPE,
    "total_to_pay": DECIMAL_TYPE,
}

INVOICE_VALIDATION_SCHEMA = {
    "invoice_id": NORMAL_STRING_TYPE_REQUIRED,
    "service_id": SHORT_STRING_TYPE_REQUIRED,
    "reg_number": REG_TYPE_REQUIRED,
    "seller_reg_number": REG_TYPE_REQUIRED
}
