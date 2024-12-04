"""
This type stub file was generated by pyright.
"""

from django.utils.deconstruct import deconstructible
from django.utils.functional import cached_property
from .base import Storage
from .mixins import StorageSettingsMixin

@deconstructible(path="django.core.files.storage.FileSystemStorage")
class FileSystemStorage(Storage, StorageSettingsMixin):
    """
    Standard filesystem storage
    """
    OS_OPEN_FLAGS = ...
    def __init__(self, location=..., base_url=..., file_permissions_mode=..., directory_permissions_mode=..., allow_overwrite=...) -> None:
        ...
    
    @cached_property
    def base_location(self): # -> Any:
        ...
    
    @cached_property
    def location(self):
        ...
    
    @cached_property
    def base_url(self): # -> Any:
        ...
    
    @cached_property
    def file_permissions_mode(self): # -> Any:
        ...
    
    @cached_property
    def directory_permissions_mode(self): # -> Any:
        ...
    
    def delete(self, name): # -> None:
        ...
    
    def is_name_available(self, name, max_length=...): # -> bool:
        ...
    
    def get_alternative_name(self, file_root, file_ext): # -> str:
        ...
    
    def exists(self, name): # -> bool:
        ...
    
    def listdir(self, path): # -> tuple[list[Any], list[Any]]:
        ...
    
    def path(self, name):
        ...
    
    def size(self, name): # -> int:
        ...
    
    def url(self, name): # -> str:
        ...
    
    def get_accessed_time(self, name): # -> datetime:
        ...
    
    def get_created_time(self, name): # -> datetime:
        ...
    
    def get_modified_time(self, name): # -> datetime:
        ...
    


