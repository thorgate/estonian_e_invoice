import datetime
from decimal import Decimal
from typing import Optional


class Header:
    """
    Contains file specific elements.

        date: Determines the date when the file is generated.
        file_id: Unique identification of the file. Used to prevent double-processing of the same file.
        version: The version of the standard used.
        is_test: Determines whether this is a test file or not.
        app_id: Application identifier. EARVE is used for e-invoice to the internet bank.
        sender_id: Sender ID of the file.
        receiver_id: Receiver ID of the file.
        contract_id: Contract ID between the sender and the receiver.
        payee_acc_number: Account number of the payee.
    """

    def __init__(
        self,
        date: datetime.date,
        file_id: str,
        version: str,
        is_test: Optional[bool] = None,
        app_id: Optional[str] = None,
        sender_id: Optional[str] = None,
        receiver_id: Optional[str] = None,
        contract_id: Optional[str] = None,
        payee_acc_number: Optional[str] = None,
    ) -> None:
        self.date = date
        self.file_id = file_id
        self.version = version
        self.is_test = is_test
        self.app_id = app_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.contract_id = contract_id
        self.payee_acc_number = payee_acc_number


class Footer:
    """
    Contains the total number of the invoices and the sum of all the invoices in the file.

        invoices_count: Number of invoices in the file.
        total_amount: Sum of all the invoices in the file.
    """

    def __init__(self, invoices_count: int, total_amount: Decimal) -> None:
        self.invoices_count = invoices_count
        self.total_amount = total_amount
