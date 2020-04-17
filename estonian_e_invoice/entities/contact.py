from typing import Optional

from estonian_e_invoice.entities import Node
from estonian_e_invoice.validation.validation_schemas import (
    ADDRESS_RECORD_SCHEMA,
    CONTACT_DATA_SCHEMA,
)


class LegalAddress(Node):
    """
    Describes the legal address of the invoice parties.

        postal_address_1: Street, house, apartment.
        postal_address_2: Village, postal office, etc.
        city: City or county.
        postal_code: Postal code
        country: Country
    """

    tag = "LegalAddress"
    validation_schema = ADDRESS_RECORD_SCHEMA

    def __init__(
        self,
        postal_address_1: str,
        city: str,
        postal_address_2: Optional[str] = None,
        postal_code: Optional[str] = None,
        country: Optional[str] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "PostalAddress1": postal_address_1,
                "City": city,
                "PostalAddress2": postal_address_2,
                "PostalCode": postal_code,
                "Country": country,
            }
        )


class ContactData(Node):
    """
    Describes the contacts of the invoice parties.

        contact_name: Name of the contact person.
        contact_person_code: Personal ID-code of the contact person.
        phone_number: Contact phone.
        fax_number: Fax number.
        url: Web address.
        email_address: E-mail address.
        legal_address: Describes the legal address of the party.
    """

    tag = "ContactData"
    validation_schema = CONTACT_DATA_SCHEMA

    def __init__(
        self,
        contact_name: Optional[str] = None,
        contact_person_code: Optional[str] = None,
        phone_number: Optional[str] = None,
        fax_number: Optional[str] = None,
        url: Optional[str] = None,
        email_address: Optional[str] = None,
        legal_address: Optional[LegalAddress] = None,
    ) -> None:
        self.elements = self.validate(
            {
                "ContactName": contact_name,
                "ContactPersonCode": contact_person_code,
                "PhoneNumber": phone_number,
                "FaxNumber": fax_number,
                "URL": url,
                "EmailAddress": email_address,
                "LegalAddress": legal_address,
            }
        )
