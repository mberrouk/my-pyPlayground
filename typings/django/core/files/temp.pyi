import os
import tempfile
from _typeshed import Incomplete
from django.core.files.utils import FileProxyMixin

__all__ = ['NamedTemporaryFile', 'gettempdir']

class TemporaryFile(FileProxyMixin):
    name: Incomplete
    file: Incomplete
    close_called: bool
    def __init__(self, mode: str = 'w+b', bufsize: int = -1, suffix: str = '', prefix: str = '', dir: Incomplete | None = None) -> None: ...
    unlink = os.unlink
    def close(self) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
NamedTemporaryFile = TemporaryFile
gettempdir = tempfile.gettempdir
