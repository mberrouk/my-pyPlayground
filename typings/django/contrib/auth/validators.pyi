from _typeshed import Incomplete
from django.core import validators as validators
from django.utils.deconstruct import deconstructible as deconstructible

class ASCIIUsernameValidator(validators.RegexValidator):
    regex: str
    message: Incomplete
    flags: Incomplete

class UnicodeUsernameValidator(validators.RegexValidator):
    regex: str
    message: Incomplete
    flags: int
