from .base import BaseChannel as BaseChannel
from _typeshed import Incomplete
from channels.exceptions import HttpError as HttpError

class TwitterChannel(BaseChannel):
    url: str
    api_key: Incomplete
    api_secret: Incomplete
    access_token: Incomplete
    access_token_secret: Incomplete
    def __init__(self, api_key, api_secret, access_token, access_token_secret, *args, **kwargs) -> None: ...
    def send(self, message, fail_silently: bool = False, options: Incomplete | None = None) -> None: ...
