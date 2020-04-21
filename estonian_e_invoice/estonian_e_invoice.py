"""Main module."""
from typing import TYPE_CHECKING
from xml.dom import minidom
from xml.etree import ElementTree

if TYPE_CHECKING:
    from estonian_e_invoice.entities import Header, Footer, Invoice


class XMLGenerator:
    def __init__(self, header: "Header", footer: "Footer", invoice: "Invoice") -> None:
        self.header = header
        self.footer = footer
        self.invoice = invoice

    @staticmethod
    def prettify(element) -> str:
        """Return a pretty-printed XML string for the Element."""
        rough_string = ElementTree.tostring(element, "utf-8")
        re_parsed = minidom.parseString(rough_string)
        return re_parsed.toprettyxml(indent="  ")

    @staticmethod
    def set_root_attrs(root) -> None:
        root.set("xsi:noNamespaceSchemaLocation", "e-invoice_ver1.2.xsd")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

    def add_nodes_to_root(self, root) -> None:
        root.extend(
            [self.header.to_etree(), self.invoice.to_etree(), self.footer.to_etree(),]
        )

    def generate(self) -> str:
        root = ElementTree.Element("E_Invoice")
        self.set_root_attrs(root)
        self.add_nodes_to_root(root)
        return self.prettify(root)
