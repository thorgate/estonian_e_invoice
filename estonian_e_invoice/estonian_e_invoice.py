"""Main module."""
from xml.dom import minidom
from xml.etree import ElementTree

from entities.file import Footer, Header
from entities.invoice import Invoice, InvoiceParty, InvoiceInformation, InvoiceSumGroup, ItemEntry


class XMLGenerator:
    def __init__(self, header: Header, footer: Footer, invoice: Invoice):
        self.header = header
        self.footer = footer
        self.invoice = invoice

    @staticmethod
    def prettify(element):
        """Return a pretty-printed XML string for the Element."""
        rough_string = ElementTree.tostring(element, "utf-8")
        re_parsed = minidom.parseString(rough_string)
        return re_parsed.toprettyxml(indent="  ")

    @staticmethod
    def set_root_attrs(root):
        root.set("xsi:noNamespaceSchemaLocation", "e-invoice_ver1.2.xsd")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

    @staticmethod
    def add_root_nodes(root):
        header_element = header.to_etree()
        footer_element = footer.to_etree()
        invoice_element = invoice.to_etree()

        root.append(header_element)
        root.append(invoice_element)
        root.append(footer_element)

    def generate(self):
        root = ElementTree.Element("E_Invoice")
        self.set_root_attrs(root)
        self.add_root_nodes(root)
        return self.prettify(root)
