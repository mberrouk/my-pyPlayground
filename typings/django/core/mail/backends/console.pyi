from _typeshed import Incomplete
from django.core.mail.backends.base import BaseEmailBackend as BaseEmailBackend

class EmailBackend(BaseEmailBackend):
    stream: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def write_message(self, message) -> None: ...
    def send_messages(self, email_messages): ...