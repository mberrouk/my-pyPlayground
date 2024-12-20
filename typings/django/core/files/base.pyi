from _typeshed import Incomplete
from collections.abc import Generator
from django.core.files.utils import FileProxyMixin as FileProxyMixin
from django.utils.functional import cached_property as cached_property

class File(FileProxyMixin):
    DEFAULT_CHUNK_SIZE: Incomplete
    file: Incomplete
    name: Incomplete
    mode: Incomplete
    def __init__(self, file, name: Incomplete | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def size(self): ...
    def chunks(self, chunk_size: Incomplete | None = None) -> Generator[Incomplete]: ...
    def multiple_chunks(self, chunk_size: Incomplete | None = None): ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def open(self, mode: Incomplete | None = None, *args, **kwargs): ...
    def close(self) -> None: ...

class ContentFile(File):
    size: Incomplete
    def __init__(self, content, name: Incomplete | None = None) -> None: ...
    def __bool__(self) -> bool: ...
    def open(self, mode: Incomplete | None = None): ...
    def close(self) -> None: ...
    def write(self, data): ...

def endswith_cr(line): ...
def endswith_lf(line): ...
def equals_lf(line): ...
