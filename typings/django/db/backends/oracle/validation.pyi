from django.core import checks as checks
from django.db.backends.base.validation import BaseDatabaseValidation as BaseDatabaseValidation

class DatabaseValidation(BaseDatabaseValidation):
    def check_field_type(self, field, field_type): ...
