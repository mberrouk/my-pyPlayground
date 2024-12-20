"""
This type stub file was generated by pyright.
"""

from collections.abc import Iterator
from types import TracebackType
from typing import AnyStr, Callable, IO, type_check_only
from django.core.files.utils import FileProxyMixin
from django.utils.functional import cached_property
from typing_extensions import Self

class File(FileProxyMixin[AnyStr], IO[AnyStr]):
    DEFAULT_CHUNK_SIZE: int
    file: IO[AnyStr] | None
    name: str | None
    mode: str
    def __init__(self, file: IO[AnyStr] | None, name: str | None = ...) -> None:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def __len__(self) -> int:
        ...
    
    @cached_property
    def size(self) -> int:
        ...
    
    def chunks(self, chunk_size: int | None = ...) -> Iterator[AnyStr]:
        ...
    
    def multiple_chunks(self, chunk_size: int | None = ...) -> bool | None:
        ...
    
    def __iter__(self) -> Iterator[AnyStr]:
        ...
    
    def __enter__(self) -> Self:
        ...
    
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None) -> None:
        ...
    
    def open(self, mode: str | None = ..., buffering: int = ..., encoding: str | None = ..., errors: str | None = ..., newline: str | None = ..., closefd: bool = ..., opener: Callable[[str, int], int] | None = ...) -> Self:
        ...
    
    def close(self) -> None:
        ...
    
    @type_check_only
    def __next__(self) -> AnyStr:
        ...
    


class ContentFile(File[AnyStr]):
    file: IO[AnyStr]
    def __init__(self, content: AnyStr, name: str | None = ...) -> None:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def open(self, mode: str | None = ...) -> Self:
        ...
    
    def close(self) -> None:
        ...
    
    def write(self, data: AnyStr) -> int:
        ...
    


def endswith_cr(line: bytes | str) -> bool:
    ...

def endswith_lf(line: bytes | str) -> bool:
    ...

def equals_lf(line: bytes | str) -> bool:
    ...

