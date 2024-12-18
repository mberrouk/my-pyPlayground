from django.core.exceptions import ValidationError as ValidationError
from django.utils.functional import SimpleLazyObject as SimpleLazyObject
from django.utils.text import format_lazy as format_lazy

def prefix_validation_error(error, prefix, code, params): ...
