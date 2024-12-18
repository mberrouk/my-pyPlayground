from .base import BaseChannel as BaseChannel
from _typeshed import Incomplete
from channels.exceptions import HttpError as HttpError, ImproperlyConfigured as ImproperlyConfigured

class HipChatChannel(BaseChannel):
    colors: Incomplete
    message_formats: Incomplete
    url: Incomplete
    color: Incomplete
    notify: Incomplete
    message_format: Incomplete
    def __init__(self, api_id, token, base_url: str = 'https://api.hipchat.com/v2/', color: Incomplete | None = None, notify: Incomplete | None = None, message_format: str = 'html', *args, **kwargs) -> None: ...
    def send(self, message, fail_silently: bool = False, options: Incomplete | None = None) -> None: ...
