from datetime import datetime
from decimal import Decimal

from cerberus import TypeDefinition, Validator

from estonian_e_invoice.entities import (
    VAT,
    LegalAddress,
    ContactData,
    AccountInfo,
    InvoiceType,
    ItemDetailInfo,
    InvoiceInformation,
    InvoiceItemGroup,
    InvoiceSumGroup,
    PaymentInfo,
    SellerParty,
    BuyerParty,
    ItemEntry,
)

DECIMAL_TYPE = TypeDefinition("decimal", (Decimal,), ())
VAT_TYPE = TypeDefinition("vat", (VAT,), ())
LEGAL_ADDRESS_TYPE = TypeDefinition("legal_address", (LegalAddress,), ())
CONTACT_DATA_TYPE = TypeDefinition("contact_data", (ContactData,), ())
ACCOUNT_INFO_TYPE = TypeDefinition("account_info", (AccountInfo,), ())
INVOICE_TYPE_TYPE = TypeDefinition("invoice_type", (InvoiceType,), ())
ITEM_DETAIL_INFO_TYPE = TypeDefinition("item_detail_info", (ItemDetailInfo,), ())
INVOICE_INFORMATION_TYPE = TypeDefinition(
    "invoice_information", (InvoiceInformation,), ()
)
INVOICE_ITEM_GROUP_TYPE = TypeDefinition("invoice_item_group", (InvoiceItemGroup,), ())
INVOICE_SUM_GROUP_TYPE = TypeDefinition("invoice_sum_group", (InvoiceSumGroup,), ())
PAYMENT_INFO_TYPE = TypeDefinition("payment_info", (PaymentInfo,), ())
ITEM_ENTRY_TYPE = TypeDefinition("item_entry", (ItemEntry,), ())
INVOICE_PARTY_TYPE = TypeDefinition("invoice_party", (SellerParty, BuyerParty,), ())


class CustomValidator(Validator):
    types_mapping = Validator.types_mapping.copy()
    types_mapping["decimal"] = DECIMAL_TYPE
    types_mapping["vat"] = VAT_TYPE
    types_mapping["legal_address"] = LEGAL_ADDRESS_TYPE
    types_mapping["contact_data"] = CONTACT_DATA_TYPE
    types_mapping["account_info"] = ACCOUNT_INFO_TYPE
    types_mapping["invoice_type"] = INVOICE_TYPE_TYPE
    types_mapping["item_detail_info"] = ITEM_DETAIL_INFO_TYPE
    types_mapping["invoice_information"] = INVOICE_INFORMATION_TYPE
    types_mapping["invoice_item_group"] = INVOICE_ITEM_GROUP_TYPE
    types_mapping["invoice_sum_group"] = INVOICE_SUM_GROUP_TYPE
    types_mapping["payment_info"] = PAYMENT_INFO_TYPE
    types_mapping["item_entry"] = ITEM_ENTRY_TYPE
    types_mapping["invoice_party"] = INVOICE_PARTY_TYPE

    # Custom validators
    def _check_with_date_string(self, field, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            self._error(field, "Date should be in %Y-%m-%d format")

    def check_with_decimal_places(self, field, value, num_decimal_places):
        if isinstance(value, Decimal):
            if value.as_tuple().exponent != -num_decimal_places:
                self._error(field, f"must have {num_decimal_places} decimal places")
        else:
            self._error(field, "must be of a decimal type")

    def _check_with_two_decimal_places(self, field, value):
        self.check_with_decimal_places(field, value, 2)

    def _check_with_four_decimal_places(self, field, value):
        self.check_with_decimal_places(field, value, 4)

    # Custom coarces
    def _normalize_coerce_to_yes_no(self, value):
        return "YES" if value else "NO"
