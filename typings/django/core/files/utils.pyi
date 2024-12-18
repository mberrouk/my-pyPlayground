from _typeshed import Incomplete
from django.core.exceptions import SuspiciousFileOperation as SuspiciousFileOperation

def validate_file_name(name, allow_relative_path: bool = False): ...

class FileProxyMixin:
    encoding: Incomplete
    fileno: Incomplete
    flush: Incomplete
    isatty: Incomplete
    newlines: Incomplete
    read: Incomplete
    readinto: Incomplete
    readline: Incomplete
    readlines: Incomplete
    seek: Incomplete
    tell: Incomplete
    truncate: Incomplete
    write: Incomplete
    writelines: Incomplete
    @property
    def closed(self): ...
    def readable(self): ...
    def writable(self): ...
    def seekable(self): ...
    def __iter__(self): ...
