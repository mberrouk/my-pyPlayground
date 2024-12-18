from . import DEFAULT_CHANNEL_LAYER as DEFAULT_CHANNEL_LAYER
from .db import aclose_old_connections as aclose_old_connections, database_sync_to_async as database_sync_to_async
from .exceptions import StopConsumer as StopConsumer
from .layers import get_channel_layer as get_channel_layer
from .utils import await_many_dispatch as await_many_dispatch
from _typeshed import Incomplete

def get_handler_name(message): ...

class AsyncConsumer:
    channel_layer_alias = DEFAULT_CHANNEL_LAYER
    scope: Incomplete
    channel_layer: Incomplete
    channel_name: Incomplete
    channel_receive: Incomplete
    base_send: Incomplete
    async def __call__(self, scope, receive, send) -> None: ...
    async def dispatch(self, message) -> None: ...
    async def send(self, message) -> None: ...
    @classmethod
    def as_asgi(cls, **initkwargs): ...

class SyncConsumer(AsyncConsumer):
    def dispatch(self, message) -> None: ...
    def send(self, message) -> None: ...
