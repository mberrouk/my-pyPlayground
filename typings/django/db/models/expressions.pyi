from _typeshed import Incomplete
from collections.abc import Generator
from django.core.exceptions import EmptyResultSet as EmptyResultSet, FieldError as FieldError, FullResultSet as FullResultSet
from django.db import DatabaseError as DatabaseError, NotSupportedError as NotSupportedError, connection as connection
from django.db.models import fields as fields
from django.db.models.constants import LOOKUP_SEP as LOOKUP_SEP
from django.db.models.query_utils import Q as Q
from django.utils.deconstruct import deconstructible as deconstructible
from django.utils.functional import cached_property as cached_property, classproperty as classproperty
from django.utils.hashable import make_hashable as make_hashable
from enum import Enum

class SQLiteNumericMixin:
    def as_sqlite(self, compiler, connection, **extra_context): ...

class Combinable:
    ADD: str
    SUB: str
    MUL: str
    DIV: str
    POW: str
    MOD: str
    BITAND: str
    BITOR: str
    BITLEFTSHIFT: str
    BITRIGHTSHIFT: str
    BITXOR: str
    def __neg__(self): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __mod__(self, other): ...
    def __pow__(self, other): ...
    def __and__(self, other): ...
    def bitand(self, other): ...
    def bitleftshift(self, other): ...
    def bitrightshift(self, other): ...
    def __xor__(self, other): ...
    def bitxor(self, other): ...
    def __or__(self, other): ...
    def bitor(self, other): ...
    def __radd__(self, other): ...
    def __rsub__(self, other): ...
    def __rmul__(self, other): ...
    def __rtruediv__(self, other): ...
    def __rmod__(self, other): ...
    def __rpow__(self, other): ...
    def __rand__(self, other) -> None: ...
    def __ror__(self, other) -> None: ...
    def __rxor__(self, other) -> None: ...
    def __invert__(self): ...

class BaseExpression:
    empty_result_set_value = NotImplemented
    is_summary: bool
    filterable: bool
    window_compatible: bool
    allowed_default: bool
    constraint_validation_compatible: bool
    def __init__(self, output_field: Incomplete | None = None) -> None: ...
    def get_db_converters(self, connection): ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def as_sql(self, compiler, connection) -> None: ...
    def contains_aggregate(self): ...
    def contains_over_clause(self): ...
    def contains_column_references(self): ...
    def contains_subquery(self): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    @property
    def conditional(self): ...
    @property
    def field(self): ...
    def output_field(self): ...
    def convert_value(self): ...
    def get_lookup(self, lookup): ...
    def get_transform(self, name): ...
    def relabeled_clone(self, change_map): ...
    def replace_expressions(self, replacements): ...
    def get_refs(self): ...
    def copy(self): ...
    def prefix_references(self, prefix): ...
    def get_group_by_cols(self): ...
    def get_source_fields(self): ...
    def asc(self, **kwargs): ...
    def desc(self, **kwargs): ...
    def reverse_ordering(self): ...
    def flatten(self) -> Generator[Incomplete, Incomplete]: ...
    def select_format(self, compiler, sql, params): ...
    def get_expression_for_validation(self): ...

class Expression(BaseExpression, Combinable):
    def identity(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

def register_combinable_fields(lhs, connector, rhs, result) -> None: ...

class CombinedExpression(SQLiteNumericMixin, Expression):
    connector: Incomplete
    lhs: Incomplete
    rhs: Incomplete
    def __init__(self, lhs, connector, rhs, output_field: Incomplete | None = None) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def allowed_default(self): ...

class DurationExpression(CombinedExpression):
    def compile(self, side, compiler, connection): ...
    def as_sql(self, compiler, connection): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...

class TemporalSubtraction(CombinedExpression):
    output_field: Incomplete
    def __init__(self, lhs, rhs) -> None: ...
    def as_sql(self, compiler, connection): ...

class F(Combinable):
    allowed_default: bool
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __getitem__(self, subscript): ...
    def __contains__(self, other) -> bool: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def replace_expressions(self, replacements): ...
    def asc(self, **kwargs): ...
    def desc(self, **kwargs): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def copy(self): ...

class ResolvedOuterRef(F):
    contains_aggregate: bool
    contains_over_clause: bool
    def as_sql(self, *args, **kwargs) -> None: ...
    def resolve_expression(self, *args, **kwargs): ...
    def relabeled_clone(self, relabels): ...
    def get_group_by_cols(self): ...

class OuterRef(F):
    contains_aggregate: bool
    contains_over_clause: bool
    def resolve_expression(self, *args, **kwargs): ...
    def relabeled_clone(self, relabels): ...

class Sliced(F):
    obj: Incomplete
    start: Incomplete
    length: int
    def __init__(self, obj, subscript) -> None: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...

class Func(SQLiteNumericMixin, Expression):
    function: Incomplete
    template: str
    arg_joiner: str
    arity: Incomplete
    source_expressions: Incomplete
    extra: Incomplete
    def __init__(self, *expressions, output_field: Incomplete | None = None, **extra) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def as_sql(self, compiler, connection, function: Incomplete | None = None, template: Incomplete | None = None, arg_joiner: Incomplete | None = None, **extra_context): ...
    def copy(self): ...
    def allowed_default(self): ...

class Value(SQLiteNumericMixin, Expression):
    for_save: bool
    allowed_default: bool
    value: Incomplete
    def __init__(self, value, output_field: Incomplete | None = None) -> None: ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def get_group_by_cols(self): ...
    @property
    def empty_result_set_value(self): ...

class RawSQL(Expression):
    allowed_default: bool
    def __init__(self, sql, params, output_field: Incomplete | None = None) -> None: ...
    def as_sql(self, compiler, connection): ...
    def get_group_by_cols(self): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...

class Star(Expression):
    def as_sql(self, compiler, connection): ...

class DatabaseDefault(Expression):
    expression: Incomplete
    def __init__(self, expression, output_field: Incomplete | None = None) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def as_sql(self, compiler, connection): ...

class Col(Expression):
    contains_column_references: bool
    possibly_multivalued: bool
    def __init__(self, alias, target, output_field: Incomplete | None = None) -> None: ...
    def as_sql(self, compiler, connection): ...
    def relabeled_clone(self, relabels): ...
    def get_group_by_cols(self): ...
    def get_db_converters(self, connection): ...

class Ref(Expression):
    def __init__(self, refs, source) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def get_refs(self): ...
    def relabeled_clone(self, relabels): ...
    def as_sql(self, compiler, connection): ...
    def get_group_by_cols(self): ...

class ExpressionList(Func):
    template: str
    def as_sql(self, *args, **kwargs): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...
    def get_group_by_cols(self): ...

class OrderByList(ExpressionList):
    allowed_default: bool
    template: str
    def __init__(self, *expressions, **extra) -> None: ...

class ExpressionWrapper(SQLiteNumericMixin, Expression):
    expression: Incomplete
    def __init__(self, expression, output_field) -> None: ...
    def set_source_expressions(self, exprs) -> None: ...
    def get_source_expressions(self): ...
    def get_group_by_cols(self): ...
    def as_sql(self, compiler, connection): ...
    @property
    def allowed_default(self): ...

class NegatedExpression(ExpressionWrapper):
    def __init__(self, expression) -> None: ...
    def __invert__(self): ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def select_format(self, compiler, sql, params): ...

class When(Expression):
    template: str
    conditional: bool
    condition: Incomplete
    result: Incomplete
    def __init__(self, condition: Incomplete | None = None, then: Incomplete | None = None, **lookups) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def get_source_fields(self): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def as_sql(self, compiler, connection, template: Incomplete | None = None, **extra_context): ...
    def get_group_by_cols(self): ...
    def allowed_default(self): ...

class Case(SQLiteNumericMixin, Expression):
    template: str
    case_joiner: str
    cases: Incomplete
    default: Incomplete
    extra: Incomplete
    def __init__(self, *cases, default: Incomplete | None = None, output_field: Incomplete | None = None, **extra) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def copy(self): ...
    def as_sql(self, compiler, connection, template: Incomplete | None = None, case_joiner: Incomplete | None = None, **extra_context): ...
    def get_group_by_cols(self): ...
    def allowed_default(self): ...

class Subquery(BaseExpression, Combinable):
    template: str
    contains_aggregate: bool
    empty_result_set_value: Incomplete
    subquery: bool
    query: Incomplete
    extra: Incomplete
    def __init__(self, queryset, output_field: Incomplete | None = None, **extra) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def copy(self): ...
    @property
    def external_aliases(self): ...
    def get_external_cols(self): ...
    def as_sql(self, compiler, connection, template: Incomplete | None = None, **extra_context): ...
    def get_group_by_cols(self): ...

class Exists(Subquery):
    template: str
    output_field: Incomplete
    empty_result_set_value: bool
    query: Incomplete
    def __init__(self, queryset, **kwargs) -> None: ...
    def select_format(self, compiler, sql, params): ...
    def as_sql(self, compiler, *args, **kwargs): ...

class OrderBy(Expression):
    template: str
    conditional: bool
    constraint_validation_compatible: bool
    nulls_first: Incomplete
    nulls_last: Incomplete
    descending: Incomplete
    expression: Incomplete
    def __init__(self, expression, descending: bool = False, nulls_first: Incomplete | None = None, nulls_last: Incomplete | None = None) -> None: ...
    def set_source_expressions(self, exprs) -> None: ...
    def get_source_expressions(self): ...
    def as_sql(self, compiler, connection, template: Incomplete | None = None, **extra_context): ...
    def as_oracle(self, compiler, connection): ...
    def get_group_by_cols(self): ...
    def reverse_ordering(self): ...
    def asc(self) -> None: ...
    def desc(self) -> None: ...

class Window(SQLiteNumericMixin, Expression):
    template: str
    contains_aggregate: bool
    contains_over_clause: bool
    partition_by: Incomplete
    order_by: Incomplete
    frame: Incomplete
    source_expression: Incomplete
    def __init__(self, expression, partition_by: Incomplete | None = None, order_by: Incomplete | None = None, frame: Incomplete | None = None, output_field: Incomplete | None = None) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def as_sql(self, compiler, connection, template: Incomplete | None = None): ...
    def as_sqlite(self, compiler, connection): ...
    def get_group_by_cols(self): ...

class WindowFrameExclusion(Enum):
    CURRENT_ROW = 'CURRENT ROW'
    GROUP = 'GROUP'
    TIES = 'TIES'
    NO_OTHERS = 'NO OTHERS'

class WindowFrame(Expression):
    template: str
    start: Incomplete
    end: Incomplete
    exclusion: Incomplete
    def __init__(self, start: Incomplete | None = None, end: Incomplete | None = None, exclusion: Incomplete | None = None) -> None: ...
    def set_source_expressions(self, exprs) -> None: ...
    def get_source_expressions(self): ...
    def get_exclusion(self): ...
    def as_sql(self, compiler, connection): ...
    def get_group_by_cols(self): ...
    def window_frame_start_end(self, connection, start, end) -> None: ...

class RowRange(WindowFrame):
    frame_type: str
    def window_frame_start_end(self, connection, start, end): ...

class ValueRange(WindowFrame):
    frame_type: str
    def window_frame_start_end(self, connection, start, end): ...