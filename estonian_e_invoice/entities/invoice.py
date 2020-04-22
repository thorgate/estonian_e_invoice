from decimal import Decimal
from typing import List, Optional

from estonian_e_invoice.entities import AccountInfo, ContactData, PaymentInfo
from estonian_e_invoice.entities.common import Node
from estonian_e_invoice.validation.validation_schemas import (
    BUYER_PARTY_SCHEMA,
    INVOICE_INFORMATION_SCHEMA,
    INVOICE_ITEM_GROUP_SCHEMA,
    INVOICE_SCHEMA,
    INVOICE_SUM_GROUP_SCHEMA,
    INVOICE_TYPE_VALIDATION_SCHEMA,
    ITEM_DETAIL_INFO_SCHEMA,
    ITEM_ENTRY_SCHEMA,
    SELLER_PARTY_SCHEMA,
    VAT_SCHEMA,
)


class VAT(Node):
    """
    Describes value-added tax.

        vat_rate: VAT rate
        vat_sum: VAT amount
        sum_before_vat: Amount of which the VAT is calculated.
        sum_after_vat: Amount with VAT amount.
        currency: VAT currency
    """

    tag = "VAT"
    validation_schema = VAT_SCHEMA

    def __init__(
        self,
        vat_rate: Decimal,
        vat_sum: Decimal,
        sum_before_vat: Optional[Decimal] = None,
        sum_after_vat: Optional[Decimal] = None,
        currency: Optional[str] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "VATRate": vat_rate,
                "VATSum": vat_sum,
                "SumBeforeVAT": sum_before_vat,
                "SumAfterVAT": sum_after_vat,
                "Currency": currency,
            }
        )


class SellerParty(Node):
    """
    Defines SellerParty involved with the invoice. Differs from the buyer party
    by the mandatory register code.

        name: Name of the party of the invoice.
        reg_number: Registration number of the party.
        vat_reg_number: VAT registration number of the party.
        contact_data: Contact information of the party (phone number, e-mail, address).
        account_info: Describes the accounts of the party.
    """

    tag = "SellerParty"
    validation_schema = SELLER_PARTY_SCHEMA

    def __init__(
        self,
        name: str,
        reg_number: str,
        vat_reg_number: Optional[str] = None,
        contact_data: Optional[ContactData] = None,
        account_info: Optional[AccountInfo] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "Name": name,
                "RegNumber": reg_number,
                "VATRegNumber": vat_reg_number,
                "ContactData": contact_data,
                "AccountInfo": account_info,
            }
        )


class BuyerParty(SellerParty):
    """Defines the buyer of the invoice"""

    tag = "BuyerParty"
    validation_schema = BUYER_PARTY_SCHEMA

    def __init__(
        self,
        name: str,
        reg_number: Optional[str] = None,
        vat_reg_number: Optional[str] = None,
        contact_data: Optional[ContactData] = None,
        account_info: Optional[AccountInfo] = None,
    ) -> None:
        super().__init__(
            name=name,
            reg_number=reg_number,
            vat_reg_number=vat_reg_number,
            contact_data=contact_data,
            account_info=account_info,
        )


class InvoiceType(Node):
    """"
    Invoice type.

        invoice_type: Invoice type. DEB – debit invoice, CRE – credit invoice.
    """

    tag = "Type"
    validation_schema = INVOICE_TYPE_VALIDATION_SCHEMA

    def __init__(self, invoice_type: str, source_invoice: Optional[str] = None):
        validated_data = self.validate(
            {"Type": invoice_type, "SourceInvoice": source_invoice,}
        )
        self.attributes = {
            "type": validated_data["Type"],
        }

        source_invoice = validated_data.get("SourceInvoice")
        if source_invoice:
            self.elements = {
                "SourceInvoice": source_invoice,
            }


class InvoiceInformation(Node):
    """
    Contains general invoice specific information about the invoice, like invoice number and dates.

        invoice_type: Type of the invoice.
        invoice_number: Number of the invoice.
        invoice_date: Invoice date.
        document_name: Name of the document (ex: invoice, credit invoice, waybill etc).
        due_date: Invoice due date.
        fine_rate_per_day: Fine rate per day. Shown in percent.
    """

    tag = "InvoiceInformation"
    validation_schema = INVOICE_INFORMATION_SCHEMA

    def __init__(
        self,
        invoice_type: InvoiceType,
        invoice_number: str,
        invoice_date: str,
        document_name: str,
        due_date: Optional[str] = None,
        fine_rate_per_day: Optional[Decimal] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "Type": invoice_type,
                "InvoiceNumber": invoice_number,
                "InvoiceDate": invoice_date,
                "DocumentName": document_name,
                "DueDate": due_date,
                "FineRatePerDay": fine_rate_per_day,
            }
        )


class ItemDetailInfo(Node):
    """
    Detailed information of products/services.

        item_unit: Unit (e.g: h, kg, l, kWh).
        item_amount: Amount of the products /services.
        item_price: Price of one product or service (without taxes).
    """

    tag = "ItemDetailInfo"
    validation_schema = ITEM_DETAIL_INFO_SCHEMA

    def __init__(
        self,
        item_unit: Optional[str] = None,
        item_amount: Optional[Decimal] = None,
        item_price: Optional[Decimal] = None,
    ):
        self.elements = self.validate(
            {"ItemUnit": item_unit, "ItemAmount": item_amount, "ItemPrice": item_price,}
        )


class ItemEntry(Node):
    """
    Describes detailed info about one specific invoice row.

        description: Product/service/article name or description.
        item_sum: Total amount without taxes and discount.
        vat: Describes value-added tax
        item_total: Total amount including taxes.
        item_detail_info: Detailed information of products/services.
    """

    tag = "ItemEntry"
    validation_schema = ITEM_ENTRY_SCHEMA

    def __init__(
        self,
        description: str,
        item_sum: Optional[Decimal] = None,
        vat: Optional[VAT] = None,
        item_total: Optional[Decimal] = None,
        item_detail_info: Optional[ItemDetailInfo] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "Description": description,
                "ItemSum": item_sum,
                "VAT": vat,
                "ItemTotal": item_total,
                "ItemDetailInfo": item_detail_info,
            }
        )


class InvoiceItemGroup(Node):
    """
    The main group on invoice rows. Group of invoice items or invoice rows

        invoice_item_entries: Describes one specific invoice row entries.
    """

    tag = "InvoiceItemGroup"
    validation_schema = INVOICE_ITEM_GROUP_SCHEMA

    def __init__(self, invoice_item_entries: List[ItemEntry],) -> None:
        self.elements = self.validate({"ItemEntry": invoice_item_entries,})


class InvoiceSumGroup(Node):
    """
    Contains invoiced amounts (total sum, sum_before_var etc).

        total_sum: Invoice total sum.
        invoice_sum: Amount of the invoice without tax.
        currency: Three-character currency code as specified in ISO 4217.
        total_to_pay: Amout to be paid. Credit invoice must have 0.00.
                      Negative amounts does not correspond to the Estonian legislation.
        vat: Describes value-added tax.
    """

    tag = "InvoiceSumGroup"
    validation_schema = INVOICE_SUM_GROUP_SCHEMA

    def __init__(
        self,
        total_sum: Decimal,
        invoice_sum: Optional[Decimal] = None,
        currency: Optional[str] = None,
        total_to_pay: Optional[Decimal] = None,
        vat: Optional[VAT] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "TotalSum": total_sum,
                "InvoiceSum": invoice_sum,
                "Currency": currency,
                "TotalToPay": total_to_pay,
                "VAT": vat,
            }
        )


class Invoice(Node):
    """
    Contains information about one specific invoice.

        invoice_id: Unique id of the invoice (on the scope of one file).
        reg_number: Personal ID/registration code of the invoice receiver.
        seller_reg_number: Seller’s registration number.
        seller_party: Sender of the invoice.
        buyer_party: Receiver of the invoice.
        invoice_information: Contains general information about the invoice.
        invoice_sum_group: Information block for invoiced amounts.
        invoice_item_group: The main group on invoice rows. Group of invoice items or invoice rows.
    """

    tag = "Invoice"
    validation_schema = INVOICE_SCHEMA

    def __init__(
        self,
        invoice_id: str,
        reg_number: str,
        seller_reg_number: str,
        seller_party: SellerParty,
        buyer_party: BuyerParty,
        invoice_information: InvoiceInformation,
        invoice_sum_group: InvoiceSumGroup,
        invoice_item_group: InvoiceItemGroup,
        payment_info: PaymentInfo,
    ) -> None:
        validated_data = self.validate(
            {
                "invoiceId": invoice_id,
                "regNumber": reg_number,
                "sellerRegnumber": seller_reg_number,
                "InvoiceParties": [seller_party, buyer_party],
                "InvoiceInformation": invoice_information,
                "InvoiceSumGroup": invoice_sum_group,
                "InvoiceItemGroup": invoice_item_group,
                "PaymentInfo": payment_info,
            }
        )
        self.attributes = {
            "invoiceId": validated_data["invoiceId"],
            "regNumber": validated_data["regNumber"],
            "sellerRegnumber": validated_data["sellerRegnumber"],
        }
        self.elements = {
            "InvoiceParties": validated_data["InvoiceParties"],
            "InvoiceInformation": validated_data["InvoiceInformation"],
            "InvoiceSumGroup": validated_data["InvoiceSumGroup"],
            "InvoiceItemGroup": validated_data["InvoiceItemGroup"],
            "PaymentInfo": validated_data["PaymentInfo"],
        }
