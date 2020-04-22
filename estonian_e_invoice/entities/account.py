from decimal import Decimal
from typing import Optional

from estonian_e_invoice.entities.common import Node
from estonian_e_invoice.validation.validation_schemas import (
    ACCOUNT_INFO_SCHEMA,
    PAYMENT_INFO_SCHEMA,
)


class AccountInfo(Node):
    """
    Describes the accounts of a party.

        account_number: Account number in local banking system.
        iban: International Banking Account Number.
        bic: Bank identification code (SWIFT code).
        bank_name: The name of the bank.
    """

    tag = "AccountInfo"
    validation_schema = ACCOUNT_INFO_SCHEMA

    def __init__(
        self,
        account_number: str,
        iban: Optional[str] = None,
        bic: Optional[str] = None,
        bank_name: Optional[str] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "AccountNumber": account_number,
                "IBAN": iban,
                "BIC": bic,
                "BankName": bank_name,
            }
        )


class PaymentInfo(Node):
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
        pay_due_date: Payment due date.
    """

    tag = "PaymentInfo"
    validation_schema = PAYMENT_INFO_SCHEMA

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
        pay_due_date: Optional[str] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "Currency": currency,
                "PaymentDescription": payment_description,
                "Payable": payable,
                "PaymentTotalSum": payment_total_sum,
                "PayerName": payer_name,
                "PaymentID": payment_id,
                "PayToAccount": pay_to_account,
                "PayToName": pay_to_name,
                "PayDueDate": pay_due_date,
            }
        )
