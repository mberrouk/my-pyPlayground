from _typeshed import Incomplete
from django.utils.inspect import func_accepts_kwargs as func_accepts_kwargs

logger: Incomplete
NONE_ID: Incomplete
NO_RECEIVERS: Incomplete

class Signal:
    receivers: Incomplete
    lock: Incomplete
    use_caching: Incomplete
    sender_receivers_cache: Incomplete
    def __init__(self, use_caching: bool = False) -> None: ...
    def connect(self, receiver, sender: Incomplete | None = None, weak: bool = True, dispatch_uid: Incomplete | None = None) -> None: ...
    def disconnect(self, receiver: Incomplete | None = None, sender: Incomplete | None = None, dispatch_uid: Incomplete | None = None): ...
    def has_listeners(self, sender: Incomplete | None = None): ...
    def send(self, sender, **named): ...
    async def asend(self, sender, **named): ...
    def send_robust(self, sender, **named): ...
    async def asend_robust(self, sender, **named): ...

def receiver(signal, **kwargs): ...