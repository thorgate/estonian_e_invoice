from decimal import Decimal

from cerberus import TypeDefinition
from estonian_e_invoice.entities import (
    VAT,
    AccountInfo,
    BuyerParty,
    ContactData,
    InvoiceInformation,
    InvoiceItem,
    InvoiceSumGroup,
    InvoiceType,
    ItemDetailInfo,
    ItemEntry,
    LegalAddress,
    PaymentInfo,
    SellerParty,
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
INVOICE_ITEM_TYPE = TypeDefinition("invoice_item", (InvoiceItem,), ())
INVOICE_SUM_GROUP_TYPE = TypeDefinition("invoice_sum_group", (InvoiceSumGroup,), ())
PAYMENT_INFO_TYPE = TypeDefinition("payment_info", (PaymentInfo,), ())
ITEM_ENTRY_TYPE = TypeDefinition("item_entry", (ItemEntry,), ())
INVOICE_PARTY_TYPE = TypeDefinition("invoice_party", (SellerParty, BuyerParty,), ())
