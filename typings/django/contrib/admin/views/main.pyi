from _typeshed import Incomplete
from django import forms as forms
from django.conf import settings as settings
from django.contrib import messages as messages
from django.contrib.admin import FieldListFilter as FieldListFilter
from django.contrib.admin.exceptions import DisallowedModelAdminLookup as DisallowedModelAdminLookup, DisallowedModelAdminToField as DisallowedModelAdminToField
from django.contrib.admin.options import IS_FACETS_VAR as IS_FACETS_VAR, IS_POPUP_VAR as IS_POPUP_VAR, IncorrectLookupParameters as IncorrectLookupParameters, ShowFacets as ShowFacets, TO_FIELD_VAR as TO_FIELD_VAR
from django.contrib.admin.utils import build_q_object_from_lookup_parameters as build_q_object_from_lookup_parameters, get_fields_from_path as get_fields_from_path, lookup_spawns_duplicates as lookup_spawns_duplicates, prepare_lookup_value as prepare_lookup_value, quote as quote
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist, ImproperlyConfigured as ImproperlyConfigured, SuspiciousOperation as SuspiciousOperation
from django.core.paginator import InvalidPage as InvalidPage
from django.db.models import F as F, Field as Field, ManyToOneRel as ManyToOneRel, OrderBy as OrderBy
from django.db.models.constants import LOOKUP_SEP as LOOKUP_SEP
from django.db.models.expressions import Combinable as Combinable
from django.urls import reverse as reverse
from django.utils.deprecation import RemovedInDjango60Warning as RemovedInDjango60Warning
from django.utils.http import urlencode as urlencode
from django.utils.inspect import func_supports_parameter as func_supports_parameter
from django.utils.timezone import make_aware as make_aware
from django.utils.translation import gettext as gettext

ALL_VAR: str
ORDER_VAR: str
PAGE_VAR: str
SEARCH_VAR: str
ERROR_FLAG: str
IGNORED_PARAMS: Incomplete

class ChangeListSearchForm(forms.Form):
    fields: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class ChangeList:
    search_form_class = ChangeListSearchForm
    model: Incomplete
    opts: Incomplete
    lookup_opts: Incomplete
    root_queryset: Incomplete
    list_display: Incomplete
    list_display_links: Incomplete
    list_filter: Incomplete
    has_filters: Incomplete
    has_active_filters: Incomplete
    clear_all_filters_qs: Incomplete
    date_hierarchy: Incomplete
    search_fields: Incomplete
    list_select_related: Incomplete
    list_per_page: Incomplete
    list_max_show_all: Incomplete
    model_admin: Incomplete
    preserved_filters: Incomplete
    sortable_by: Incomplete
    search_help_text: Incomplete
    query: Incomplete
    page_num: Incomplete
    show_all: Incomplete
    is_popup: Incomplete
    add_facets: Incomplete
    is_facets_optional: Incomplete
    to_field: Incomplete
    params: Incomplete
    filter_params: Incomplete
    remove_facet_link: Incomplete
    add_facet_link: Incomplete
    list_editable: Incomplete
    queryset: Incomplete
    title: Incomplete
    pk_attname: Incomplete
    def __init__(self, request, model, list_display, list_display_links, list_filter, date_hierarchy, search_fields, list_select_related, list_per_page, list_max_show_all, list_editable, model_admin, sortable_by, search_help_text) -> None: ...
    def get_filters_params(self, params: Incomplete | None = None): ...
    def get_filters(self, request): ...
    def get_query_string(self, new_params: Incomplete | None = None, remove: Incomplete | None = None): ...
    result_count: Incomplete
    show_full_result_count: Incomplete
    show_admin_actions: Incomplete
    full_result_count: Incomplete
    result_list: Incomplete
    can_show_all: Incomplete
    multi_page: Incomplete
    paginator: Incomplete
    def get_results(self, request) -> None: ...
    def get_ordering_field(self, field_name): ...
    def get_ordering(self, request, queryset): ...
    def get_ordering_field_columns(self): ...
    def get_queryset(self, request, exclude_parameters: Incomplete | None = None): ...
    def apply_select_related(self, qs): ...
    def has_related_field_in_list_display(self): ...
    def url_for_result(self, result): ...
