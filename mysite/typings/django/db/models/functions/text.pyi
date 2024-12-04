"""
This type stub file was generated by pyright.
"""

from django.db.models.expressions import Func
from django.db.models.lookups import Transform

class MySQLSHA2Mixin:
    def as_mysql(self, compiler, connection, **extra_context):
        ...
    


class OracleHashMixin:
    def as_oracle(self, compiler, connection, **extra_context):
        ...
    


class PostgreSQLSHAMixin:
    def as_postgresql(self, compiler, connection, **extra_context):
        ...
    


class Chr(Transform):
    function = ...
    lookup_name = ...
    output_field = ...
    def as_mysql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class ConcatPair(Func):
    """
    Concatenate two arguments together. This is used by `Concat` because not
    all backend databases support more than two arguments.
    """
    function = ...
    def pipes_concat_sql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    as_sqlite = ...
    def as_postgresql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_mysql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def coalesce(self): # -> Self:
        ...
    


class Concat(Func):
    """
    Concatenate text fields together. Backends that result in an entire
    null expression when any arguments are null will wrap each argument in
    coalesce functions to ensure a non-null result.
    """
    function = ...
    template = ...
    def __init__(self, *expressions, **extra) -> None:
        ...
    


class Left(Func):
    function = ...
    arity = ...
    output_field = ...
    def __init__(self, expression, length, **extra) -> None:
        """
        expression: the name of a field, or an expression returning a string
        length: the number of characters to return from the start of the string
        """
        ...
    
    def get_substr(self): # -> Substr:
        ...
    
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Length(Transform):
    """Return the number of characters in the expression."""
    function = ...
    lookup_name = ...
    output_field = ...
    def as_mysql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Lower(Transform):
    function = ...
    lookup_name = ...


class LPad(Func):
    function = ...
    output_field = ...
    def __init__(self, expression, length, fill_text=..., **extra) -> None:
        ...
    


class LTrim(Transform):
    function = ...
    lookup_name = ...


class MD5(OracleHashMixin, Transform):
    function = ...
    lookup_name = ...


class Ord(Transform):
    function = ...
    lookup_name = ...
    output_field = ...
    def as_mysql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Repeat(Func):
    function = ...
    output_field = ...
    def __init__(self, expression, number, **extra) -> None:
        ...
    
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Replace(Func):
    function = ...
    def __init__(self, expression, text, replacement=..., **extra) -> None:
        ...
    


class Reverse(Transform):
    function = ...
    lookup_name = ...
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Right(Left):
    function = ...
    def get_substr(self): # -> Substr:
        ...
    


class RPad(LPad):
    function = ...


class RTrim(Transform):
    function = ...
    lookup_name = ...


class SHA1(OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function = ...
    lookup_name = ...


class SHA224(MySQLSHA2Mixin, PostgreSQLSHAMixin, Transform):
    function = ...
    lookup_name = ...
    def as_oracle(self, compiler, connection, **extra_context):
        ...
    


class SHA256(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function = ...
    lookup_name = ...


class SHA384(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function = ...
    lookup_name = ...


class SHA512(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform):
    function = ...
    lookup_name = ...


class StrIndex(Func):
    """
    Return a positive integer corresponding to the 1-indexed position of the
    first occurrence of a substring inside another string, or 0 if the
    substring is not found.
    """
    function = ...
    arity = ...
    output_field = ...
    def as_postgresql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Substr(Func):
    function = ...
    output_field = ...
    def __init__(self, expression, pos, length=..., **extra) -> None:
        """
        expression: the name of a field, or an expression returning a string
        pos: an integer > 0, or an expression returning an integer
        length: an optional number of characters to return
        """
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Trim(Transform):
    function = ...
    lookup_name = ...


class Upper(Transform):
    function = ...
    lookup_name = ...


