"""
This type stub file was generated by pyright.
"""

import enum
import sys
from typing import Any, TypeVar, overload, type_check_only
from _typeshed import ConvertibleToInt
from django.utils.functional import _StrOrPromise
from typing_extensions import TypeAlias

"""
This type stub file was generated by pyright.
"""
_Self = TypeVar("_Self")
if sys.version_info >= (3, 11):
    _enum_property = enum.property
    EnumType = enum.EnumType
    IntEnum = enum.IntEnum
    StrEnum = enum.StrEnum
else:
    ...
class ChoicesMeta(EnumType):
    def __new__(metacls: type[_Self], classname: str, bases: tuple[type, ...], classdict: enum._EnumDict, **kwds: Any) -> _Self:
        ...
    
    def __contains__(self, member: Any) -> bool:
        ...
    
    @property
    def names(self) -> list[str]:
        ...
    
    @property
    def choices(self) -> list[tuple[Any, str]]:
        ...
    
    @property
    def labels(self) -> list[str]:
        ...
    
    @property
    def values(self) -> list[Any]:
        ...
    


ChoicesType: TypeAlias = ChoicesMeta
class Choices(enum.Enum, metaclass=ChoicesType):
    @property
    def label(self) -> str:
        ...
    
    @_enum_property
    def value(self) -> Any:
        ...
    
    @property
    def do_not_call_in_templates(self) -> bool:
        ...
    


@type_check_only
class _IntegerChoicesMeta(ChoicesType):
    @property
    def choices(self) -> list[tuple[int, str]]:
        ...
    
    @property
    def values(self) -> list[int]:
        ...
    


class IntegerChoices(Choices, IntEnum, metaclass=_IntegerChoicesMeta):
    @overload
    def __init__(self, x: ConvertibleToInt) -> None:
        ...
    
    @overload
    def __init__(self, x: ConvertibleToInt, label: _StrOrPromise) -> None:
        ...
    
    @_enum_property
    def value(self) -> int:
        ...
    


@type_check_only
class _TextChoicesMeta(ChoicesType):
    @property
    def choices(self) -> list[tuple[str, str]]:
        ...
    
    @property
    def values(self) -> list[str]:
        ...
    


class TextChoices(Choices, StrEnum, metaclass=_TextChoicesMeta):
    @overload
    def __init__(self, object: str) -> None:
        ...
    
    @overload
    def __init__(self, object: str, label: _StrOrPromise) -> None:
        ...
    
    @_enum_property
    def value(self) -> str:
        ...
    

