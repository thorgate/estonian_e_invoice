from xml.etree.ElementTree import Element, SubElement


class Node:
    """
    Represents an XML element.

    This class is the reference implementation of the Element interface.

    The element tag, attribute names, and attribute values are string values.

    Example:
        tag = "Node"
        elements = {
            "Child": "Text",
        }
        attributes = {
            "id": "1",
        }
        element_attrs = {
            "childId": "2",
        }

        Renders to:
        <Node id="1">
            <Child childId="2">
                Text
            </Child>
        </Node>
    """
    # XML element's name.
    tag = "Node"
    # Dictionary of sub XML elements.
    elements = {}
    # Dictionary of the element's attributes.
    attributes = {}
    # Dictionary of sub elements' attributes.
    element_attrs = {}
    # Cerberus validation schema to be used while validating the element.
    validation_schema = None

    def validate(self, data: dict) -> dict:
        # Run validations if there is a validation schema
        if not self.validation_schema:
            raise ValueError("validation_schema has to be defined to run validation")

        from estonian_e_invoice.validation.exceptions import ValidationError
        from estonian_e_invoice.validation.validators import CustomValidator

        validator = CustomValidator(self.validation_schema)
        # Exclude null and blank values.
        is_valid = validator.validate(
            {k: v for k, v in data.items() if v not in (None, "")}
        )

        if is_valid:
            return validator.document
        else:
            raise ValidationError(validator.errors)

    @classmethod
    def set_attrs(cls, element: Element, attributes: dict) -> None:
        for key, value in attributes.items():
            element.set(key, str(value))

    def to_etree(self) -> Element:
        parent = Element(self.tag)
        self.set_attrs(parent, self.attributes)

        for key, value in self.elements.items():
            if not value:
                continue

            if isinstance(value, Node):
                parent.append(value.to_etree())
            elif isinstance(value, list):
                for node in value:
                    if isinstance(node, Node):
                        parent.append(node.to_etree())
                    else:
                        raise ValueError("Provided value is not an instance of Node class")
            else:
                child = SubElement(parent, key)
                self.set_attrs(child, self.element_attrs.get(key, {}))
                child.text = str(value)

        return parent
