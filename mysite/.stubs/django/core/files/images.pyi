"""
This type stub file was generated by pyright.
"""

from typing import IO
from django.core.files import File
from django.utils._os import _PathCompatible

"""
This type stub file was generated by pyright.
"""
class ImageFile(File[bytes]):
    @property
    def width(self) -> int:
        ...
    
    @property
    def height(self) -> int:
        ...
    


def get_image_dimensions(file_or_path: _PathCompatible | IO[bytes], close: bool = ...) -> tuple[int | None, int | None]:
    ...

