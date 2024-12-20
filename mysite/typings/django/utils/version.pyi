"""
This type stub file was generated by pyright.
"""

import functools

"""
This type stub file was generated by pyright.
"""
PYPY = ...
PY38 = ...
PY39 = ...
PY310 = ...
PY311 = ...
PY312 = ...
PY313 = ...
def get_version(version=...):
    """Return a PEP 440-compliant version number from VERSION."""
    ...

def get_main_version(version=...):
    """Return main version (X.Y[.Z]) from VERSION."""
    ...

def get_complete_version(version=...):
    """
    Return a tuple of the django version. If version argument is non-empty,
    check for correctness of the tuple provided.
    """
    ...

def get_docs_version(version=...):
    ...

@functools.lru_cache
def get_git_changeset():
    """Return a numeric identifier of the latest git changeset.

    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    ...

version_component_re = ...
def get_version_tuple(version):
    """
    Return a tuple of version numbers (e.g. (1, 2, 3)) from the version
    string (e.g. '1.2.3').
    """
    ...

