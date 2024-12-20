from _typeshed import Incomplete
from django.apps import apps as apps
from django.conf import settings as settings
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist, ImproperlyConfigured as ImproperlyConfigured
from django.core.signals import setting_changed as setting_changed
from django.db import connections as connections
from django.db.models import AutoField as AutoField, Manager as Manager, OrderWrt as OrderWrt, UniqueConstraint as UniqueConstraint
from django.db.models.query_utils import PathInfo as PathInfo
from django.utils.datastructures import ImmutableList as ImmutableList, OrderedSet as OrderedSet
from django.utils.functional import cached_property as cached_property
from django.utils.module_loading import import_string as import_string
from django.utils.text import camel_case_to_spaces as camel_case_to_spaces, format_lazy as format_lazy
from django.utils.translation import override as override

PROXY_PARENTS: Incomplete
EMPTY_RELATION_TREE: Incomplete
IMMUTABLE_WARNING: str
DEFAULT_NAMES: Incomplete

def normalize_together(option_together): ...
def make_immutable_fields_list(name, data): ...

class Options:
    FORWARD_PROPERTIES: Incomplete
    REVERSE_PROPERTIES: Incomplete
    default_apps = apps
    local_fields: Incomplete
    local_many_to_many: Incomplete
    private_fields: Incomplete
    local_managers: Incomplete
    base_manager_name: Incomplete
    default_manager_name: Incomplete
    model_name: Incomplete
    verbose_name: Incomplete
    verbose_name_plural: Incomplete
    db_table: str
    db_table_comment: str
    ordering: Incomplete
    indexes: Incomplete
    constraints: Incomplete
    unique_together: Incomplete
    select_on_save: bool
    default_permissions: Incomplete
    permissions: Incomplete
    object_name: Incomplete
    app_label: Incomplete
    get_latest_by: Incomplete
    order_with_respect_to: Incomplete
    db_tablespace: Incomplete
    required_db_features: Incomplete
    required_db_vendor: Incomplete
    meta: Incomplete
    pk: Incomplete
    auto_field: Incomplete
    abstract: bool
    managed: bool
    proxy: bool
    proxy_for_model: Incomplete
    concrete_model: Incomplete
    swappable: Incomplete
    parents: Incomplete
    auto_created: bool
    related_fkey_lookups: Incomplete
    apps: Incomplete
    default_related_name: Incomplete
    def __init__(self, meta, app_label: Incomplete | None = None) -> None: ...
    @property
    def label(self): ...
    @property
    def label_lower(self): ...
    @property
    def app_config(self): ...
    model: Incomplete
    original_attrs: Incomplete
    def contribute_to_class(self, cls, name) -> None: ...
    def add_manager(self, manager) -> None: ...
    def add_field(self, field, private: bool = False) -> None: ...
    def setup_pk(self, field) -> None: ...
    def setup_proxy(self, target) -> None: ...
    def can_migrate(self, connection): ...
    def verbose_name_raw(self): ...
    def swapped(self): ...
    def setting_changed(self, *, setting, **kwargs) -> None: ...
    def managers(self): ...
    def managers_map(self): ...
    def base_manager(self): ...
    def default_manager(self): ...
    def fields(self): ...
    def concrete_fields(self): ...
    def local_concrete_fields(self): ...
    def many_to_many(self): ...
    def related_objects(self): ...
    def fields_map(self): ...
    def get_field(self, field_name): ...
    def get_base_chain(self, model): ...
    def all_parents(self): ...
    def get_parent_list(self): ...
    def get_ancestor_link(self, ancestor): ...
    def get_path_to_parent(self, parent): ...
    def get_path_from_parent(self, parent): ...
    def get_fields(self, include_parents: bool = True, include_hidden: bool = False): ...
    def total_unique_constraints(self): ...
    def db_returning_fields(self): ...
