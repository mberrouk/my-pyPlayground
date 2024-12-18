from .base import BaseChannel as BaseChannel
from _typeshed import Incomplete
from channels.exceptions import HttpError as HttpError

class YoChannel(BaseChannel):
    url: str
    api_token: Incomplete
    username: Incomplete
    def __init__(self, api_token, username: Incomplete | None = None, *args, **kwargs) -> None: ...
    def send(self, message, fail_silently: bool = False, options: Incomplete | None = None) -> None: ...
