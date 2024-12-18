from _typeshed import Incomplete
from django.contrib.messages.storage.base import BaseStorage as BaseStorage
from django.contrib.messages.storage.cookie import CookieStorage as CookieStorage
from django.contrib.messages.storage.session import SessionStorage as SessionStorage

class FallbackStorage(BaseStorage):
    storage_classes: Incomplete
    storages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
