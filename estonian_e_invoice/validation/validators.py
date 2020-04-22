from datetime import datetime
from decimal import Decimal

from cerberus import Validator
from estonian_e_invoice.validation.validator_custom_types import (
    ACCOUNT_INFO_TYPE,
    CONTACT_DATA_TYPE,
    DECIMAL_TYPE,
    INVOICE_INFORMATION_TYPE,
    INVOICE_ITEM_TYPE,
    INVOICE_PARTY_TYPE,
    INVOICE_SUM_GROUP_TYPE,
    INVOICE_TYPE_TYPE,
    ITEM_DETAIL_INFO_TYPE,
    ITEM_ENTRY_TYPE,
    LEGAL_ADDRESS_TYPE,
    PAYMENT_INFO_TYPE,
    VAT_TYPE,
)


class CustomValidator(Validator):
    types_mapping = {
        **Validator.types_mapping,
        "decimal": DECIMAL_TYPE,
        "vat": VAT_TYPE,
        "legal_address": LEGAL_ADDRESS_TYPE,
        "contact_data": CONTACT_DATA_TYPE,
        "account_info": ACCOUNT_INFO_TYPE,
        "invoice_type": INVOICE_TYPE_TYPE,
        "item_detail_info": ITEM_DETAIL_INFO_TYPE,
        "invoice_information": INVOICE_INFORMATION_TYPE,
        "invoice_item": INVOICE_ITEM_TYPE,
        "invoice_sum_group": INVOICE_SUM_GROUP_TYPE,
        "payment_info": PAYMENT_INFO_TYPE,
        "item_entry": ITEM_ENTRY_TYPE,
        "invoice_party": INVOICE_PARTY_TYPE,
    }

    # Custom validators
    def _check_with_date_string(self, field, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            self._error(field, "Date should be in %Y-%m-%d format")

    def check_with_decimal_places(self, field, value, num_decimal_places):
        if isinstance(value, Decimal):
            if -value.as_tuple().exponent > num_decimal_places:
                self._error(
                    field,
                    "must not have more than {num_decimal_places} decimal places".format(
                        num_decimal_places=num_decimal_places
                    ),
                )
        else:
            self._error(field, "must be of a decimal type")

    def _check_with_two_decimal_places(self, field, value):
        self.check_with_decimal_places(field, value, 2)

    def _check_with_four_decimal_places(self, field, value):
        self.check_with_decimal_places(field, value, 4)

    # Custom coarces
    def _normalize_coerce_to_yes_no(self, value):
        return "YES" if value else "NO"
