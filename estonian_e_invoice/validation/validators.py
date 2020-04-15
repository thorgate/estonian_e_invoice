from cerberus import Validator

from estonian_e_invoice.validation.validator_custom_types import DECIMAL_TYPE


class BaseValidator(Validator):
    types_mapping = Validator.types_mapping.copy()
    types_mapping["decimal"] = DECIMAL_TYPE

    def validate_object(self, obj):
        return self.validate(obj.__dict__)
