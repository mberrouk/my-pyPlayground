from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.mail.backends.base import BaseEmailBackend as BaseEmailBackend
from django.core.mail.message import sanitize_address as sanitize_address
from django.core.mail.utils import DNS_NAME as DNS_NAME
from django.utils.functional import cached_property as cached_property

class EmailBackend(BaseEmailBackend):
    host: Incomplete
    port: Incomplete
    username: Incomplete
    password: Incomplete
    use_tls: Incomplete
    use_ssl: Incomplete
    timeout: Incomplete
    ssl_keyfile: Incomplete
    ssl_certfile: Incomplete
    connection: Incomplete
    def __init__(self, host: Incomplete | None = None, port: Incomplete | None = None, username: Incomplete | None = None, password: Incomplete | None = None, use_tls: Incomplete | None = None, fail_silently: bool = False, use_ssl: Incomplete | None = None, timeout: Incomplete | None = None, ssl_keyfile: Incomplete | None = None, ssl_certfile: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def connection_class(self): ...
    def ssl_context(self): ...
    def open(self): ...
    def close(self) -> None: ...
    def send_messages(self, email_messages): ...
