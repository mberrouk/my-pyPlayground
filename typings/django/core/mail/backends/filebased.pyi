from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend

class EmailBackend(ConsoleEmailBackend):
    file_path: Incomplete
    def __init__(self, *args, file_path: Incomplete | None = None, **kwargs) -> None: ...
    def write_message(self, message) -> None: ...
    stream: Incomplete
    def open(self): ...
    def close(self) -> None: ...
