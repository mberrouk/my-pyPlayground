"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable, Iterator
from contextlib import contextmanager
from types import TracebackType
from typing import Any, TypeVar, overload
from django.db import ProgrammingError

"""
This type stub file was generated by pyright.
"""
class TransactionManagementError(ProgrammingError):
    ...


def get_connection(using: str | None = ...) -> Any:
    ...

def get_autocommit(using: str | None = ...) -> bool:
    ...

def set_autocommit(autocommit: bool, using: str | None = ...) -> Any:
    ...

def commit(using: str | None = ...) -> None:
    ...

def rollback(using: str | None = ...) -> None:
    ...

def savepoint(using: str | None = ...) -> str:
    ...

def savepoint_rollback(sid: str, using: str | None = ...) -> None:
    ...

def savepoint_commit(sid: str, using: str | None = ...) -> None:
    ...

def clean_savepoints(using: str | None = ...) -> None:
    ...

def get_rollback(using: str | None = ...) -> bool:
    ...

def set_rollback(rollback: bool, using: str | None = ...) -> None:
    ...

@contextmanager
def mark_for_rollback_on_error(using: str | None = ...) -> Iterator[None]:
    ...

def on_commit(func: Callable[[], object], using: str | None = ..., robust: bool = ...) -> None:
    ...

_C = TypeVar("_C", bound=Callable)
class Atomic:
    using: str | None
    savepoint: bool
    def __init__(self, using: str | None, savepoint: bool, durable: bool) -> None:
        ...
    
    def __call__(self, func: _C) -> _C:
        ...
    
    def __enter__(self) -> None:
        ...
    
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None) -> None:
        ...
    


@overload
def atomic(using: _C) -> _C:
    ...

@overload
def atomic(using: str | None = ..., savepoint: bool = ..., durable: bool = ...) -> Atomic:
    ...

@overload
def non_atomic_requests(using: _C) -> _C:
    ...

@overload
def non_atomic_requests(using: str | None = ...) -> Callable[[_C], _C]:
    ...
