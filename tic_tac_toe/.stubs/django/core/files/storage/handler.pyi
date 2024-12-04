"""
This type stub file was generated by pyright.
"""

from typing import Any
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import cached_property
from .base import Storage

class InvalidStorageError(ImproperlyConfigured):
    ...


class StorageHandler:
    def __init__(self, backends: dict[str, Storage] | None = ...) -> None:
        ...
    
    @cached_property
    def backends(self) -> dict[str, Storage]:
        ...
    
    def __getitem__(self, alias: str) -> Storage:
        ...
    
    def create_storage(self, params: dict[str, Any]) -> Storage:
        ...
    


