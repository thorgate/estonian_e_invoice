import datetime
from decimal import Decimal

from entities.common import Node


class Header(Node):
    """
    Contains file specific elements.

        date: Determines the date when the file is generated.
        file_id: Unique identification of the file. Used to prevent double-processing of the same file.
        version: The version of the standard used.
    """

    tag = "Header"

    def __init__(self, date: datetime.date, file_id: str, version: str,) -> None:
        self.elements = {
            "Date": date,
            "FileID": file_id,
            "Version": version,
        }


class Footer(Node):
    """
    Contains the total number of the invoices and the sum of all the invoices in the file.

        invoices_count: Number of invoices in the file.
        total_amount: Sum of all the invoices in the file.
    """

    tag = "Footer"

    def __init__(self, invoices_count: int, total_amount: Decimal) -> None:
        self.elements = {
            "TotalNumberInvoices": invoices_count,
            "TotalAmount": total_amount,
        }
