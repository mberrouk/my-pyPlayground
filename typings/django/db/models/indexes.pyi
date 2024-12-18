from _typeshed import Incomplete
from django.db.models.expressions import Func

__all__ = ['Index']

class Index:
    suffix: str
    max_name_length: int
    fields: Incomplete
    fields_orders: Incomplete
    name: Incomplete
    db_tablespace: Incomplete
    opclasses: Incomplete
    condition: Incomplete
    include: Incomplete
    expressions: Incomplete
    def __init__(self, *expressions, fields=(), name: Incomplete | None = None, db_tablespace: Incomplete | None = None, opclasses=(), condition: Incomplete | None = None, include: Incomplete | None = None) -> None: ...
    @property
    def contains_expressions(self): ...
    def create_sql(self, model, schema_editor, using: str = '', **kwargs): ...
    def remove_sql(self, model, schema_editor, **kwargs): ...
    def deconstruct(self): ...
    def clone(self): ...
    def set_name_with_model(self, model) -> None: ...
    def __eq__(self, other): ...

class IndexExpression(Func):
    template: str
    wrapper_classes: Incomplete
    def set_wrapper_classes(self, connection: Incomplete | None = None) -> None: ...
    @classmethod
    def register_wrappers(cls, *wrapper_classes) -> None: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...
