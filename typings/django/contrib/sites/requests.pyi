from _typeshed import Incomplete

class RequestSite:
    domain: Incomplete
    def __init__(self, request) -> None: ...
    def save(self, force_insert: bool = False, force_update: bool = False) -> None: ...
    def delete(self) -> None: ...