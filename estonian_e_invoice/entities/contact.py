from typing import Optional

from estonian_e_invoice.entities.common import Node


class AddressRecord(Node):
    """
    Describes the address of the invoice parties.

        tag: XML element tag
        postal_address_1: Street, house, apartment.
        postal_address_2: Village, postal office, etc.
        city: City or county.
        postal_code: Postal code
        country: Country
    """

    def __init__(
        self,
        tag: str,
        postal_address_1: str,
        city: str,
        postal_address_2: Optional[str] = None,
        postal_code: Optional[str] = None,
        country: Optional[str] = None,
    ) -> None:
        self.tag = tag
        self.elements = {
            "PostalAddress1": postal_address_1,
            "City": city,
            "PostalAddress2": postal_address_2,
            "PostalCode": postal_code,
            "Country": country,
        }


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
        mail_address: Describes the postal address of the party.
    """

    tag = "ContactData"

    def __init__(
        self,
        contact_name: Optional[str] = None,
        contact_person_code: Optional[str] = None,
        phone_number: Optional[str] = None,
        fax_number: Optional[str] = None,
        url: Optional[str] = None,
        email_address: Optional[str] = None,
        legal_address: Optional[AddressRecord] = None,
        mail_address: Optional[AddressRecord] = None,
    ) -> None:
        self.elements = {
            "ContactName": contact_name,
            "ContactPersonCode": contact_person_code,
            "PhoneNumber": phone_number,
            "FaxNumber": fax_number,
            "URL": url,
            "EmailAddress": email_address,
            "LegalAddress": legal_address,
            "MailAddress": mail_address,
        }
