from _typeshed import Incomplete
from collections.abc import Generator
from django.contrib.admin.exceptions import NotRegistered as NotRegistered
from django.contrib.admin.options import IncorrectLookupParameters as IncorrectLookupParameters
from django.contrib.admin.utils import build_q_object_from_lookup_parameters as build_q_object_from_lookup_parameters, get_last_value_from_parameters as get_last_value_from_parameters, get_model_from_relation as get_model_from_relation, prepare_lookup_value as prepare_lookup_value, reverse_field_path as reverse_field_path
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured, ValidationError as ValidationError
from django.db import models as models
from django.utils import timezone as timezone

class ListFilter:
    title: Incomplete
    template: str
    request: Incomplete
    used_parameters: Incomplete
    def __init__(self, request, params, model, model_admin) -> None: ...
    def has_output(self) -> None: ...
    def choices(self, changelist) -> None: ...
    def queryset(self, request, queryset) -> None: ...
    def expected_parameters(self) -> None: ...

class FacetsMixin:
    def get_facet_counts(self, pk_attname, filtered_qs) -> None: ...
    def get_facet_queryset(self, changelist): ...

class SimpleListFilter(FacetsMixin, ListFilter):
    parameter_name: Incomplete
    lookup_choices: Incomplete
    def __init__(self, request, params, model, model_admin) -> None: ...
    def has_output(self): ...
    def value(self): ...
    def lookups(self, request, model_admin) -> None: ...
    def expected_parameters(self): ...
    def get_facet_counts(self, pk_attname, filtered_qs): ...
    def choices(self, changelist) -> Generator[Incomplete]: ...

class FieldListFilter(FacetsMixin, ListFilter):
    list_separator: str
    field: Incomplete
    field_path: Incomplete
    title: Incomplete
    def __init__(self, field, request, params, model, model_admin, field_path) -> None: ...
    def has_output(self): ...
    def queryset(self, request, queryset): ...
    @classmethod
    def register(cls, test, list_filter_class, take_priority: bool = False) -> None: ...
    @classmethod
    def create(cls, field, request, params, model, model_admin, field_path): ...

class RelatedFieldListFilter(FieldListFilter):
    lookup_kwarg: Incomplete
    lookup_kwarg_isnull: Incomplete
    lookup_val: Incomplete
    lookup_val_isnull: Incomplete
    lookup_choices: Incomplete
    lookup_title: Incomplete
    title: Incomplete
    empty_value_display: Incomplete
    def __init__(self, field, request, params, model, model_admin, field_path) -> None: ...
    @property
    def include_empty_choice(self): ...
    def has_output(self): ...
    def expected_parameters(self): ...
    def field_admin_ordering(self, field, request, model_admin): ...
    def field_choices(self, field, request, model_admin): ...
    def get_facet_counts(self, pk_attname, filtered_qs): ...
    def choices(self, changelist) -> Generator[Incomplete]: ...

class BooleanFieldListFilter(FieldListFilter):
    lookup_kwarg: Incomplete
    lookup_kwarg2: Incomplete
    lookup_val: Incomplete
    lookup_val2: Incomplete
    def __init__(self, field, request, params, model, model_admin, field_path) -> None: ...
    def expected_parameters(self): ...
    def get_facet_counts(self, pk_attname, filtered_qs): ...
    def choices(self, changelist) -> Generator[Incomplete]: ...

class ChoicesFieldListFilter(FieldListFilter):
    lookup_kwarg: Incomplete
    lookup_kwarg_isnull: Incomplete
    lookup_val: Incomplete
    lookup_val_isnull: Incomplete
    def __init__(self, field, request, params, model, model_admin, field_path) -> None: ...
    def expected_parameters(self): ...
    def get_facet_counts(self, pk_attname, filtered_qs): ...
    def choices(self, changelist) -> Generator[Incomplete]: ...

class DateFieldListFilter(FieldListFilter):
    field_generic: Incomplete
    date_params: Incomplete
    lookup_kwarg_since: Incomplete
    lookup_kwarg_until: Incomplete
    links: Incomplete
    lookup_kwarg_isnull: Incomplete
    def __init__(self, field, request, params, model, model_admin, field_path) -> None: ...
    def expected_parameters(self): ...
    def get_facet_counts(self, pk_attname, filtered_qs): ...
    def choices(self, changelist) -> Generator[Incomplete]: ...

class AllValuesFieldListFilter(FieldListFilter):
    lookup_kwarg: Incomplete
    lookup_kwarg_isnull: Incomplete
    lookup_val: Incomplete
    lookup_val_isnull: Incomplete
    empty_value_display: Incomplete
    lookup_choices: Incomplete
    def __init__(self, field, request, params, model, model_admin, field_path) -> None: ...
    def expected_parameters(self): ...
    def get_facet_counts(self, pk_attname, filtered_qs): ...
    def choices(self, changelist) -> Generator[Incomplete]: ...

class RelatedOnlyFieldListFilter(RelatedFieldListFilter):
    def field_choices(self, field, request, model_admin): ...

class EmptyFieldListFilter(FieldListFilter):
    lookup_kwarg: Incomplete
    lookup_val: Incomplete
    def __init__(self, field, request, params, model, model_admin, field_path) -> None: ...
    def get_lookup_condition(self): ...
    def queryset(self, request, queryset): ...
    def expected_parameters(self): ...
    def get_facet_counts(self, pk_attname, filtered_qs): ...
    def choices(self, changelist) -> Generator[Incomplete]: ...
