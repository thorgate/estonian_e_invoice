from xml.etree.ElementTree import Element, SubElement


class Node:
    tag = "Node"
    elements = {}

    def to_etree(self):
        parent = Element(self.tag)

        for key, value in self.elements.items():
            child = SubElement(parent, key)
            if isinstance(value, Node):
                child.append(value.to_etree())
            elif isinstance(value, list):
                for node in value:
                    if isinstance(node, Node):
                        child.append(node.to_etree())
            else:
                child.text = value

        return parent
