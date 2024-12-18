from _typeshed import Incomplete
from django.core.exceptions import ValidationError as ValidationError
from django.core.validators import MaxLengthValidator as MaxLengthValidator, MaxValueValidator as MaxValueValidator, MinLengthValidator as MinLengthValidator, MinValueValidator as MinValueValidator
from django.utils.deconstruct import deconstructible as deconstructible
from django.utils.translation import ngettext_lazy as ngettext_lazy

class ArrayMaxLengthValidator(MaxLengthValidator):
    message: Incomplete

class ArrayMinLengthValidator(MinLengthValidator):
    message: Incomplete

class KeysValidator:
    messages: Incomplete
    strict: bool
    keys: Incomplete
    def __init__(self, keys, strict: bool = False, messages: Incomplete | None = None) -> None: ...
    def __call__(self, value) -> None: ...
    def __eq__(self, other): ...

class RangeMaxValueValidator(MaxValueValidator):
    def compare(self, a, b): ...
    message: Incomplete

class RangeMinValueValidator(MinValueValidator):
    def compare(self, a, b): ...
    message: Incomplete
