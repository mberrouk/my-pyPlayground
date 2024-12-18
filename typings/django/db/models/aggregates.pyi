from _typeshed import Incomplete
from django.db.models.expressions import Func
from django.db.models.functions.mixins import FixDurationInputMixin, NumericOutputFieldMixin

__all__ = ['Aggregate', 'Avg', 'Count', 'Max', 'Min', 'StdDev', 'Sum', 'Variance']

class Aggregate(Func):
    template: str
    contains_aggregate: bool
    name: Incomplete
    filter_template: str
    window_compatible: bool
    allow_distinct: bool
    empty_result_set_value: Incomplete
    distinct: Incomplete
    filter: Incomplete
    default: Incomplete
    def __init__(self, *expressions, distinct: bool = False, filter: Incomplete | None = None, default: Incomplete | None = None, **extra) -> None: ...
    def get_source_fields(self): ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    @property
    def default_alias(self): ...
    def get_group_by_cols(self): ...
    def as_sql(self, compiler, connection, **extra_context): ...

class Avg(FixDurationInputMixin, NumericOutputFieldMixin, Aggregate):
    function: str
    name: str
    allow_distinct: bool

class Count(Aggregate):
    function: str
    name: str
    output_field: Incomplete
    allow_distinct: bool
    empty_result_set_value: int
    def __init__(self, expression, filter: Incomplete | None = None, **extra) -> None: ...

class Max(Aggregate):
    function: str
    name: str

class Min(Aggregate):
    function: str
    name: str

class StdDev(NumericOutputFieldMixin, Aggregate):
    name: str
    function: Incomplete
    def __init__(self, expression, sample: bool = False, **extra) -> None: ...

class Sum(FixDurationInputMixin, Aggregate):
    function: str
    name: str
    allow_distinct: bool

class Variance(NumericOutputFieldMixin, Aggregate):
    name: str
    function: Incomplete
    def __init__(self, expression, sample: bool = False, **extra) -> None: ...
