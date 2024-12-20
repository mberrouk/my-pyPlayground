from _typeshed import Incomplete
from django.db import NotSupportedError as NotSupportedError
from django.db.models.expressions import Func as Func, Value as Value
from django.db.models.fields import TextField as TextField
from django.db.models.fields.json import JSONField as JSONField

class Cast(Func):
    function: str
    template: str
    def __init__(self, expression, output_field) -> None: ...
    def as_sql(self, compiler, connection, **extra_context): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...
    def as_mysql(self, compiler, connection, **extra_context): ...
    def as_postgresql(self, compiler, connection, **extra_context): ...
    def as_oracle(self, compiler, connection, **extra_context): ...

class Coalesce(Func):
    function: str
    def __init__(self, *expressions, **extra) -> None: ...
    @property
    def empty_result_set_value(self): ...
    def as_oracle(self, compiler, connection, **extra_context): ...

class Collate(Func):
    function: str
    template: str
    allowed_default: bool
    collation_re: Incomplete
    collation: Incomplete
    def __init__(self, expression, collation) -> None: ...
    def as_sql(self, compiler, connection, **extra_context): ...

class Greatest(Func):
    function: str
    def __init__(self, *expressions, **extra) -> None: ...
    def as_sqlite(self, compiler, connection, **extra_context): ...

class JSONObject(Func):
    function: str
    output_field: Incomplete
    def __init__(self, **fields) -> None: ...
    def as_sql(self, compiler, connection, **extra_context): ...
    def as_native(self, compiler, connection, *, returning, **extra_context): ...
    def as_postgresql(self, compiler, connection, **extra_context): ...
    def as_oracle(self, compiler, connection, **extra_context): ...

class Least(Func):
    function: str
    def __init__(self, *expressions, **extra) -> None: ...
    def as_sqlite(self, compiler, connection, **extra_context): ...

class NullIf(Func):
    function: str
    arity: int
    def as_oracle(self, compiler, connection, **extra_context): ...
