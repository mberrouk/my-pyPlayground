from _typeshed import Incomplete
from django.db.models.query_utils import DeferredAttribute, RegisterLookupMixin

__all__ = ['AutoField', 'BLANK_CHOICE_DASH', 'BigAutoField', 'BigIntegerField', 'BinaryField', 'BooleanField', 'CharField', 'CommaSeparatedIntegerField', 'DateField', 'DateTimeField', 'DecimalField', 'DurationField', 'EmailField', 'Empty', 'Field', 'FilePathField', 'FloatField', 'GenericIPAddressField', 'IPAddressField', 'IntegerField', 'NOT_PROVIDED', 'NullBooleanField', 'PositiveBigIntegerField', 'PositiveIntegerField', 'PositiveSmallIntegerField', 'SlugField', 'SmallAutoField', 'SmallIntegerField', 'TextField', 'TimeField', 'URLField', 'UUIDField']

class Empty: ...
class NOT_PROVIDED: ...

BLANK_CHOICE_DASH: Incomplete

class Field(RegisterLookupMixin):
    empty_strings_allowed: bool
    empty_values: Incomplete
    creation_counter: int
    auto_creation_counter: int
    default_validators: Incomplete
    default_error_messages: Incomplete
    system_check_deprecated_details: Incomplete
    system_check_removed_details: Incomplete
    non_db_attrs: Incomplete
    hidden: bool
    many_to_many: Incomplete
    many_to_one: Incomplete
    one_to_many: Incomplete
    one_to_one: Incomplete
    related_model: Incomplete
    generated: bool
    descriptor_class = DeferredAttribute
    description: Incomplete
    name: Incomplete
    verbose_name: Incomplete
    primary_key: Incomplete
    remote_field: Incomplete
    is_relation: Incomplete
    default: Incomplete
    db_default: Incomplete
    editable: Incomplete
    serialize: Incomplete
    unique_for_date: Incomplete
    unique_for_month: Incomplete
    unique_for_year: Incomplete
    help_text: Incomplete
    db_index: Incomplete
    db_column: Incomplete
    db_comment: Incomplete
    auto_created: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, primary_key: bool = False, max_length: Incomplete | None = None, unique: bool = False, blank: bool = False, null: bool = False, db_index: bool = False, rel: Incomplete | None = None, default=..., editable: bool = True, serialize: bool = True, unique_for_date: Incomplete | None = None, unique_for_month: Incomplete | None = None, unique_for_year: Incomplete | None = None, choices: Incomplete | None = None, help_text: str = '', db_column: Incomplete | None = None, db_tablespace: Incomplete | None = None, auto_created: bool = False, validators=(), error_messages: Incomplete | None = None, db_comment: Incomplete | None = None, db_default=...) -> None: ...
    def check(self, **kwargs): ...
    def get_col(self, alias, output_field: Incomplete | None = None): ...
    @property
    def choices(self): ...
    @choices.setter
    def choices(self, value) -> None: ...
    def cached_col(self): ...
    def select_format(self, compiler, sql, params): ...
    def deconstruct(self): ...
    def clone(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __deepcopy__(self, memodict): ...
    def __copy__(self): ...
    def __reduce__(self): ...
    def get_pk_value_on_save(self, instance): ...
    def to_python(self, value): ...
    def error_messages(self): ...
    def validators(self): ...
    def run_validators(self, value) -> None: ...
    def validate(self, value, model_instance) -> None: ...
    def clean(self, value, model_instance): ...
    def db_type_parameters(self, connection): ...
    def db_check(self, connection): ...
    def db_type(self, connection): ...
    def rel_db_type(self, connection): ...
    def cast_db_type(self, connection): ...
    def db_parameters(self, connection): ...
    def db_type_suffix(self, connection): ...
    def get_db_converters(self, connection): ...
    def unique(self): ...
    @property
    def db_tablespace(self): ...
    @property
    def db_returning(self): ...
    concrete: Incomplete
    def set_attributes_from_name(self, name) -> None: ...
    model: Incomplete
    def contribute_to_class(self, cls, name, private_only: bool = False) -> None: ...
    def get_filter_kwargs_for_object(self, obj): ...
    def get_attname(self): ...
    def get_attname_column(self): ...
    def get_internal_type(self): ...
    def pre_save(self, model_instance, add): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def get_db_prep_save(self, value, connection): ...
    def has_default(self): ...
    def get_default(self): ...
    def get_choices(self, include_blank: bool = True, blank_choice=..., limit_choices_to: Incomplete | None = None, ordering=()): ...
    def value_to_string(self, obj): ...
    @property
    def flatchoices(self): ...
    def save_form_data(self, instance, data) -> None: ...
    def formfield(self, form_class: Incomplete | None = None, choices_form_class: Incomplete | None = None, **kwargs): ...
    def value_from_object(self, obj): ...
    def slice_expression(self, expression, start, length) -> None: ...

class BooleanField(Field):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class CharField(Field):
    db_collation: Incomplete
    def __init__(self, *args, db_collation: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def description(self): ...
    def check(self, **kwargs): ...
    def cast_db_type(self, connection): ...
    def db_parameters(self, connection): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...
    def deconstruct(self): ...
    def slice_expression(self, expression, start, length): ...

class CommaSeparatedIntegerField(CharField):
    default_validators: Incomplete
    description: Incomplete
    system_check_removed_details: Incomplete

class DateTimeCheckMixin:
    def check(self, **kwargs): ...

class DateField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, auto_now: bool = False, auto_now_add: bool = False, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def pre_save(self, model_instance, add): ...
    def contribute_to_class(self, cls, name, **kwargs) -> None: ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class DateTimeField(DateField):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def pre_save(self, model_instance, add): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class DecimalField(Field):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, max_digits: Incomplete | None = None, decimal_places: Incomplete | None = None, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def validators(self): ...
    def context(self): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_db_prep_save(self, value, connection): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class DurationField(Field):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def get_db_converters(self, connection): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class EmailField(CharField):
    default_validators: Incomplete
    description: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs): ...

class FilePathField(Field):
    description: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, path: str = '', match: Incomplete | None = None, recursive: bool = False, allow_files: bool = True, allow_folders: bool = False, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...
    def get_internal_type(self): ...

class FloatField(Field):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def get_prep_value(self, value): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def formfield(self, **kwargs): ...

class IntegerField(Field):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def check(self, **kwargs): ...
    def validators(self): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def formfield(self, **kwargs): ...

class BigIntegerField(IntegerField):
    description: Incomplete
    MAX_BIGINT: int
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class SmallIntegerField(IntegerField):
    description: Incomplete
    def get_internal_type(self): ...

class IPAddressField(Field):
    empty_strings_allowed: bool
    description: Incomplete
    system_check_removed_details: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_prep_value(self, value): ...
    def get_internal_type(self): ...

class GenericIPAddressField(Field):
    empty_strings_allowed: bool
    description: Incomplete
    default_error_messages: Incomplete
    unpack_ipv4: Incomplete
    protocol: Incomplete
    default_validators: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, protocol: str = 'both', unpack_ipv4: bool = False, *args, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class NullBooleanField(BooleanField):
    default_error_messages: Incomplete
    description: Incomplete
    system_check_removed_details: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...

class PositiveIntegerRelDbTypeMixin:
    def __init_subclass__(cls, **kwargs) -> None: ...
    def rel_db_type(self, connection): ...

class PositiveBigIntegerField(PositiveIntegerRelDbTypeMixin, BigIntegerField):
    description: Incomplete
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description: Incomplete
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, SmallIntegerField):
    description: Incomplete
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class SlugField(CharField):
    default_validators: Incomplete
    description: Incomplete
    allow_unicode: Incomplete
    def __init__(self, *args, max_length: int = 50, db_index: bool = True, allow_unicode: bool = False, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class TextField(Field):
    description: Incomplete
    db_collation: Incomplete
    def __init__(self, *args, db_collation: Incomplete | None = None, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def db_parameters(self, connection): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...
    def deconstruct(self): ...
    def slice_expression(self, expression, start, length): ...

class TimeField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, auto_now: bool = False, auto_now_add: bool = False, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def pre_save(self, model_instance, add): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class URLField(CharField):
    default_validators: Incomplete
    description: Incomplete
    def __init__(self, verbose_name: Incomplete | None = None, name: Incomplete | None = None, **kwargs) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs): ...

class BinaryField(Field):
    description: Incomplete
    empty_values: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def get_placeholder(self, value, compiler, connection): ...
    def get_default(self): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def value_to_string(self, obj): ...
    def to_python(self, value): ...

class UUIDField(Field):
    default_error_messages: Incomplete
    description: Incomplete
    empty_strings_allowed: bool
    def __init__(self, verbose_name: Incomplete | None = None, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def to_python(self, value): ...
    def formfield(self, **kwargs): ...

class AutoFieldMixin:
    db_returning: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def validate(self, value, model_instance) -> None: ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def contribute_to_class(self, cls, name, **kwargs) -> None: ...
    def formfield(self, **kwargs) -> None: ...

class AutoFieldMeta(type):
    def __instancecheck__(self, instance): ...
    def __subclasscheck__(self, subclass): ...

class AutoField(AutoFieldMixin, IntegerField, metaclass=AutoFieldMeta):
    def get_internal_type(self): ...
    def rel_db_type(self, connection): ...

class BigAutoField(AutoFieldMixin, BigIntegerField):
    def get_internal_type(self): ...
    def rel_db_type(self, connection): ...

class SmallAutoField(AutoFieldMixin, SmallIntegerField):
    def get_internal_type(self): ...
    def rel_db_type(self, connection): ...