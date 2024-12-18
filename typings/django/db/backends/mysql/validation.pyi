from django.core import checks as checks
from django.db.backends.base.validation import BaseDatabaseValidation as BaseDatabaseValidation
from django.utils.version import get_docs_version as get_docs_version

class DatabaseValidation(BaseDatabaseValidation):
    def check(self, **kwargs): ...
    def check_field_type(self, field, field_type): ...
