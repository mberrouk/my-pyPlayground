from . import Field as Field
from .mixins import FieldCacheMixin as FieldCacheMixin
from .related_descriptors import ForeignKeyDeferredAttribute as ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor as ForwardManyToOneDescriptor, ForwardOneToOneDescriptor as ForwardOneToOneDescriptor, ManyToManyDescriptor as ManyToManyDescriptor, ReverseManyToOneDescriptor as ReverseManyToOneDescriptor, ReverseOneToOneDescriptor as ReverseOneToOneDescriptor
from .related_lookups import RelatedExact as RelatedExact, RelatedGreaterThan as RelatedGreaterThan, RelatedGreaterThanOrEqual as RelatedGreaterThanOrEqual, RelatedIn as RelatedIn, RelatedIsNull as RelatedIsNull, RelatedLessThan as RelatedLessThan, RelatedLessThanOrEqual as RelatedLessThanOrEqual
from .reverse_related import ForeignObjectRel as ForeignObjectRel, ManyToManyRel as ManyToManyRel, ManyToOneRel as ManyToOneRel, OneToOneRel as OneToOneRel
from _typeshed import Incomplete
from django import forms as forms
from django.apps import apps as apps
from django.conf import SettingsReference as SettingsReference, settings as settings
from django.core import checks as checks, exceptions as exceptions
from django.db import connection as connection, router as router
from django.db.backends import utils as utils
from django.db.models import Q as Q
from django.db.models.constants import LOOKUP_SEP as LOOKUP_SEP
from django.db.models.deletion import CASCADE as CASCADE, SET_DEFAULT as SET_DEFAULT, SET_NULL as SET_NULL
from django.db.models.query_utils import PathInfo as PathInfo
from django.db.models.utils import make_model_tuple as make_model_tuple
from django.utils.deprecation import RemovedInDjango60Warning as RemovedInDjango60Warning
from django.utils.functional import cached_property as cached_property

RECURSIVE_RELATIONSHIP_CONSTANT: str

def resolve_relation(scope_model, relation): ...
def lazy_related_operation(function, model, *related_models, **kwargs): ...

class RelatedField(FieldCacheMixin, Field):
    one_to_many: bool
    one_to_one: bool
    many_to_many: bool
    many_to_one: bool
    def __init__(self, related_name: Incomplete | None = None, related_query_name: Incomplete | None = None, limit_choices_to: Incomplete | None = None, **kwargs) -> None: ...
    def related_model(self): ...
    def check(self, **kwargs): ...
    def db_type(self, connection) -> None: ...
    opts: Incomplete
    def contribute_to_class(self, cls, name, private_only: bool = False, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_forward_related_filter(self, obj): ...
    def get_reverse_related_filter(self, obj): ...
    @property
    def swappable_setting(self): ...
    name: Incomplete
    verbose_name: Incomplete
    def set_attributes_from_rel(self) -> None: ...
    def do_related_class(self, other, cls) -> None: ...
    def get_limit_choices_to(self): ...
    def formfield(self, **kwargs): ...
    def related_query_name(self): ...
    @property
    def target_field(self): ...
    def cache_name(self): ...

class ForeignObject(RelatedField):
    many_to_many: bool
    many_to_one: bool
    one_to_many: bool
    one_to_one: bool
    requires_unique_target: bool
    related_accessor_class = ReverseManyToOneDescriptor
    forward_related_accessor_class = ForwardManyToOneDescriptor
    rel_class = ForeignObjectRel
    from_fields: Incomplete
    to_fields: Incomplete
    swappable: Incomplete
    def __init__(self, to, on_delete, from_fields, to_fields, rel: Incomplete | None = None, related_name: Incomplete | None = None, related_query_name: Incomplete | None = None, limit_choices_to: Incomplete | None = None, parent_link: bool = False, swappable: bool = True, **kwargs) -> None: ...
    def __copy__(self): ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def resolve_related_fields(self): ...
    def related_fields(self): ...
    def reverse_related_fields(self): ...
    def local_related_fields(self): ...
    def foreign_related_fields(self): ...
    def get_local_related_value(self, instance): ...
    def get_foreign_related_value(self, instance): ...
    @staticmethod
    def get_instance_value_for_fields(instance, fields): ...
    def get_attname_column(self): ...
    def get_joining_columns(self, reverse_join: bool = False): ...
    def get_reverse_joining_columns(self): ...
    def get_joining_fields(self, reverse_join: bool = False): ...
    def get_reverse_joining_fields(self): ...
    def get_extra_descriptor_filter(self, instance): ...
    def get_extra_restriction(self, alias, related_alias) -> None: ...
    def get_path_info(self, filtered_relation: Incomplete | None = None): ...
    def path_infos(self): ...
    def get_reverse_path_info(self, filtered_relation: Incomplete | None = None): ...
    def reverse_path_infos(self): ...
    @classmethod
    def get_class_lookups(cls): ...
    def contribute_to_class(self, cls, name, private_only: bool = False, **kwargs) -> None: ...
    def contribute_to_related_class(self, cls, related) -> None: ...

class ForeignKey(ForeignObject):
    descriptor_class = ForeignKeyDeferredAttribute
    many_to_many: bool
    many_to_one: bool
    one_to_many: bool
    one_to_one: bool
    rel_class = ManyToOneRel
    empty_strings_allowed: bool
    default_error_messages: Incomplete
    description: Incomplete
    db_constraint: Incomplete
    def __init__(self, to, on_delete, related_name: Incomplete | None = None, related_query_name: Incomplete | None = None, limit_choices_to: Incomplete | None = None, parent_link: bool = False, to_field: Incomplete | None = None, db_constraint: bool = True, **kwargs) -> None: ...
    def __class_getitem__(cls, *args, **kwargs): ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def to_python(self, value): ...
    @property
    def target_field(self): ...
    def validate(self, value, model_instance) -> None: ...
    def resolve_related_fields(self): ...
    def get_attname(self): ...
    def get_attname_column(self): ...
    def get_default(self): ...
    def get_db_prep_save(self, value, connection): ...
    def get_db_prep_value(self, value, connection, prepared: bool = False): ...
    def get_prep_value(self, value): ...
    def contribute_to_related_class(self, cls, related) -> None: ...
    def formfield(self, *, using: Incomplete | None = None, **kwargs): ...
    def db_check(self, connection) -> None: ...
    def db_type(self, connection): ...
    def cast_db_type(self, connection): ...
    def db_parameters(self, connection): ...
    def convert_empty_strings(self, value, expression, connection): ...
    def get_db_converters(self, connection): ...
    def get_col(self, alias, output_field: Incomplete | None = None): ...

class OneToOneField(ForeignKey):
    many_to_many: bool
    many_to_one: bool
    one_to_many: bool
    one_to_one: bool
    related_accessor_class = ReverseOneToOneDescriptor
    forward_related_accessor_class = ForwardOneToOneDescriptor
    rel_class = OneToOneRel
    description: Incomplete
    def __init__(self, to, on_delete, to_field: Incomplete | None = None, **kwargs) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs): ...
    def save_form_data(self, instance, data) -> None: ...

def create_many_to_many_intermediary_model(field, klass): ...

class ManyToManyField(RelatedField):
    many_to_many: bool
    many_to_one: bool
    one_to_many: bool
    one_to_one: bool
    rel_class = ManyToManyRel
    description: Incomplete
    has_null_arg: Incomplete
    db_table: Incomplete
    swappable: Incomplete
    def __init__(self, to, related_name: Incomplete | None = None, related_query_name: Incomplete | None = None, limit_choices_to: Incomplete | None = None, symmetrical: Incomplete | None = None, through: Incomplete | None = None, through_fields: Incomplete | None = None, db_constraint: bool = True, db_table: Incomplete | None = None, swappable: bool = True, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_path_info(self, filtered_relation: Incomplete | None = None): ...
    def path_infos(self): ...
    def get_reverse_path_info(self, filtered_relation: Incomplete | None = None): ...
    def reverse_path_infos(self): ...
    m2m_db_table: Incomplete
    def contribute_to_class(self, cls, name, **kwargs) -> None: ...
    m2m_column_name: Incomplete
    m2m_reverse_name: Incomplete
    m2m_field_name: Incomplete
    m2m_reverse_field_name: Incomplete
    m2m_target_field_name: Incomplete
    m2m_reverse_target_field_name: Incomplete
    def contribute_to_related_class(self, cls, related): ...
    def set_attributes_from_rel(self) -> None: ...
    def value_from_object(self, obj): ...
    def save_form_data(self, instance, data) -> None: ...
    def formfield(self, *, using: Incomplete | None = None, **kwargs): ...
    def db_check(self, connection) -> None: ...
    def db_type(self, connection) -> None: ...
    def db_parameters(self, connection): ...