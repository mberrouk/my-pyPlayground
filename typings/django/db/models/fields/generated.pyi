from . import Field
from _typeshed import Incomplete

__all__ = ['GeneratedField']

class GeneratedField(Field):
    generated: bool
    db_returning: bool
    output_field: Incomplete
    expression: Incomplete
    db_persist: Incomplete
    def __init__(self, *, expression, output_field, db_persist: Incomplete | None = None, **kwargs) -> None: ...
    def cached_col(self): ...
    def get_col(self, alias, output_field: Incomplete | None = None): ...
    def contribute_to_class(self, *args, **kwargs) -> None: ...
    def generated_sql(self, connection): ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def db_parameters(self, connection): ...
    def db_type_parameters(self, connection): ...
