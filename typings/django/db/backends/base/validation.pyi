from _typeshed import Incomplete

class BaseDatabaseValidation:
    connection: Incomplete
    def __init__(self, connection) -> None: ...
    def check(self, **kwargs): ...
    def check_field(self, field, **kwargs): ...