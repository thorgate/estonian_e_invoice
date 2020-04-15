import datetime
from decimal import Decimal
from typing import Optional


class AccountInfo:
    """
    Describes the accounts of a party.

        account_number: Account number in local banking system.
        iban: International Banking Account Number.
        bic: Bank identification code (SWIFT code).
        bank_name: The name of the bank.
    """

    def __init__(
        self,
        account_number: str,
        iban: Optional[str] = None,
        bic: Optional[str] = None,
        bank_name: Optional[str] = None,
    ) -> None:
        self.account_number = account_number
        self.iban = iban
        self.bic = bic
        self.bank_name = bank_name


class PaymentInfo:
    """
    Describes the information used for generating payment order form from the invoice.

        currency: Three-character currency code as specified in ISO 4217.
        payment_description: Description of the payment.
        payable: Whether this bill needs to be paid or not. Payment due date is mandatory if payable.
        payment_total_sum: Total amount of the payment.
        payer_name: Name of the payer.
        payment_id: Invoice number.
        pay_to_account: The beneficiary’s account number.
        pay_to_name: The beneficiary’s name.
        payment_due_date: Payment due date.
    """

    def __init__(
        self,
        currency: str,
        payment_description: str,
        payable: bool,
        payment_total_sum: Decimal,
        payer_name: str,
        payment_id: str,
        pay_to_account: str,
        pay_to_name: str,
        payment_due_date: Optional[datetime.date] = None,
    ) -> None:
        self.currency = currency
        self.payment_description = payment_description
        self.payable = payable
        self.payment_due_date = payment_due_date
        self.payment_total_sum = payment_total_sum
        self.payer_name = payer_name
        self.payment_id = payment_id
        self.pay_to_account = pay_to_account
        self.pay_to_name = pay_to_name
