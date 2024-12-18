from . import Field
from .mixins import CheckFieldDefaultMixin
from _typeshed import Incomplete
from django.db.models import lookups
from django.db.models.lookups import FieldGetDbPrepValueMixin, PostgresOperatorLookup, Transform

__all__ = ['JSONField']

class JSONField(CheckFieldDefaultMixin, Field):
    empty_strings_allowed: bool
    description: Incomplete
    default_error_messages: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, encoder: Incomplete | None = None, decoder: Incomplete | None = None, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def from_db_value(self, value, expression, connection): ...
    def get_internal_type(self): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def get_db_prep_save(self, value, connection): ...
    def get_transform(self, name): ...
    def validate(self, value, model_instance) -> None: ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class DataContains(FieldGetDbPrepValueMixin, PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str
    def as_sql(self, compiler, connection): ...

class ContainedBy(FieldGetDbPrepValueMixin, PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str
    def as_sql(self, compiler, connection): ...

class HasKeyLookup(PostgresOperatorLookup):
    logical_operator: Incomplete
    def compile_json_path_final_key(self, key_transform): ...
    def as_sql(self, compiler, connection, template: Incomplete | None = None): ...
    def as_mysql(self, compiler, connection): ...
    def as_oracle(self, compiler, connection): ...
    lhs: Incomplete
    rhs: Incomplete
    def as_postgresql(self, compiler, connection): ...
    def as_sqlite(self, compiler, connection): ...

class HasKey(HasKeyLookup):
    lookup_name: str
    postgres_operator: str
    prepare_rhs: bool

class HasKeys(HasKeyLookup):
    lookup_name: str
    postgres_operator: str
    logical_operator: str
    def get_prep_lookup(self): ...

class HasAnyKeys(HasKeys):
    lookup_name: str
    postgres_operator: str
    logical_operator: str

class HasKeyOrArrayIndex(HasKey):
    def compile_json_path_final_key(self, key_transform): ...

class CaseInsensitiveMixin:
    def process_lhs(self, compiler, connection): ...
    def process_rhs(self, compiler, connection): ...

class JSONExact(lookups.Exact):
    can_use_none_as_rhs: bool
    def process_rhs(self, compiler, connection): ...
    def as_oracle(self, compiler, connection): ...

class JSONIContains(CaseInsensitiveMixin, lookups.IContains): ...

class KeyTransform(Transform):
    postgres_operator: str
    postgres_nested_operator: str
    key_name: Incomplete
    def __init__(self, key_name, *args, **kwargs) -> None: ...
    def preprocess_lhs(self, compiler, connection): ...
    def as_mysql(self, compiler, connection): ...
    def as_oracle(self, compiler, connection): ...
    def as_postgresql(self, compiler, connection): ...
    def as_sqlite(self, compiler, connection): ...

class KeyTextTransform(KeyTransform):
    postgres_operator: str
    postgres_nested_operator: str
    output_field: Incomplete
    def as_mysql(self, compiler, connection): ...
    @classmethod
    def from_lookup(cls, lookup): ...

class KeyTransformTextLookupMixin:
    def __init__(self, key_transform, *args, **kwargs) -> None: ...

class KeyTransformIsNull(lookups.IsNull):
    def as_oracle(self, compiler, connection): ...
    def as_sqlite(self, compiler, connection): ...

class KeyTransformIn(lookups.In):
    def resolve_expression_parameter(self, compiler, connection, sql, param): ...

class KeyTransformExact(JSONExact):
    def process_rhs(self, compiler, connection): ...
    def as_oracle(self, compiler, connection): ...

class KeyTransformIExact(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IExact): ...
class KeyTransformIContains(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IContains): ...
class KeyTransformStartsWith(KeyTransformTextLookupMixin, lookups.StartsWith): ...
class KeyTransformIStartsWith(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IStartsWith): ...
class KeyTransformEndsWith(KeyTransformTextLookupMixin, lookups.EndsWith): ...
class KeyTransformIEndsWith(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IEndsWith): ...
class KeyTransformRegex(KeyTransformTextLookupMixin, lookups.Regex): ...
class KeyTransformIRegex(CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IRegex): ...

class KeyTransformNumericLookupMixin:
    def process_rhs(self, compiler, connection): ...

class KeyTransformLt(KeyTransformNumericLookupMixin, lookups.LessThan): ...
class KeyTransformLte(KeyTransformNumericLookupMixin, lookups.LessThanOrEqual): ...
class KeyTransformGt(KeyTransformNumericLookupMixin, lookups.GreaterThan): ...
class KeyTransformGte(KeyTransformNumericLookupMixin, lookups.GreaterThanOrEqual): ...

class KeyTransformFactory:
    key_name: Incomplete
    def __init__(self, key_name) -> None: ...
    def __call__(self, *args, **kwargs): ...