from _typeshed import Incomplete

class PermLookupDict:
    def __init__(self, user, app_label) -> None: ...
    def __getitem__(self, perm_name): ...
    def __iter__(self): ...
    def __bool__(self) -> bool: ...

class PermWrapper:
    user: Incomplete
    def __init__(self, user) -> None: ...
    def __getitem__(self, app_label): ...
    def __iter__(self): ...
    def __contains__(self, perm_name) -> bool: ...

def auth(request): ...
