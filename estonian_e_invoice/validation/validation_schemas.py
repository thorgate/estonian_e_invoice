from estonian_e_invoice.validation.validation_schema_types import *

HEADER_SCHEMA = {
    "Date": DATE_STRING_TYPE_REQUIRED,
    "FileID": SHORT_STRING_TYPE_REQUIRED,
    "Version": SHORT_STRING_TYPE_REQUIRED,
}

FOOTER_SCHEMA = {
    "TotalNumberInvoices": INTEGER_TYPE_REQUIRED,
    "TotalAmount": DECIMAL_TYPE_TWO_DECIMAL_PLACES_REQUIRED,
}

ACCOUNT_INFO_SCHEMA = {
    "AccountNumber": ACCOUNT_TYPE_REQUIRED,
    "IBAN": ACCOUNT_TYPE,
    "BIC": {**STRING_TYPE, "maxlength": 11,},
    "BankName": NORMAL_STRING_TYPE,
}

PAYMENT_INFO_SCHEMA = {
    "Currency": CURRENCY_TYPE_REQUIRED,
    "PaymentDescription": {**STRING_TYPE_REQUIRED, "maxlength": 210,},
    "Payable": {
        **SHORT_STRING_TYPE_REQUIRED,
        "coerce": "to_yes_no",
        "allowed": ["YES", "NO",],
    },
    "PaymentTotalSum": DECIMAL_TYPE_TWO_DECIMAL_PLACES_REQUIRED,
    "PayerName": NORMAL_STRING_TYPE_REQUIRED,
    "PaymentID": NORMAL_STRING_TYPE_REQUIRED,
    "PayToAccount": ACCOUNT_TYPE_REQUIRED,
    "PayToName": SHORT_STRING_TYPE_REQUIRED,
    "PaymentDueDate": DATE_STRING_TYPE,
}

ADDRESS_RECORD_SCHEMA = {
    "PostalAddress1": NORMAL_STRING_TYPE_REQUIRED,
    "PostalAddress2": NORMAL_STRING_TYPE,
    "City": NORMAL_STRING_TYPE_REQUIRED,
    "PostalCode": {**STRING_TYPE, "maxlength": 10,},
    "Country": NORMAL_STRING_TYPE,
}

CONTACT_DATA_SCHEMA = {
    "ContactName": NORMAL_STRING_TYPE,
    "ContactPersonCode": REG_TYPE,
    "PhoneNumber": NORMAL_STRING_TYPE,
    "FaxNumber": NORMAL_STRING_TYPE,
    "URL": NORMAL_STRING_TYPE,
    "EmailAddress": {
        **STRING_TYPE,
        "regex": ".+@.+",  # From the documentation, not a real good regex for emails.
    },
    "LegalAddress": LEGAL_ADDRESS_TYPE,
}

VAT_SCHEMA = {
    "VATRate": DECIMAL_TYPE_TWO_DECIMAL_PLACES_REQUIRED,
    "VATSum": DECIMAL_TYPE_FOUR_DECIMAL_PLACES_REQUIRED,
    "SumBeforeVAT": DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
    "SumAfterVAT": DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
    "Currency": CURRENCY_TYPE,
}

SELLER_PARTY_SCHEMA = {
    "Name": NORMAL_STRING_TYPE_REQUIRED,
    "RegNumber": REG_TYPE_REQUIRED,
    "VATRegNumber": REG_TYPE,
    "ContactData": CONTACT_DATA_TYPE,
    "AccountInfo": ACCOUNT_INFO_TYPE,
}

BUYER_PARTY_SCHEMA = {
    **SELLER_PARTY_SCHEMA,
    "RegNumber": REG_TYPE,
}

INVOICE_INFORMATION_SCHEMA = {
    "Type": INVOICE_TYPE_TYPE_REQUIRED,
    "InvoiceNumber": NORMAL_STRING_TYPE_REQUIRED,
    "InvoiceDate": DATE_STRING_TYPE_REQUIRED,
    "DocumentName": NORMAL_STRING_TYPE_REQUIRED,
    "DueDate": DATE_STRING_TYPE,
    "FineRatePerDay": DECIMAL_TYPE_TWO_DECIMAL_PLACES,
}

ITEM_DETAIL_INFO_SCHEMA = {
    "ItemUnit": SHORT_STRING_TYPE,
    "ItemAmount": DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
    "ItemPrice": DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
}

ITEM_ENTRY_SCHEMA = {
    "Description": LONG_STRING_TYPE_REQUIRED,
    "ItemSum": DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
    "ItemTotal": DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
    "ItemDetailInfo": ITEM_DETAIL_INFO_TYPE,
    "VAT": VAT_TYPE,
}

INVOICE_SUM_GROUP_SCHEMA = {
    "TotalSum": DECIMAL_TYPE_TWO_DECIMAL_PLACES_REQUIRED,
    "InvoiceSum": DECIMAL_TYPE_FOUR_DECIMAL_PLACES,
    "Currency": CURRENCY_TYPE,
    "TotalToPay": DECIMAL_TYPE_TWO_DECIMAL_PLACES,
    "VAT": VAT_TYPE,
}

INVOICE_ITEM_GROUP_SCHEMA = {
    "ItemEntry": {"type": "list", "schema": {"type": "item_entry",}, "required": True,}
}

INVOICE_TYPE_VALIDATION_SCHEMA = {
    "Type": {**STRING_TYPE_REQUIRED, "maxlength": 3, "allowed": ["DEB", "CRE",],},
    "SourceInvoice": SHORT_STRING_TYPE,
}

INVOICE_SCHEMA = {
    "invoiceId": NORMAL_STRING_TYPE_REQUIRED,
    "serviceId": SHORT_STRING_TYPE_REQUIRED,
    "regNumber": REG_TYPE_REQUIRED,
    "sellerRegnumber": REG_TYPE_REQUIRED,
    "InvoiceParties": {
        "type": "list",
        "schema": {"type": "invoice_party",},
        "required": True,
    },
    "InvoiceInformation": INVOICE_INFORMATION_TYPE_REQUIRED,
    "InvoiceSumGroup": INVOICE_SUM_GROUP_TYPE_REQUIRED,
    "InvoiceItemGroup": INVOICE_ITEM_GROUP_TYPE_REQUIRED,
    "PaymentInfo": PAYMENT_INFO_TYPE_REQUIRED,
}
