from _typeshed import Incomplete
from contextlib import ContextDecorator

__all__ = ['get_fixed_timezone', 'get_default_timezone', 'get_default_timezone_name', 'get_current_timezone', 'get_current_timezone_name', 'activate', 'deactivate', 'override', 'localtime', 'localdate', 'now', 'is_aware', 'is_naive', 'make_aware', 'make_naive']

def get_fixed_timezone(offset): ...
def get_default_timezone(): ...
def get_default_timezone_name(): ...
def get_current_timezone(): ...
def get_current_timezone_name(): ...
def activate(timezone) -> None: ...
def deactivate() -> None: ...

class override(ContextDecorator):
    timezone: Incomplete
    def __init__(self, timezone) -> None: ...
    old_timezone: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def localtime(value: Incomplete | None = None, timezone: Incomplete | None = None): ...
def localdate(value: Incomplete | None = None, timezone: Incomplete | None = None): ...
def now(): ...
def is_aware(value): ...
def is_naive(value): ...
def make_aware(value, timezone: Incomplete | None = None): ...
def make_naive(value, timezone: Incomplete | None = None): ...
