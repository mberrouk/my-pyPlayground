"""
This type stub file was generated by pyright.
"""

from django.db.models.expressions import Func

"""Database functions that do comparisons or type conversions."""
class Cast(Func):
    """Coerce an expression to a new field type."""
    function = ...
    template = ...
    def __init__(self, expression, output_field) -> None:
        ...
    
    def as_sql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_mysql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_postgresql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Coalesce(Func):
    """Return, from left to right, the first non-null expression."""
    function = ...
    def __init__(self, *expressions, **extra) -> None:
        ...
    
    @property
    def empty_result_set_value(self): # -> None:
        ...
    
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Collate(Func):
    function = ...
    template = ...
    allowed_default = ...
    collation_re = ...
    def __init__(self, expression, collation) -> None:
        ...
    
    def as_sql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Greatest(Func):
    """
    Return the maximum expression.

    If any expression is null the return value is database-specific:
    On PostgreSQL, the maximum not-null expression is returned.
    On MySQL, Oracle, and SQLite, if any expression is null, null is returned.
    """
    function = ...
    def __init__(self, *expressions, **extra) -> None:
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Any, Any]:
        """Use the MAX function on SQLite."""
        ...
    


class JSONObject(Func):
    function = ...
    output_field = ...
    def __init__(self, **fields) -> None:
        ...
    
    def as_sql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_native(self, compiler, connection, *, returning, **extra_context): # -> tuple[Any, list[Any]]:
        class ArgJoiner:
            ...
        
        
    
    def as_postgresql(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


class Least(Func):
    """
    Return the minimum expression.

    If any expression is null the return value is database-specific:
    On PostgreSQL, return the minimum not-null expression.
    On MySQL, Oracle, and SQLite, if any expression is null, return null.
    """
    function = ...
    def __init__(self, *expressions, **extra) -> None:
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Any, Any]:
        """Use the MIN function on SQLite."""
        ...
    


class NullIf(Func):
    function = ...
    arity = ...
    def as_oracle(self, compiler, connection, **extra_context): # -> tuple[Any, list[Any]]:
        ...
    


