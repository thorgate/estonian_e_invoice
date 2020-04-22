"""Main module."""
from typing import TYPE_CHECKING, ByteString, Union
from xml.dom import minidom
from xml.etree import ElementTree

if TYPE_CHECKING:
    from estonian_e_invoice.entities import Header, Footer, Invoice


class XMLGenerator:
    """
    Generate string representation of XML element.
    """
    encoding = "utf-8"

    def __init__(self, header: "Header", footer: "Footer", invoice: "Invoice") -> None:
        self.root = ElementTree.Element("E_Invoice")
        self.header = header
        self.footer = footer
        self.invoice = invoice

    def to_string(self, prettify: bool) -> Union[ByteString, str]:
        """
        A ByteString is returned if prettified, otherwise str.

        Returns an (optionally prettified) encoded string containing the XML data.
        """
        rough_string = ElementTree.tostring(self.root, self.encoding)

        if not prettify:
            return rough_string

        re_parsed = minidom.parseString(rough_string)
        return re_parsed.toprettyxml(indent="  ")

    def set_root_attrs(self) -> None:
        self.root.set("xsi:noNamespaceSchemaLocation", "e-invoice_ver1.2.xsd")
        self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

    def add_nodes_to_root(self) -> None:
        self.root.extend(
            [self.header.to_etree(), self.invoice.to_etree(), self.footer.to_etree(),]
        )

    def generate(self, prettify=True) -> Union[ByteString, str]:
        self.set_root_attrs()
        self.add_nodes_to_root()
        return self.to_string(prettify)
