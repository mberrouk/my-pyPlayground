from _typeshed import Incomplete
from collections.abc import Generator
from django.core.files.base import File

__all__ = ['UploadedFile', 'TemporaryUploadedFile', 'InMemoryUploadedFile', 'SimpleUploadedFile']

class UploadedFile(File):
    size: Incomplete
    content_type: Incomplete
    charset: Incomplete
    content_type_extra: Incomplete
    def __init__(self, file: Incomplete | None = None, name: Incomplete | None = None, content_type: Incomplete | None = None, size: Incomplete | None = None, charset: Incomplete | None = None, content_type_extra: Incomplete | None = None) -> None: ...
    name: Incomplete

class TemporaryUploadedFile(UploadedFile):
    def __init__(self, name, content_type, size, charset, content_type_extra: Incomplete | None = None) -> None: ...
    def temporary_file_path(self): ...
    def close(self): ...

class InMemoryUploadedFile(UploadedFile):
    field_name: Incomplete
    def __init__(self, file, field_name, name, content_type, size, charset, content_type_extra: Incomplete | None = None) -> None: ...
    def open(self, mode: Incomplete | None = None): ...
    def chunks(self, chunk_size: Incomplete | None = None) -> Generator[Incomplete]: ...
    def multiple_chunks(self, chunk_size: Incomplete | None = None): ...

class SimpleUploadedFile(InMemoryUploadedFile):
    def __init__(self, name, content, content_type: str = 'text/plain') -> None: ...
    @classmethod
    def from_dict(cls, file_dict): ...
