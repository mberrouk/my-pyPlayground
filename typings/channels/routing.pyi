from _typeshed import Incomplete

def get_default_application(): ...

class ProtocolTypeRouter:
    application_mapping: Incomplete
    def __init__(self, application_mapping) -> None: ...
    async def __call__(self, scope, receive, send): ...

class URLRouter:
    routes: Incomplete
    def __init__(self, routes) -> None: ...
    async def __call__(self, scope, receive, send): ...

class ChannelNameRouter:
    application_mapping: Incomplete
    def __init__(self, application_mapping) -> None: ...
    async def __call__(self, scope, receive, send): ...