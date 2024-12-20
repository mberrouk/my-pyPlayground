"""
This type stub file was generated by pyright.
"""

from django.core.exceptions import EmptyResultSet, FullResultSet
from django.db.models.expressions import Expression, Func
from django.db.models.fields import Field, IntegerField, UUIDField
from django.db.models.query_utils import RegisterLookupMixin
from django.utils.functional import cached_property

class Lookup(Expression):
    lookup_name = ...
    prepare_rhs = ...
    can_use_none_as_rhs = ...
    def __init__(self, lhs, rhs) -> None:
        ...
    
    def apply_bilateral_transforms(self, value):
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def batch_process_rhs(self, compiler, connection, rhs=...): # -> tuple[list[str], list[Any]]:
        ...
    
    def get_source_expressions(self): # -> list[Any | Value] | list[Any]:
        ...
    
    def set_source_expressions(self, new_exprs): # -> None:
        ...
    
    def get_prep_lookup(self): # -> Any | Value:
        ...
    
    def get_prep_lhs(self): # -> Any | Value:
        ...
    
    def get_db_prep_lookup(self, value, connection): # -> tuple[Literal['%s'], list[Any]]:
        ...
    
    def process_lhs(self, compiler, connection, lhs=...): # -> tuple[str | Any, Any]:
        ...
    
    def process_rhs(self, compiler, connection): # -> tuple[Any, Any] | tuple[Literal['%s'], list[Any]]:
        ...
    
    def rhs_is_direct_value(self): # -> bool:
        ...
    
    def get_group_by_cols(self): # -> list[Any]:
        ...
    
    def as_oracle(self, compiler, connection):
        ...
    
    @cached_property
    def output_field(self): # -> BooleanField:
        ...
    
    @property
    def identity(self): # -> tuple[type[Self], Any | Value, Any]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def resolve_expression(self, query=..., allow_joins=..., reuse=..., summarize=..., for_save=...): # -> Self:
        ...
    
    def select_format(self, compiler, sql, params): # -> tuple[str | Any, Any]:
        ...
    
    @cached_property
    def allowed_default(self): # -> Literal[False]:
        ...
    


class Transform(RegisterLookupMixin, Func):
    """
    RegisterLookupMixin() is first so that get_lookup() and get_transform()
    first examine self and then check output_field.
    """
    bilateral = ...
    arity = ...
    @property
    def lhs(self): # -> F | Value:
        ...
    
    def get_bilateral_transforms(self): # -> list[Any]:
        ...
    


class BuiltinLookup(Lookup):
    def process_lhs(self, compiler, connection, lhs=...): # -> tuple[Any, list[Any]]:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[LiteralString, list[Any]]:
        ...
    
    def get_rhs_op(self, connection, rhs):
        ...
    


class FieldGetDbPrepValueMixin:
    """
    Some lookups require Field.get_db_prep_value() to be called on their
    inputs.
    """
    get_db_prep_lookup_value_is_iterable = ...
    def get_db_prep_lookup(self, value, connection): # -> tuple[Literal['%s'], list[Any]]:
        ...
    


class FieldGetDbPrepValueIterableMixin(FieldGetDbPrepValueMixin):
    """
    Some lookups require Field.get_db_prep_value() to be called on each value
    in an iterable.
    """
    get_db_prep_lookup_value_is_iterable = ...
    def get_prep_lookup(self): # -> list[Any]:
        ...
    
    def process_rhs(self, compiler, connection): # -> tuple[Any, tuple[Any, ...]]:
        ...
    
    def resolve_expression_parameter(self, compiler, connection, sql, param): # -> tuple[Any, Any | list[Any]]:
        ...
    
    def batch_process_rhs(self, compiler, connection, rhs=...): # -> tuple[Any, tuple[Any, ...]]:
        ...
    


class PostgresOperatorLookup(Lookup):
    """Lookup defined by operators on PostgreSQL."""
    postgres_operator = ...
    def as_postgresql(self, compiler, connection): # -> tuple[str, tuple[Any, ...]]:
        ...
    


@Field.register_lookup
class Exact(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name = ...
    def get_prep_lookup(self): # -> Any | Value:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[Any, list[Any]] | tuple[LiteralString, list[Any]]:
        ...
    


@Field.register_lookup
class IExact(BuiltinLookup):
    lookup_name = ...
    prepare_rhs = ...
    def process_rhs(self, qn, connection): # -> tuple[Any | Literal['%s'], Any | list[Any]]:
        ...
    


@Field.register_lookup
class GreaterThan(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name = ...


@Field.register_lookup
class GreaterThanOrEqual(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name = ...


@Field.register_lookup
class LessThan(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name = ...


@Field.register_lookup
class LessThanOrEqual(FieldGetDbPrepValueMixin, BuiltinLookup):
    lookup_name = ...


class IntegerFieldOverflow:
    underflow_exception = EmptyResultSet
    overflow_exception = EmptyResultSet
    def process_rhs(self, compiler, connection):
        ...
    


class IntegerFieldFloatRounding:
    """
    Allow floats to work as query values for IntegerField. Without this, the
    decimal portion of the float would always be discarded.
    """
    def get_prep_lookup(self):
        ...
    


@IntegerField.register_lookup
class IntegerFieldExact(IntegerFieldOverflow, Exact):
    ...


@IntegerField.register_lookup
class IntegerGreaterThan(IntegerFieldOverflow, GreaterThan):
    underflow_exception = FullResultSet


@IntegerField.register_lookup
class IntegerGreaterThanOrEqual(IntegerFieldOverflow, IntegerFieldFloatRounding, GreaterThanOrEqual):
    underflow_exception = FullResultSet


@IntegerField.register_lookup
class IntegerLessThan(IntegerFieldOverflow, IntegerFieldFloatRounding, LessThan):
    overflow_exception = FullResultSet


@IntegerField.register_lookup
class IntegerLessThanOrEqual(IntegerFieldOverflow, LessThanOrEqual):
    overflow_exception = FullResultSet


@Field.register_lookup
class In(FieldGetDbPrepValueIterableMixin, BuiltinLookup):
    lookup_name = ...
    def get_refs(self): # -> set[Any] | Any:
        ...
    
    def get_prep_lookup(self): # -> list[Any]:
        ...
    
    def process_rhs(self, compiler, connection): # -> tuple[str, tuple[Any, ...]] | tuple[Any, tuple[Any, ...]]:
        ...
    
    def get_rhs_op(self, connection, rhs):
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[str, list[Any]] | tuple[LiteralString, list[Any]]:
        ...
    
    def split_parameter_list_as_sql(self, compiler, connection): # -> tuple[str, list[Any]]:
        ...
    


class PatternLookup(BuiltinLookup):
    param_pattern = ...
    prepare_rhs = ...
    def get_rhs_op(self, connection, rhs):
        ...
    
    def process_rhs(self, qn, connection): # -> tuple[Any | Literal['%s'], Any | list[Any]]:
        ...
    


@Field.register_lookup
class Contains(PatternLookup):
    lookup_name = ...


@Field.register_lookup
class IContains(Contains):
    lookup_name = ...


@Field.register_lookup
class StartsWith(PatternLookup):
    lookup_name = ...
    param_pattern = ...


@Field.register_lookup
class IStartsWith(StartsWith):
    lookup_name = ...


@Field.register_lookup
class EndsWith(PatternLookup):
    lookup_name = ...
    param_pattern = ...


@Field.register_lookup
class IEndsWith(EndsWith):
    lookup_name = ...


@Field.register_lookup
class Range(FieldGetDbPrepValueIterableMixin, BuiltinLookup):
    lookup_name = ...
    def get_rhs_op(self, connection, rhs): # -> LiteralString:
        ...
    


@Field.register_lookup
class IsNull(BuiltinLookup):
    lookup_name = ...
    prepare_rhs = ...
    def as_sql(self, compiler, connection): # -> tuple[Any, list[Any]]:
        ...
    


@Field.register_lookup
class Regex(BuiltinLookup):
    lookup_name = ...
    prepare_rhs = ...
    def as_sql(self, compiler, connection): # -> tuple[LiteralString, list[Any]] | tuple[Any, Any | list[Any]]:
        ...
    


@Field.register_lookup
class IRegex(Regex):
    lookup_name = ...


class YearLookup(Lookup):
    def year_lookup_bounds(self, connection, year):
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[str, Any]:
        ...
    
    def get_direct_rhs_sql(self, connection, rhs):
        ...
    
    def get_bound_params(self, start, finish):
        ...
    


class YearExact(YearLookup, Exact):
    def get_direct_rhs_sql(self, connection, rhs): # -> Literal['BETWEEN %s AND %s']:
        ...
    
    def get_bound_params(self, start, finish): # -> tuple[Any, Any]:
        ...
    


class YearGt(YearLookup, GreaterThan):
    def get_bound_params(self, start, finish): # -> tuple[Any]:
        ...
    


class YearGte(YearLookup, GreaterThanOrEqual):
    def get_bound_params(self, start, finish): # -> tuple[Any]:
        ...
    


class YearLt(YearLookup, LessThan):
    def get_bound_params(self, start, finish): # -> tuple[Any]:
        ...
    


class YearLte(YearLookup, LessThanOrEqual):
    def get_bound_params(self, start, finish): # -> tuple[Any]:
        ...
    


class UUIDTextMixin:
    """
    Strip hyphens from a value when filtering a UUIDField on backends without
    a native datatype for UUID.
    """
    def process_rhs(self, qn, connection): # -> tuple[Any, Any]:
        ...
    


@UUIDField.register_lookup
class UUIDIExact(UUIDTextMixin, IExact):
    ...


@UUIDField.register_lookup
class UUIDContains(UUIDTextMixin, Contains):
    ...


@UUIDField.register_lookup
class UUIDIContains(UUIDTextMixin, IContains):
    ...


@UUIDField.register_lookup
class UUIDStartsWith(UUIDTextMixin, StartsWith):
    ...


@UUIDField.register_lookup
class UUIDIStartsWith(UUIDTextMixin, IStartsWith):
    ...


@UUIDField.register_lookup
class UUIDEndsWith(UUIDTextMixin, EndsWith):
    ...


@UUIDField.register_lookup
class UUIDIEndsWith(UUIDTextMixin, IEndsWith):
    ...


