from xml.etree.ElementTree import Element, SubElement


class Node:
    tag = "Node"
    elements = {}
    attributes = {}
    element_attrs = {}
    validation_schema = None

    def validate(self, data: dict) -> dict:
        # Run validations if there is a validation schema
        if self.validation_schema:
            from estonian_e_invoice.validation.exceptions import ValidationError
            from estonian_e_invoice.validation.validators import CustomValidator

            validator = CustomValidator(self.validation_schema)
            # Exclude None values.
            is_valid = validator.validate(
                {k: v for k, v in data.items() if v is not None}
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
                child = SubElement(parent, key)
                self.set_attrs(child, self.element_attrs.get(key, {}))
                child.text = str(value)

        return parent
