import datetime
from decimal import Decimal
from typing import Optional, List

from entities.account import AccountInfo, PaymentInfo
from entities.contact import ContactData


class VAT:
    """
    Describes value-added tax.

        vat_rate: VAT rate
        vat_sum: VAT amount
        total_vat_sum: Total of all VAT sums.
        sum_before_vat: Amount of which the VAT is calculated.
        sum_after_vat: Amount with VAT amount.
    """

    def __init__(
        self,
        vat_rate: Decimal,
        vat_sum: Decimal,
        sum_before_vat: Optional[Decimal] = None,
        sum_after_vat: Optional[Decimal] = None,
        total_vat_sum: Optional[Decimal] = None,
    ) -> None:
        self.vat_rate = vat_rate
        self.vat_sum = vat_sum
        self.sum_before_vat = sum_before_vat
        self.sum_after_var = sum_after_vat
        self.total_vat_sum = total_vat_sum


class InvoiceParty:
    """
    Defines different companies/persons involved with the invoice (the seller and the buyer, the
    recipient of the invoice, the recipient of the products/services and the payer of the invoice)

        name: Name of the party of the invoice.
        reg_number: Registration number of the party.
        gln: Party’s GLN-code.
        transaction_partner_code: Transaction partner code issued by Estonian government.
        unique_code: Unique code of the party (e.g: client number).
        dep_id: Department identifier (e.g: sales).
        vat_reg_number: VAT registration number of the party.
        contact_data: Contact information of the party (phone number, e-mail, address).
        account_info: Describes the accounts of the party.
        extension: Describes additional information elements.
    """

    def __init__(
        self,
        name: str,
        reg_number: str,
        gln: Optional[str] = None,
        transaction_partner_code: Optional[str] = None,
        unique_code: Optional[str] = None,
        dep_id: Optional[str] = None,
        vat_reg_number: Optional[str] = None,
        contact_data: Optional[ContactData] = None,
        account_info: Optional[AccountInfo] = None,
    ) -> None:
        self.name = name
        self.reg_number = reg_number
        self.gln = gln
        self.transaction_partner_code = transaction_partner_code
        self.unique_code = unique_code
        self.dep_id = dep_id
        self.vat_reg_number = vat_reg_number
        self.contact_data = contact_data
        self.account_info = account_info


class InvoiceInformation:
    """
    Contains general invoice specific information about the invoice, like invoice number and dates.

        invoice_type: Invoice type. DEB – debit invoice, CRE – credit invoice.
        invoice_number: Number of invoice,
        invoice_date: datetime.date,
        document_name: str,
        source_invoice: Optional[str] = None,
        factor_contract_number: Optional[str] = None,
        contract_number: Optional[str] = None,
        invoice_content_code: Optional[str] = None,
        invoice_content_text: Optional[str] = None,
        payment_reference_number: Optional[str] = None,
        payment_method: Optional[str] = None,
        due_date: Optional[datetime.date] = None,
        payment_term: Optional[str] = None,
        fine_rate_per_day: Optional[Decimal] = None,
    """

    def __init__(
        self,
        invoice_type: str,
        invoice_number: str,
        invoice_date: datetime.date,
        document_name: str,
        source_invoice: Optional[str] = None,
        factor_contract_number: Optional[str] = None,
        contract_number: Optional[str] = None,
        invoice_content_code: Optional[str] = None,
        invoice_content_text: Optional[str] = None,
        payment_reference_number: Optional[str] = None,
        payment_method: Optional[str] = None,
        due_date: Optional[datetime.date] = None,
        payment_term: Optional[str] = None,
        fine_rate_per_day: Optional[Decimal] = None,
    ) -> None:
        self.invoice_type = invoice_type
        self.invoice_number = invoice_number
        self.invoice_date = invoice_date
        self.document_name = document_name
        self.source_invoice = source_invoice
        self.factor_contract_number = factor_contract_number
        self.contract_number = contract_number
        self.invoice_content_code = invoice_content_code
        self.invoice_content_text = invoice_content_text
        self.payment_reference_number = payment_reference_number
        self.payment_method = payment_method
        self.due_date = due_date
        self.payment_term = payment_term
        self.fine_rate_per_day = fine_rate_per_day


class ItemEntry:
    """
    Describes detailed info about one specific invoice row.

        description: Product/service/article name or description.
        item_unit: Unit (e.g: h, kg, l, kWh).
        item_amount: Amount of the products /services.
        item_price: Price of one product or service (without taxes).
        item_sum: Total amount without taxes and discount.
        vat: Describes value-added tax
        item_total: Total amount including taxes.
    """

    def __init__(
        self,
        description: str,
        item_unit: Optional[str] = None,
        item_amount: Optional[Decimal] = None,
        item_price: Optional[Decimal] = None,
        item_sum: Optional[Decimal] = None,
        vat: Optional[VAT] = None,
        item_total: Optional[Decimal] = None,
    ) -> None:
        self.description = description
        self.item_unit = item_unit
        self.item_amount = item_amount
        self.item_price = item_price
        self.item_sum = item_sum
        self.vat = vat
        self.item_total = item_total


class InvoiceSumGroup:
    """
    Contains invoiced amounts (total sum, sum_before_var etc).

        total_sum: Invoice total sum.
        invoice_sum: Amount of the invoice without tax.
        currency: Three-character currency code as specified in ISO 4217.
        total_to_pay: Amout to be paid. Credit invoice must have 0.00.
                      Negative amounts does not correspond to the Estonian legislation.
    """

    def __init__(
        self,
        total_sum: Decimal,
        invoice_sum: Optional[Decimal] = None,
        currency: Optional[str] = None,
        total_to_pay: Optional[Decimal] = None,
        vat: Optional[VAT] = None,
    ) -> None:
        self.total_sum = total_sum
        self.invoice_sum = invoice_sum
        self.currency = currency
        self.total_to_pay = total_to_pay
        self.vat = vat


class Invoice:
    """
    Contains information about one specific invoice.

    """

    def __init__(
        self,
        invoice_id: str,
        service_id: str,
        reg_number: str,
        seller_reg_number: str,
        seller_party: InvoiceParty,
        buyer_party: InvoiceParty,
        invoice_information: InvoiceInformation,
        invoice_sum_group: InvoiceSumGroup,
        invoice_item_entries: List[ItemEntry],
    ) -> None:
        self.invoice_id = invoice_id
        self.service_id = service_id
        self.reg_number = reg_number
        self.seller_reg_number = seller_reg_number
        self.seller_party = seller_party
        self.buyer_party = buyer_party
        self.invoice_information = invoice_information
        self.invoice_sum_group = invoice_sum_group
        self.invoice_items = invoice_item_entries
