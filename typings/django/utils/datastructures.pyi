from _typeshed import Incomplete
from collections.abc import Generator, Mapping

class OrderedSet:
    dict: Incomplete
    def __init__(self, iterable: Incomplete | None = None) -> None: ...
    def add(self, item) -> None: ...
    def remove(self, item) -> None: ...
    def discard(self, item) -> None: ...
    def __iter__(self): ...
    def __reversed__(self): ...
    def __contains__(self, item) -> bool: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...

class MultiValueDictKeyError(KeyError): ...

class MultiValueDict(dict):
    def __init__(self, key_to_list_mapping=()) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def get(self, key, default: Incomplete | None = None): ...
    def getlist(self, key, default: Incomplete | None = None): ...
    def setlist(self, key, list_) -> None: ...
    def setdefault(self, key, default: Incomplete | None = None): ...
    def setlistdefault(self, key, default_list: Incomplete | None = None): ...
    def appendlist(self, key, value) -> None: ...
    def items(self) -> Generator[Incomplete]: ...
    def lists(self): ...
    def values(self) -> Generator[Incomplete]: ...
    def copy(self): ...
    def update(self, *args, **kwargs) -> None: ...
    def dict(self): ...

class ImmutableList(tuple):
    warning: Incomplete
    def __new__(cls, *args, warning: str = 'ImmutableList object is immutable.', **kwargs): ...
    def complain(self, *args, **kwargs) -> None: ...
    __delitem__ = complain
    __delslice__ = complain
    __iadd__ = complain
    __imul__ = complain
    __setitem__ = complain
    __setslice__ = complain
    append = complain
    extend = complain
    insert = complain
    pop = complain
    remove = complain
    sort = complain
    reverse = complain

class DictWrapper(dict):
    func: Incomplete
    prefix: Incomplete
    def __init__(self, data, func, prefix) -> None: ...
    def __getitem__(self, key): ...

class CaseInsensitiveMapping(Mapping):
    def __init__(self, data) -> None: ...
    def __getitem__(self, key): ...
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    def __iter__(self): ...
    def copy(self): ...