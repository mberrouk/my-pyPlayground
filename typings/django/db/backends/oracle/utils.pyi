import datetime
from .base import Database as Database
from _typeshed import Incomplete

class InsertVar:
    types: Incomplete
    db_type: Incomplete
    bound_param: Incomplete
    def __init__(self, field) -> None: ...
    def bind_parameter(self, cursor): ...
    def get_value(self): ...

class Oracle_datetime(datetime.datetime):
    input_size: Incomplete
    @classmethod
    def from_datetime(cls, dt): ...

class BulkInsertMapper:
    BLOB: str
    DATE: str
    INTERVAL: str
    NCLOB: str
    NUMBER: str
    TIMESTAMP: str
    types: Incomplete

def dsn(settings_dict): ...
