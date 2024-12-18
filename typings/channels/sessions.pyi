from _typeshed import Incomplete
from channels.db import database_sync_to_async as database_sync_to_async

class CookieMiddleware:
    inner: Incomplete
    def __init__(self, inner) -> None: ...
    async def __call__(self, scope, receive, send): ...
    @classmethod
    def set_cookie(cls, message, key, value: str = '', max_age: Incomplete | None = None, expires: Incomplete | None = None, path: str = '/', domain: Incomplete | None = None, secure: bool = False, httponly: bool = False, samesite: str = 'lax') -> None: ...
    @classmethod
    def delete_cookie(cls, message, key, path: str = '/', domain: Incomplete | None = None): ...

class InstanceSessionWrapper:
    save_message_types: Incomplete
    cookie_response_message_types: Incomplete
    cookie_name: Incomplete
    session_store: Incomplete
    scope: Incomplete
    activated: bool
    real_send: Incomplete
    def __init__(self, scope, send) -> None: ...
    async def resolve_session(self) -> None: ...
    async def send(self, message): ...
    async def save_session(self) -> None: ...

class SessionMiddleware:
    inner: Incomplete
    def __init__(self, inner) -> None: ...
    async def __call__(self, scope, receive, send): ...

def SessionMiddlewareStack(inner): ...
