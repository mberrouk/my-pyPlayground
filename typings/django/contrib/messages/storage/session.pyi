from django.contrib.messages.storage.base import BaseStorage as BaseStorage
from django.contrib.messages.storage.cookie import MessageDecoder as MessageDecoder, MessageEncoder as MessageEncoder
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured

class SessionStorage(BaseStorage):
    session_key: str
    def __init__(self, request, *args, **kwargs) -> None: ...
    def serialize_messages(self, messages): ...
    def deserialize_messages(self, data): ...
