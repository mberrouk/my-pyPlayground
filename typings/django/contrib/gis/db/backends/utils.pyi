from _typeshed import Incomplete

class SpatialOperator:
    sql_template: Incomplete
    op: Incomplete
    func: Incomplete
    def __init__(self, op: Incomplete | None = None, func: Incomplete | None = None) -> None: ...
    @property
    def default_template(self): ...
    def as_sql(self, connection, lookup, template_params, sql_params): ...
