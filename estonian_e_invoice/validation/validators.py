from cerberus import Validator


class BaseValidator(Validator):
    def validate_object(self, obj):
        return self.validate(obj.__dict__)
