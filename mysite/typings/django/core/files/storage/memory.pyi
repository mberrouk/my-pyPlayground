"""
This type stub file was generated by pyright.
"""

from django.core.files.base import ContentFile
from django.utils.deconstruct import deconstructible
from django.utils.functional import cached_property
from .base import Storage
from .mixins import StorageSettingsMixin

"""
Based on dj-inmemorystorage (BSD) by Cody Soyland, Seán Hayes, Tore Birkeland,
and Nick Presta.
"""
__all__ = ("InMemoryStorage", )
class TimingMixin:
    ...


class InMemoryFileNode(ContentFile, TimingMixin):
    """
    Helper class representing an in-memory file node.

    Handle unicode/bytes conversion during I/O operations and record creation,
    modification, and access times.
    """
    def __init__(self, content=..., name=...) -> None:
        ...
    
    def open(self, mode): # -> Self:
        ...
    
    def write(self, data): # -> None:
        ...
    


class InMemoryDirNode(TimingMixin):
    """
    Helper class representing an in-memory directory node.

    Handle path navigation of directory trees, creating missing nodes if
    needed.
    """
    def __init__(self) -> None:
        ...
    
    def resolve(self, path, create_if_missing=..., leaf_cls=..., check_exists=...): # -> Self | None:
        """
        Navigate current directory tree, returning node matching path or
        creating a new one, if missing.
        - path: path of the node to search
        - create_if_missing: create nodes if not exist. Defaults to False.
        - leaf_cls: expected type of leaf node. Defaults to None.
        - check_exists: if True and the leaf node does not exist, raise a
          FileNotFoundError. Defaults to True.
        """
        ...
    
    def listdir(self): # -> tuple[list[Any], list[Any]]:
        ...
    
    def remove_child(self, name): # -> None:
        ...
    


@deconstructible(path="django.core.files.storage.InMemoryStorage")
class InMemoryStorage(Storage, StorageSettingsMixin):
    """A storage saving files in memory."""
    def __init__(self, location=..., base_url=..., file_permissions_mode=..., directory_permissions_mode=...) -> None:
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
    
    def path(self, name):
        ...
    
    def delete(self, name): # -> None:
        ...
    
    def exists(self, name): # -> bool:
        ...
    
    def listdir(self, path): # -> tuple[list[Any], list[Any]]:
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
    


