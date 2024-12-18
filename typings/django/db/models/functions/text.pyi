from _typeshed import Incomplete
from django.db import NotSupportedError as NotSupportedError
from django.db.models.expressions import Func as Func, Value as Value
from django.db.models.fields import CharField as CharField, IntegerField as IntegerField, TextField as TextField
from django.db.models.functions import Cast as Cast, Coalesce as Coalesce
from django.db.models.lookups import Transform as Transform

class MySQLSHA2Mixin:
    def as_mysql(self, compiler, connection, **extra_context): ...

class OracleHashMixin:
    def as_oracle(self, compiler, connection, **extra_context): ...

class PostgreSQLSHAMixin:
    def as_postgresql(self, compiler, connection, **extra_context): ...

class Chr(Transform):
    function: str
    lookup_name: str
    output_field: Incomplete
    def as_mysql(self, compiler, connection, **extra_context): ...
    def as_oracle(self, compiler, connection, **extra_context): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...

class ConcatPair(Func):
    function: str
    def pipes_concat_sql(self, compiler, connection, **extra_context): ...
    as_sqlite = pipes_concat_sql
    def as_postgresql(self, compiler, connection, **extra_context): ...
    def as_mysql(self, compiler, connection, **extra_context): ...
    def coalesce(self): ...

class Concat(Func):
    function: Incomplete
    template: str
    def __init__(self, *expressions, **extra) -> None: ...

class Left(Func):
    function: str
    arity: int
    output_field: Incomplete
    def __init__(self, expression, length, **extra) -> None: ...
    def get_substr(self): ...
    def as_oracle(self, compiler, connection, **extra_context): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...

class Length(Transform):
    function: str
    lookup_name: str
    output_field: Incomplete
    def as_mysql(self, compiler, connection, **extra_context): ...

class Lower(Transform):
    function: str
    lookup_name: str

class LPad(Func):
    function: str
    output_field: Incomplete
    def __init__(self, expression, length, fill_text=..., **extra) -> None: ...

class LTrim(Transform):
    function: str
    lookup_name: str

class MD5(OracleHashMixin, Transform):
    function: str
    lookup_name: str

class Ord(Transform):
    function: str
    lookup_name: str
    output_field: Incomplete
    def as_mysql(self, compiler, connection, **extra_context): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...

class Repeat(Func):
    function: str
    output_field: Incomplete
    def __init__(self, expression, number, **extra) -> None: ...
    def as_oracle(self, compiler, connection, **extra_context): ...

class Replace(Func):
    function: str
    def __init__(self, expression, text, replacement=..., **extra) -> None: ...

class Reverse(Transform):
    function: str
    lookup_name: str
    def as_oracle(self, compiler, connection, **extra_context): ...

class Right(Left):
    function: str
    def get_substr(self): ...

class RPad(LPad):
    function: str

class RTrim(Transform):
    function: str
    lookup_name: str

class SHA1(OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function: str
    lookup_name: str

class SHA224(MySQLSHA2Mixin, PostgreSQLSHAMixin, Transform):
    function: str
    lookup_name: str
    def as_oracle(self, compiler, connection, **extra_context) -> None: ...

class SHA256(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function: str
    lookup_name: str

class SHA384(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function: str
    lookup_name: str

class SHA512(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function: str
    lookup_name: str

class StrIndex(Func):
    function: str
    arity: int
    output_field: Incomplete
    def as_postgresql(self, compiler, connection, **extra_context): ...

class Substr(Func):
    function: str
    output_field: Incomplete
    def __init__(self, expression, pos, length: Incomplete | None = None, **extra) -> None: ...
    def as_sqlite(self, compiler, connection, **extra_context): ...
    def as_oracle(self, compiler, connection, **extra_context): ...

class Trim(Transform):
    function: str
    lookup_name: str

class Upper(Transform):
    function: str
    lookup_name: str
