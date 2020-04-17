from datetime import datetime
from decimal import Decimal

from cerberus import TypeDefinition, Validator

from estonian_e_invoice.entities import Node

DECIMAL_TYPE = TypeDefinition("decimal", (Decimal,), ())
NODE_TYPE = TypeDefinition("node", (Node,), ())


class CustomValidator(Validator):
    types_mapping = Validator.types_mapping.copy()
    types_mapping["decimal"] = DECIMAL_TYPE
    types_mapping["node"] = NODE_TYPE

    # Custom type validations
    def _validate_type_node(self, value):
        return isinstance(value, Node)

    # Custom validators
    def _check_with_date_string(self, field, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            self._error(field, "Date should be in %Y-%m-%d format")

    # Custom coarces
    def _normalize_coerce_to_yes_no(self, value):
        return "YES" if value else "NO"

    def _normalize_coerce_two_decimal_places(self, value):
        return round(value, 2)

    def _normalize_coerce_four_decimal_places(self, value):
        return round(value, 4)
