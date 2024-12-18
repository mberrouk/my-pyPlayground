from _typeshed import Incomplete

DEBUG: int
INFO: int
WARNING: int
ERROR: int
CRITICAL: int

class CheckMessage:
    level: Incomplete
    msg: Incomplete
    hint: Incomplete
    obj: Incomplete
    id: Incomplete
    def __init__(self, level, msg, hint: Incomplete | None = None, obj: Incomplete | None = None, id: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def is_serious(self, level=...): ...
    def is_silenced(self): ...

class Debug(CheckMessage):
    def __init__(self, *args, **kwargs) -> None: ...

class Info(CheckMessage):
    def __init__(self, *args, **kwargs) -> None: ...

class Warning(CheckMessage):
    def __init__(self, *args, **kwargs) -> None: ...

class Error(CheckMessage):
    def __init__(self, *args, **kwargs) -> None: ...

class Critical(CheckMessage):
    def __init__(self, *args, **kwargs) -> None: ...
