from .base import Storage as Storage
from .filesystem import FileSystemStorage as FileSystemStorage
from .handler import InvalidStorageError as InvalidStorageError, StorageHandler as StorageHandler
from .memory import InMemoryStorage as InMemoryStorage
from _typeshed import Incomplete
from django.utils.functional import LazyObject

__all__ = ['FileSystemStorage', 'InMemoryStorage', 'Storage', 'DefaultStorage', 'default_storage', 'InvalidStorageError', 'StorageHandler', 'storages']

class DefaultStorage(LazyObject): ...

storages: Incomplete
default_storage: Incomplete
