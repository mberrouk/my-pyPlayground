from .base import BaseChannel as BaseChannel
from _typeshed import Incomplete
from channels.exceptions import HttpError as HttpError, ImproperlyConfigured as ImproperlyConfigured

class SlackChannel(BaseChannel):
    url: Incomplete
    username: Incomplete
    channel: Incomplete
    icon_emoji: Incomplete
    icon_url: Incomplete
    def __init__(self, url, username: Incomplete | None = None, channel: Incomplete | None = None, icon_emoji: Incomplete | None = None, icon_url: Incomplete | None = None, *args, **kwargs) -> None: ...
    def send(self, message, fail_silently: bool = False, options: Incomplete | None = None) -> None: ...
