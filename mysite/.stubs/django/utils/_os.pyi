"""
This type stub file was generated by pyright.
"""

import os
from pathlib import Path
from typing_extensions import TypeAlias

"""
This type stub file was generated by pyright.
"""
_PathCompatible: TypeAlias = str | os.PathLike[str]
def safe_join(base: _PathCompatible, *paths: _PathCompatible) -> str:
    ...

def symlinks_supported() -> bool:
    ...

def to_path(value: Path | str) -> Path:
    ...

