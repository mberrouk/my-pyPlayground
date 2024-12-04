"""
This type stub file was generated by pyright.
"""

from datetime import datetime
from typing import Any, IO
from django.core.files.base import File
from django.utils._os import _PathCompatible

class Storage:
    def open(self, name: str, mode: str = ...) -> File:
        ...
    
    def save(self, name: str | None, content: IO[Any], max_length: int | None = ...) -> str:
        ...
    
    def get_valid_name(self, name: str) -> str:
        ...
    
    def get_alternative_name(self, file_root: str, file_ext: str) -> str:
        ...
    
    def get_available_name(self, name: str, max_length: int | None = ...) -> str:
        ...
    
    def generate_filename(self, filename: _PathCompatible) -> str:
        ...
    
    def path(self, name: str) -> str:
        ...
    
    def delete(self, name: str) -> None:
        ...
    
    def exists(self, name: str) -> bool:
        ...
    
    def listdir(self, path: str) -> tuple[list[str], list[str]]:
        ...
    
    def size(self, name: str) -> int:
        ...
    
    def url(self, name: str | None) -> str:
        ...
    
    def get_accessed_time(self, name: str) -> datetime:
        ...
    
    def get_created_time(self, name: str) -> datetime:
        ...
    
    def get_modified_time(self, name: str) -> datetime:
        ...
    


