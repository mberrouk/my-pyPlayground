from _typeshed import Incomplete
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.core.validators import EMPTY_VALUES as EMPTY_VALUES
from django.db import models as models, router as router
from django.db.models.constants import LOOKUP_SEP as LOOKUP_SEP
from django.db.models.deletion import Collector as Collector
from django.forms.utils import pretty_name as pretty_name
from django.urls import NoReverseMatch as NoReverseMatch, reverse as reverse
from django.utils import formats as formats, timezone as timezone
from django.utils.hashable import make_hashable as make_hashable
from django.utils.html import format_html as format_html
from django.utils.text import capfirst as capfirst
from django.utils.translation import ngettext as ngettext

QUOTE_MAP: Incomplete
UNQUOTE_MAP: Incomplete
UNQUOTE_RE: Incomplete

class FieldIsAForeignKeyColumnName(Exception): ...

def lookup_spawns_duplicates(opts, lookup_path): ...
def get_last_value_from_parameters(parameters, key): ...
def prepare_lookup_value(key, value, separator: str = ','): ...
def build_q_object_from_lookup_parameters(parameters): ...
def quote(s): ...
def unquote(s): ...
def flatten(fields): ...
def flatten_fieldsets(fieldsets): ...
def get_deleted_objects(objs, request, admin_site): ...

class NestedObjects(Collector):
    edges: Incomplete
    protected: Incomplete
    model_objs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def add_edge(self, source, target) -> None: ...
    def collect(self, objs, source: Incomplete | None = None, source_attr: Incomplete | None = None, **kwargs): ...
    def related_objects(self, related_model, related_fields, objs): ...
    def nested(self, format_callback: Incomplete | None = None): ...
    def can_fast_delete(self, *args, **kwargs): ...

def model_format_dict(obj): ...
def model_ngettext(obj, n: Incomplete | None = None): ...
def lookup_field(name, obj, model_admin: Incomplete | None = None): ...
def label_for_field(name, model, model_admin: Incomplete | None = None, return_attr: bool = False, form: Incomplete | None = None): ...
def help_text_for_field(name, model): ...
def display_for_field(value, field, empty_value_display): ...
def display_for_value(value, empty_value_display, boolean: bool = False): ...

class NotRelationField(Exception): ...

def get_model_from_relation(field): ...
def reverse_field_path(model, path): ...
def get_fields_from_path(model, path): ...
def construct_change_message(form, formsets, add): ...
