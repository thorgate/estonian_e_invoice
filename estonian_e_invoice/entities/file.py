from decimal import Decimal

from estonian_e_invoice.entities.common import Node
from estonian_e_invoice.validation.validation_schemas import (
    FOOTER_SCHEMA,
    HEADER_SCHEMA,
)

"""
The version of the standard used. Further information can be found here:
https://wp.itl.ee/files/Estonian_e-invoice_description_ver1.2_eng.pdf
"""
E_INVOICE_VERSION = "1.2"


class Header(Node):
    """
    Contains file specific elements.

        date: Determines the date when the file is generated.
        file_id: Unique identification of the file. Used to prevent double-processing of the same file.
    """

    tag = "Header"
    validation_schema = HEADER_SCHEMA

    def __init__(self, date: str, file_id: str,) -> None:
        self.elements = self.validate(
            {"Date": date, "FileId": file_id, "Version": E_INVOICE_VERSION,}
        )


class Footer(Node):
    """
    Contains the total number of the invoices and the sum of all the invoices in the file.

        invoices_count: Number of invoices in the file.
        total_amount: Sum of all the invoices in the file.
    """

    tag = "Footer"
    validation_schema = FOOTER_SCHEMA

    def __init__(self, invoices_count: int, total_amount: Decimal) -> None:
        self.elements = self.validate(
            {"TotalNumberInvoices": invoices_count, "TotalAmount": total_amount,}
        )
