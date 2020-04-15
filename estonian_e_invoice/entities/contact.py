from typing import Optional


class AddressRecord:
    """
    Describes the address of the invoice parties.

        postal_address_1: Street, house, apartment.
        postal_address_2: Village, postal office, etc.
        city: City or county.
        postal_code: Postal code
        country: Country
    """

    def __init__(
        self,
        postal_address_1: str,
        city: str = None,
        postal_address_2: Optional[str] = None,
        postal_code: Optional[str] = None,
        country: Optional[str] = None,
    ) -> None:
        self.postal_address_1 = postal_address_1
        self.city = city
        self.postal_address_2 = postal_address_2
        self.postal_code = postal_code
        self.country = country


class ContactData:
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
        self.contact_name = contact_name
        self.contact_person_code = contact_person_code
        self.phone_number = phone_number
        self.fax_number = fax_number
        self.url = url
        self.email_address = email_address
        self.legal_address = legal_address
        self.mail_address = mail_address
