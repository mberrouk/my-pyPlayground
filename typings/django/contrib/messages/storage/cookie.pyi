import json
from _typeshed import Incomplete
from django.conf import settings as settings
from django.contrib.messages.storage.base import BaseStorage as BaseStorage, Message as Message
from django.core import signing as signing
from django.http import SimpleCookie as SimpleCookie
from django.utils.safestring import SafeData as SafeData, mark_safe as mark_safe

class MessageEncoder(json.JSONEncoder):
    message_key: str
    def default(self, obj): ...

class MessageDecoder(json.JSONDecoder):
    def process_messages(self, obj): ...
    def decode(self, s, **kwargs): ...

class MessagePartSerializer:
    def dumps(self, obj): ...

class MessagePartGatherSerializer:
    def dumps(self, obj): ...

class MessageSerializer:
    def loads(self, data): ...

class CookieStorage(BaseStorage):
    cookie_name: str
    max_cookie_size: int
    not_finished: str
    not_finished_json: Incomplete
    key_salt: str
    signer: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

def bisect_keep_left(a, fn): ...
def bisect_keep_right(a, fn): ...
