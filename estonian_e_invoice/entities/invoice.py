import datetime
from decimal import Decimal
from typing import Optional, List

from estonian_e_invoice.entities.account import AccountInfo, PaymentInfo
from estonian_e_invoice.entities.common import Node
from estonian_e_invoice.entities.contact import ContactData


class VAT(Node):
    """
    Describes value-added tax.

        vat_rate: VAT rate
        vat_sum: VAT amount
        total_vat_sum: Total of all VAT sums.
        sum_before_vat: Amount of which the VAT is calculated.
        sum_after_vat: Amount with VAT amount.
    """

    tag = "Vat"

    def __init__(
        self,
        vat_rate: Decimal,
        vat_sum: Decimal,
        sum_before_vat: Optional[Decimal] = None,
        sum_after_vat: Optional[Decimal] = None,
        total_vat_sum: Optional[Decimal] = None,
    ) -> None:
        self.elements = {
            "VATRate": vat_rate,
            "VATSum": vat_sum,
            "SumBeforeVAT": sum_before_vat,
            "SumAfterVAT": sum_after_vat,
            "TotalVATSum": total_vat_sum,
        }


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

    def __init__(
        self,
        name: str,
        reg_number: str,
        vat_reg_number: Optional[str] = None,
        contact_data: Optional[ContactData] = None,
        account_info: Optional[AccountInfo] = None,
    ) -> None:
        self.elements = {
            "Name": name,
            "RegNumber": reg_number,
            "VATRegNumber": vat_reg_number,
            "ContactData": contact_data,
            "AccountInfo": account_info,
        }


class BuyerParty(SellerParty):
    """Defines the buyer of the invoice"""

    tag = "BuyerParty"

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


class InvoiceInformation(Node):
    """
    Contains general invoice specific information about the invoice, like invoice number and dates.

        invoice_type: Invoice type. DEB – debit invoice, CRE – credit invoice.
        invoice_number: Number of invoice,
        invoice_date: datetime.date,
        document_name: str,
        due_date: Optional[datetime.date] = None,
        fine_rate_per_day: Optional[Decimal] = None,
    """

    tag = "InvoiceInformation"

    def __init__(
        self,
        invoice_type: str,
        invoice_number: str,
        invoice_date: datetime.date,
        document_name: str,
        due_date: Optional[datetime.date] = None,
        fine_rate_per_day: Optional[Decimal] = None,
    ) -> None:
        self.elements = {
            "Type": invoice_type,
            "InvoiceNumber": invoice_number,
            "InvoiceDate": invoice_date,
            "DocumentName": document_name,
            "DueDate": due_date,
            "FineRatePerDay": fine_rate_per_day,
        }


class ItemDetailInfo(Node):
    """
    Detailed information of products/services.

        item_unit: Unit (e.g: h, kg, l, kWh).
        item_amount: Amount of the products /services.
        item_price: Price of one product or service (without taxes).
    """

    tag = "ItemDetailInfo"

    def __init__(
        self,
        item_unit: Optional[str] = None,
        item_amount: Optional[Decimal] = None,
        item_price: Optional[Decimal] = None,
    ):
        self.elements = {
            "ItemUnit": item_unit,
            "ItemAmount": item_amount,
            "ItemPrice": item_price,
        }


class ItemEntry(Node):
    """
    Describes detailed info about one specific invoice row.

        description: Product/service/article name or description.
        item_sum: Total amount without taxes and discount.
        vat: Describes value-added tax
        item_total: Total amount including taxes.
    """

    tag = "ItemEntry"

    def __init__(
        self,
        description: str,
        item_sum: Optional[Decimal] = None,
        vat: Optional[VAT] = None,
        item_total: Optional[Decimal] = None,
        item_detail_info: Optional[ItemDetailInfo] = None,
    ) -> None:
        self.elements = {
            "Description": description,
            "ItemSum": item_sum,
            "VAT": vat,
            "ItemTotal": item_total,
            "ItemDetailInfo": item_detail_info,
        }


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

    def __init__(
        self,
        total_sum: Decimal,
        invoice_sum: Optional[Decimal] = None,
        currency: Optional[str] = None,
        total_to_pay: Optional[Decimal] = None,
        vat: Optional[VAT] = None,
    ) -> None:
        self.elements = {
            "TotalSum": total_sum,
            "InvoiceSum": invoice_sum,
            "Currency": currency,
            "TotalToPay": total_to_pay,
            "VAT": vat,
        }


class Invoice(Node):
    """
    Contains information about one specific invoice.

        invoice_id: Unique id of the invoice (on the scope of one file).
        service_id: Client identification number (reference number, client code, client number etc.) in sellers system.
        reg_number: Personal ID/registration code of the invoice receiver.
        seller_reg_number: Seller’s registration number.
        seller_party: Sender of the invoice.
        buyer_party: Receiver of the invoice.
        invoice_information: Contains general information about the invoice.
        invoice_sum_group: Information block for invoiced amounts.
        invoice_item: Contains detailed information about the invoice rows.
    """

    tag = "Invoice"

    def __init__(
        self,
        invoice_id: str,
        service_id: str,
        reg_number: str,
        seller_reg_number: str,
        seller_party: SellerParty,
        buyer_party: BuyerParty,
        invoice_information: InvoiceInformation,
        invoice_sum_group: InvoiceSumGroup,
        invoice_item_entries: List[ItemEntry],
    ) -> None:
        self.attributes = {
            "invoiceId": invoice_id,
            "serviceId": service_id,
            "regNumber": reg_number,
            "sellerRegnumber": seller_reg_number,
        }
        self.elements = {
            "InvoiceParties": [seller_party, buyer_party],
            "InvoiceInformation": invoice_information,
            "InvoiceSumGroup": invoice_sum_group,
            "InvoiceItem": invoice_item_entries,
        }
