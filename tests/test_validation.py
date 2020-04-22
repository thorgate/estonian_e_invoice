#!/usr/bin/env python

"""Test for validators"""

import ast
from datetime import datetime
from decimal import Decimal

import pytest
from estonian_e_invoice.entities import (
    VAT,
    AccountInfo,
    BuyerParty,
    ContactData,
    Footer,
    Header,
    Invoice,
    InvoiceInformation,
    InvoiceItemGroup,
    InvoiceSumGroup,
    InvoiceType,
    ItemDetailInfo,
    ItemEntry,
    LegalAddress,
    PaymentInfo,
    SellerParty,
)
from estonian_e_invoice.validation.exceptions import ValidationError


def test_header_validation():
    # Test date, file_id and version are required
    with pytest.raises(ValidationError) as validation_error:
        Header(date=None, file_id=None)
    assert {
        "Date": ["required field"],
        "FileID": ["required field"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        Header(date=1111, file_id=123456)
    assert {
        "Date": ["must be of string type"],
        "FileID": ["must be of string type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid date
    with pytest.raises(ValidationError) as validation_error:
        Header(date="20-04-2020", file_id="123456")
    assert {"Date": ["Date should be in %Y-%m-%d format"]} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with valid params
    header = Header(date="2020-04-20", file_id="123456")
    assert header.elements == {
        "Date": "2020-04-20",
        "FileID": "123456",
        "Version": "1.2",
    }


def test_footer_validation():
    # Test invoices_count and total amount are required
    with pytest.raises(ValidationError) as validation_error:
        Footer(invoices_count=None, total_amount=None)
    assert {
        "TotalNumberInvoices": ["required field"],
        "TotalAmount": ["required field"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        Footer(invoices_count=Decimal("10.00"), total_amount=10)
    assert {
        "TotalNumberInvoices": ["must be of integer type"],
        "TotalAmount": ["must be of decimal type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params
    footer = Footer(invoices_count=10, total_amount=Decimal("10.00"))
    assert footer.elements == {
        "TotalNumberInvoices": 10,
        "TotalAmount": Decimal("10.00"),
    }


def test_account_info_validation():
    # Test account number is required
    with pytest.raises(ValidationError) as validation_error:
        AccountInfo(account_number=None)
    assert {"AccountNumber": ["required field"],} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        AccountInfo(
            account_number=123123123, iban=123123123, bic=123123213, bank_name=123123123
        )
    assert {
        "AccountNumber": ["must be of string type"],
        "IBAN": ["must be of string type"],
        "BIC": ["must be of string type"],
        "BankName": ["must be of string type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid param types
    with pytest.raises(ValidationError) as validation_error:
        AccountInfo(account_number="####", iban="$$$$", bic=12345, bank_name=123456)
    assert {
        "AccountNumber": ["value does not match regex '([0-9|A-Z])*'"],
        "IBAN": ["value does not match regex '([0-9|A-Z])*'"],
        "BIC": ["must be of string type"],
        "BankName": ["must be of string type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params
    account_info = AccountInfo(
        account_number="10123456789012",
        iban="EE471000001020145685",
        bic="HABAEE2X",
        bank_name="Test Bank",
    )
    assert account_info.elements == {
        "AccountNumber": "10123456789012",
        "IBAN": "EE471000001020145685",
        "BIC": "HABAEE2X",
        "BankName": "Test Bank",
    }

    # The required params only
    account_info = AccountInfo(account_number="10123456789012",)
    assert account_info.elements == {
        "AccountNumber": "10123456789012",
    }


def test_payment_info_validation():
    # Test currency, payment_description, payable, payment_total_sum,
    # payer_name, payment_id, pay_to_account and pay_to_name are required
    with pytest.raises(ValidationError) as validation_error:
        PaymentInfo(
            currency=None,
            payment_description=None,
            payable=None,
            payment_total_sum=None,
            payer_name=None,
            payment_id=None,
            pay_to_account=None,
            pay_to_name=None,
        )
    assert {
        "Currency": ["required field"],
        "PaymentDescription": ["required field"],
        "Payable": ["required field"],
        "PaymentTotalSum": ["required field"],
        "PayerName": ["required field"],
        "PaymentID": ["required field"],
        "PayToAccount": ["required field"],
        "PayToName": ["required field"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        PaymentInfo(
            currency="1231",
            payment_description=123123,
            payable=123123,
            payment_total_sum=Decimal("1231.123213"),
            payer_name=(),
            payment_id=66.66,
            pay_to_account=Decimal("111.111"),
            pay_to_name=123123,
            pay_due_date=None,
        )
    assert {
        "Currency": ["max length is 3", "value does not match regex '[A-Z][A-Z][A-Z]'"],
        "PaymentDescription": ["must be of string type"],
        "PaymentTotalSum": ["must not have more than 2 decimal places",],
        "PayerName": ["must be of string type"],
        "PaymentID": ["must be of string type"],
        "PayToAccount": ["must be of string type"],
        "PayToName": ["must be of string type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params
    payment_info = PaymentInfo(
        currency="EUR",
        payment_description="Pay for invoice",
        payable=True,
        payment_total_sum=Decimal("123.10"),
        payer_name="Test buyer",
        payment_id="123",
        pay_to_account="EE471000001020145685",
        pay_to_name="Test Seller",
        pay_due_date="2020-04-30",
    )
    assert payment_info.elements == {
        "Currency": "EUR",
        "PaymentDescription": "Pay for invoice",
        # payable boolean will be represented as YES or NO strings.
        "Payable": "YES",
        # Note that decimal will have maximum 2 decimal points,
        "PaymentTotalSum": Decimal("123.10"),
        "PayerName": "Test buyer",
        "PaymentID": "123",
        "PayToAccount": "EE471000001020145685",
        "PayToName": "Test Seller",
        "PayDueDate": "2020-04-30",
    }


def test_legal_address_validation():
    # Test postal_address_1 and city are required
    with pytest.raises(ValidationError) as validation_error:
        LegalAddress(
            postal_address_1=None, city=None,
        )
    assert {
        "PostalAddress1": ["required field"],
        "City": ["required field"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        LegalAddress(
            postal_address_1=123123,
            city=123123,
            postal_address_2=123.123,
            postal_code={},
            country=(),
        )
    assert {
        "PostalAddress1": ["must be of string type"],
        "City": ["must be of string type"],
        "PostalAddress2": ["must be of string type"],
        "PostalCode": ["must be of string type"],
        "Country": ["must be of string type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params
    legal_address = LegalAddress(
        postal_address_1="Test street 1",
        postal_address_2="Test village",
        city="Test city",
        postal_code="12345",
        country="Testland",
    )
    assert legal_address.elements == {
        "PostalAddress1": "Test street 1",
        "PostalAddress2": "Test village",
        "City": "Test city",
        "PostalCode": "12345",
        "Country": "Testland",
    }

    # The required params only
    legal_address = LegalAddress(postal_address_1="Test street 1", city="Test city",)
    assert legal_address.elements == {
        "PostalAddress1": "Test street 1",
        "City": "Test city",
    }


def test_contact_data_validation():
    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        ContactData(
            contact_name=Decimal("10.00"),
            contact_person_code="1234567890123456",
            phone_number=58512128,
            fax_number=1.33,
            url={},
            email_address="a",
            legal_address="Legal",
        )
    assert {
        "ContactName": ["must be of string type"],
        "ContactPersonCode": ["max length is 15"],
        "PhoneNumber": ["must be of string type"],
        "FaxNumber": ["must be of string type"],
        "URL": ["must be of string type"],
        "EmailAddress": ["value does not match regex '.+@.+'"],
        "LegalAddress": ["must be of legal_address type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params

    # Create a legal address to be passed into the contact data
    legal_address = LegalAddress(postal_address_1="Test street 1", city="Test city",)
    # Test with valid params
    contact_data = ContactData(
        contact_name="Test Contact",
        contact_person_code="11111111111",
        phone_number="57557575",
        fax_number="57557575",
        url="https://test.test",
        email_address="testcontact@test.test",
        legal_address=legal_address,
    )
    assert contact_data.elements == {
        "ContactName": "Test Contact",
        "ContactPersonCode": "11111111111",
        "PhoneNumber": "57557575",
        "FaxNumber": "57557575",
        "URL": "https://test.test",
        "EmailAddress": "testcontact@test.test",
        "LegalAddress": legal_address,
    }


def test_vat_validation():
    # Test vat_rate and vat_sum are required
    with pytest.raises(ValidationError) as validation_error:
        VAT(
            vat_rate=None, vat_sum=None,
        )
    assert {
        "VATRate": ["required field",],
        "VATSum": ["required field",],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        VAT(
            vat_rate=20,
            vat_sum="20",
            sum_before_vat=100.00,
            sum_after_vat=120.0,
            currency="$",
        )
    assert {
        "VATRate": ["must be of decimal type",],
        "VATSum": ["must be of decimal type",],
        "SumBeforeVAT": ["must be of decimal type",],
        "SumAfterVAT": ["must be of decimal type",],
        "Currency": ["value does not match regex '[A-Z][A-Z][A-Z]'"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params
    vat = VAT(
        vat_rate=Decimal("20.00"),
        vat_sum=Decimal("20.0000"),
        sum_before_vat=Decimal("100.0000"),
        sum_after_vat=Decimal("120.0000"),
        currency="USD",
    )
    assert vat.elements == {
        "VATRate": Decimal("20.00"),
        "VATSum": Decimal("20.0000"),
        "SumBeforeVAT": Decimal("100.0000"),
        "SumAfterVAT": Decimal("120.0000"),
        "Currency": "USD",
    }

    # The required params only
    vat = VAT(vat_rate=Decimal("20.00"), vat_sum=Decimal("20.0000"),)
    assert vat.elements == {
        "VATRate": Decimal("20.00"),
        "VATSum": Decimal("20.0000"),
    }


def test_seller_party_validation():
    # Test name and reg_number are required
    with pytest.raises(ValidationError) as validation_error:
        SellerParty(
            name=None, reg_number=None,
        )
    assert {
        "Name": ["required field",],
        "RegNumber": ["required field",],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        SellerParty(
            name=20,
            reg_number=333,
            vat_reg_number=100.00,
            contact_data="Test street",
            account_info="$",
        )
    assert {
        "Name": ["must be of string type",],
        "RegNumber": ["must be of string type",],
        "VATRegNumber": ["must be of string type",],
        "ContactData": ["must be of contact_data type",],
        "AccountInfo": ["must be of account_info type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params

    # Create seller legal address
    legal_address = LegalAddress(postal_address_1="Test street 1", city="Test city",)
    # Create seller contact data
    contact_data = ContactData(
        contact_name="Test Contact Seller",
        contact_person_code="11111111111",
        phone_number="57557575",
        fax_number="57557575",
        url="https://test.test",
        email_address="testcontact@test.test",
        legal_address=legal_address,
    )
    # Create seller account info
    account_info = AccountInfo(
        account_number="10123456789012",
        iban="EE471000001020145685",
        bic="HABAEE2X",
        bank_name="Test Bank",
    )
    # Create seller
    seller_party = SellerParty(
        name="Test seller",
        reg_number="33333333333",
        vat_reg_number="EE123456789",
        account_info=account_info,
        contact_data=contact_data,
    )
    assert seller_party.elements == {
        "Name": "Test seller",
        "RegNumber": "33333333333",
        "VATRegNumber": "EE123456789",
        "ContactData": contact_data,
        "AccountInfo": account_info,
    }

    # The required params only
    seller_party = SellerParty(name="Test seller", reg_number="33333333333",)
    assert seller_party.elements == {
        "Name": "Test seller",
        "RegNumber": "33333333333",
    }


def test_buyer_party_validation():
    # Test name is required (reg_number is not required different from the seller party)
    with pytest.raises(ValidationError) as validation_error:
        BuyerParty(name=None,)
    assert {"Name": ["required field",],} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        BuyerParty(
            name=20,
            reg_number=333,
            vat_reg_number=100.00,
            contact_data="Test street",
            account_info="$",
        )
    assert {
        "Name": ["must be of string type",],
        "RegNumber": ["must be of string type",],
        "VATRegNumber": ["must be of string type",],
        "ContactData": ["must be of contact_data type",],
        "AccountInfo": ["must be of account_info type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params

    # Create buyer legal address
    legal_address = LegalAddress(postal_address_1="Test street 2", city="City of test",)
    # Create buyer contact data
    contact_data = ContactData(
        contact_name="Test Contact Buyer",
        contact_person_code="22222222222",
        phone_number="56556565",
        fax_number="56556565",
        url="https://test.test",
        email_address="testcontactbuyer@test.test",
        legal_address=legal_address,
    )
    # Create buyer account info
    account_info = AccountInfo(
        account_number="10123456789023",
        iban="EE471000001056543214",
        bic="HABAEE2X",
        bank_name="Test Bank",
    )
    # Create buyer
    buyer_party = BuyerParty(
        name="Test buyer",
        reg_number="44444444444",
        vat_reg_number="EE111111111",
        account_info=account_info,
        contact_data=contact_data,
    )
    assert buyer_party.elements == {
        "Name": "Test buyer",
        "RegNumber": "44444444444",
        "VATRegNumber": "EE111111111",
        "ContactData": contact_data,
        "AccountInfo": account_info,
    }

    # The required params only
    buyer_party = BuyerParty(name="Test buyer",)
    assert buyer_party.elements == {
        "Name": "Test buyer",
    }


def test_invoice_type_validation():
    # Test invoice_type is required
    with pytest.raises(ValidationError) as validation_error:
        InvoiceType(invoice_type=None)
    assert {"Type": ["required field",],} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        InvoiceType(
            invoice_type="LOA", source_invoice={"source": 123},
        )
    assert {
        "Type": ["unallowed value LOA",],
        "SourceInvoice": ["must be of string type",],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params
    invoice_type = InvoiceType(invoice_type="DEB", source_invoice="Invoice 123",)
    assert invoice_type.elements == {
        "SourceInvoice": "Invoice 123",
    }
    assert invoice_type.attributes == {
        "type": "DEB",
    }

    # The required params only
    invoice_type = InvoiceType(invoice_type="DEB",)
    assert invoice_type.elements == {}
    assert invoice_type.attributes == {
        "type": "DEB",
    }


def test_invoice_information_validation():
    # Test invoice_type, invoice_number, invoice_date and document_name are required
    with pytest.raises(ValidationError) as validation_error:
        InvoiceInformation(
            invoice_type=None,
            invoice_number=None,
            invoice_date=None,
            document_name=None,
        )
    assert {
        "Type": ["required field"],
        "InvoiceNumber": ["required field"],
        "InvoiceDate": ["required field"],
        "DocumentName": ["required field"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        InvoiceInformation(
            invoice_type="DEB",
            invoice_number=1234,
            invoice_date=datetime.today(),
            document_name={"name": "Invoice"},
            due_date=datetime.now(),
            fine_rate_per_day=1.2,
        )
    assert {
        "Type": ["must be of invoice_type type"],
        "InvoiceNumber": ["must be of string type"],
        "InvoiceDate": ["must be of string type",],
        "DocumentName": ["must be of string type"],
        "DueDate": ["must be of string type"],
        "FineRatePerDay": ["must be of decimal type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params

    # Create invoice type for the invoice information
    invoice_type = InvoiceType(invoice_type="DEB",)
    invoice_information = InvoiceInformation(
        invoice_type=invoice_type,
        invoice_number="Invoice 123",
        invoice_date="2020-04-20",
        document_name="Invoice 123 for Test Company",
        due_date="2020-05-20",
        fine_rate_per_day=Decimal("1.20"),
    )
    assert invoice_information.elements == {
        "Type": invoice_type,
        "InvoiceNumber": "Invoice 123",
        "InvoiceDate": "2020-04-20",
        "DocumentName": "Invoice 123 for Test Company",
        "DueDate": "2020-05-20",
        "FineRatePerDay": Decimal("1.20"),
    }

    # Test required params only
    invoice_type = InvoiceType(invoice_type="DEB",)
    invoice_information = InvoiceInformation(
        invoice_type=invoice_type,
        invoice_number="Invoice 123",
        invoice_date="2020-04-20",
        document_name="Invoice 123 for Test Company",
    )
    assert invoice_information.elements == {
        "Type": invoice_type,
        "InvoiceNumber": "Invoice 123",
        "InvoiceDate": "2020-04-20",
        "DocumentName": "Invoice 123 for Test Company",
    }


def test_item_detail_info_validation():
    # Test no params required
    item_detail_info = ItemDetailInfo()
    assert item_detail_info.elements == {}

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        ItemDetailInfo(
            item_unit={"unit": "m3"}, item_amount=1.0000, item_price=50.0000,
        )
    assert {
        "ItemUnit": ["must be of string type"],
        "ItemAmount": ["must be of decimal type"],
        "ItemPrice": ["must be of decimal type",],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params
    item_detail_info = ItemDetailInfo(
        item_unit="m3", item_amount=Decimal("1.0000"), item_price=Decimal("50.0000"),
    )
    assert item_detail_info.elements == {
        "ItemUnit": "m3",
        "ItemAmount": Decimal("1.0000"),
        "ItemPrice": Decimal("50.0000"),
    }


def test_item_entry_validation():
    # Test description is required
    with pytest.raises(ValidationError) as validation_error:
        ItemEntry(description=None,)
    assert {"Description": ["required field"],} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        ItemEntry(
            description=("Test description",),
            item_sum="1234.4444",
            vat={"VATRate": Decimal("20.00")},
            item_total=1234.4444,
            item_detail_info=[{"ItemDetail": "test"}],
        )
    assert {
        "Description": ["must be of string type"],
        "ItemSum": ["must be of decimal type"],
        "VAT": ["must be of vat type",],
        "ItemTotal": ["must be of decimal type",],
        "ItemDetailInfo": ["must be of item_detail_info type",],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params

    # VAT info for item entry
    vat = VAT(vat_rate=Decimal("20.00"), vat_sum=Decimal("20.0000"),)
    # Item detail info for the item entry
    item_detail_info = ItemDetailInfo(
        item_unit="m3", item_amount=Decimal("1.0000"), item_price=Decimal("50.0000"),
    )
    item_entry = ItemEntry(
        description="Item description",
        item_sum=Decimal("1234.4444"),
        vat=vat,
        item_total=Decimal("1234.4444"),
        item_detail_info=item_detail_info,
    )
    assert item_entry.elements == {
        "Description": "Item description",
        "ItemSum": Decimal("1234.4444"),
        "VAT": vat,
        "ItemTotal": Decimal("1234.4444"),
        "ItemDetailInfo": item_detail_info,
    }

    # Test required params only
    item_entry = ItemEntry(description="Item description",)
    assert item_entry.elements == {
        "Description": "Item description",
    }


def test_invoice_item_group_validation():
    # Test invoice_item_entries is required
    with pytest.raises(ValidationError) as validation_error:
        InvoiceItemGroup(invoice_item_entries=None,)
    assert {"ItemEntry": ["required field"],} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        InvoiceItemGroup(
            invoice_item_entries=[
                VAT(vat_rate=Decimal("20.00"), vat_sum=Decimal("20.0000"),),
                VAT(vat_rate=Decimal("20.00"), vat_sum=Decimal("20.0000"),),
            ]
        )
    assert {
        "ItemEntry": [
            {0: ["must be of item_entry type"], 1: ["must be of item_entry type"]},
        ],
    } == ast.literal_eval(str(validation_error.value))

    # Test a list of item entries is required
    with pytest.raises(ValidationError) as validation_error:
        InvoiceItemGroup(
            invoice_item_entries=ItemEntry(description="Item description"),
        )
    assert {"ItemEntry": ["must be of list type"],} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with valid params

    # Create item entries for the invoice item group
    item_entries = [
        ItemEntry(description="Item description",),
    ]
    invoice_item_group = InvoiceItemGroup(invoice_item_entries=item_entries)
    assert invoice_item_group.elements == {
        "ItemEntry": item_entries,
    }

    # Test with multiple item entries
    item_entries = [
        ItemEntry(description="Item description 1",),
        ItemEntry(description="Item description 2",),
    ]
    invoice_item_group = InvoiceItemGroup(invoice_item_entries=item_entries)
    assert invoice_item_group.elements == {
        "ItemEntry": item_entries,
    }


def test_invoice_sum_group_validation():
    # Test total_sum is required
    with pytest.raises(ValidationError) as validation_error:
        InvoiceSumGroup(total_sum=None,)
    assert {"TotalSum": ["required field"],} == ast.literal_eval(
        str(validation_error.value)
    )

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        InvoiceSumGroup(
            total_sum="123.123",
            invoice_sum=123.123,
            currency="US Dollar",
            total_to_pay=0,
            vat=ItemEntry(description="Test to break"),
        )
    assert {
        "TotalSum": ["must be of decimal type"],
        "InvoiceSum": ["must be of decimal type"],
        "Currency": ["max length is 3", "value does not match regex '[A-Z][A-Z][A-Z]'"],
        "TotalToPay": ["must be of decimal type"],
        "VAT": ["must be of vat type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params

    # Create VAT information for the invoice sum group
    vat = VAT(vat_rate=Decimal("20.00"), vat_sum=Decimal("20.0000"),)
    invoice_sum_group = InvoiceSumGroup(
        total_sum=Decimal("123.12"),
        invoice_sum=Decimal("123.1233"),
        currency="USD",
        total_to_pay=Decimal("0.00"),
        vat=vat,
    )
    assert invoice_sum_group.elements == {
        "TotalSum": Decimal("123.12"),
        "InvoiceSum": Decimal("123.1233"),
        "Currency": "USD",
        "TotalToPay": Decimal("0.00"),
        "VAT": vat,
    }


def test_invoice_validation():
    # Test all params are required
    with pytest.raises(ValidationError) as validation_error:
        Invoice(
            invoice_id=None,
            reg_number=None,
            seller_reg_number=None,
            seller_party=None,
            buyer_party=None,
            invoice_information=None,
            invoice_sum_group=None,
            invoice_item_group=None,
            payment_info=None,
        )
    assert {
        "invoiceId": ["required field"],
        "regNumber": ["required field"],
        "sellerRegnumber": ["required field"],
        "InvoiceInformation": ["required field"],
        "InvoiceItemGroup": ["required field"],
        "InvoiceParties": [
            {0: ["null value not allowed"], 1: ["null value not allowed"]}
        ],
        "InvoiceSumGroup": ["required field"],
        "PaymentInfo": ["required field"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with invalid params
    with pytest.raises(ValidationError) as validation_error:
        Invoice(
            invoice_id=1,
            reg_number="{REG_NUMBER_123123}",
            seller_reg_number=123456.7890,
            seller_party=[SellerParty(name="Seller", reg_number="33333333333")],
            buyer_party=[BuyerParty(name="Buyer"),],
            invoice_information="Invoice description",
            invoice_sum_group="Sum group",
            invoice_item_group=Decimal("10.00"),
            payment_info=["EUR",],
        )
    assert {
        "invoiceId": ["must be of string type"],
        "regNumber": ["max length is 15"],
        "sellerRegnumber": ["must be of string type"],
        "InvoiceInformation": ["must be of invoice_information type"],
        "InvoiceItemGroup": ["must be of invoice_item_group type"],
        "InvoiceParties": [
            {0: ["must be of invoice_party type"], 1: ["must be of invoice_party type"]}
        ],
        "InvoiceSumGroup": ["must be of invoice_sum_group type"],
        "PaymentInfo": ["must be of payment_info type"],
    } == ast.literal_eval(str(validation_error.value))

    # Test with valid params

    # Seller party of the invoice
    seller_party = SellerParty(name="Test seller", reg_number="222222222")
    # Buyer party of the invoice
    buyer_party = BuyerParty(name="Test buyer", reg_number="111111111")
    # Type of the invoice
    invoice_type = InvoiceType(invoice_type="DEB",)
    # Invoice information to be attached
    invoice_information = InvoiceInformation(
        invoice_type=invoice_type,
        invoice_number="Invoice 1234",
        invoice_date="2020-04-20",
        document_name="Invoice 1234 for Test Company",
    )
    # Invoice items
    item_entries = [
        ItemEntry(description="Item description 1",),
        ItemEntry(description="Item description 2",),
    ]
    # Item groups for the invoice
    invoice_item_group = InvoiceItemGroup(invoice_item_entries=item_entries)
    # Sum groups for the invoice
    invoice_sum_group = InvoiceSumGroup(total_sum=Decimal("1.20"),)
    # Payment info for the invoice
    payment_info = PaymentInfo(
        currency="EUR",
        payment_description="Invoice number 1234",
        payable=False,
        payment_total_sum=Decimal("1.20"),
        payer_name="Test buyer",
        payment_id="1234",
        pay_to_account="EE909900123456789012",
        pay_to_name="Test seller",
        pay_due_date="2020-04-30",
    )
    invoice = Invoice(
        invoice_id="1234",
        reg_number="111111111",
        seller_reg_number="222222222",
        seller_party=seller_party,
        buyer_party=buyer_party,
        invoice_information=invoice_information,
        invoice_sum_group=invoice_sum_group,
        invoice_item_group=invoice_item_group,
        payment_info=payment_info,
    )

    assert invoice.elements == {
        "InvoiceParties": [seller_party, buyer_party],
        "InvoiceSumGroup": invoice_sum_group,
        "InvoiceItemGroup": invoice_item_group,
        "InvoiceInformation": invoice_information,
        "PaymentInfo": payment_info,
    }
    assert invoice.attributes == {
        "invoiceId": "1234",
        "regNumber": "111111111",
        "sellerRegnumber": "222222222",
    }
