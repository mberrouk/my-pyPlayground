from .utils import get_view_name as get_view_name
from _typeshed import Incomplete
from django.apps import apps as apps
from django.contrib import admin as admin
from django.contrib.admin.views.decorators import staff_member_required as staff_member_required
from django.contrib.admindocs import utils as utils
from django.contrib.admindocs.utils import remove_non_capturing_groups as remove_non_capturing_groups, replace_metacharacters as replace_metacharacters, replace_named_groups as replace_named_groups, replace_unnamed_groups as replace_unnamed_groups
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured, ViewDoesNotExist as ViewDoesNotExist
from django.db import models as models
from django.http import Http404 as Http404
from django.template.engine import Engine as Engine
from django.urls import get_mod_func as get_mod_func, get_resolver as get_resolver, get_urlconf as get_urlconf
from django.utils._os import safe_join as safe_join
from django.utils.decorators import method_decorator as method_decorator
from django.utils.functional import cached_property as cached_property
from django.utils.inspect import func_accepts_kwargs as func_accepts_kwargs, func_accepts_var_args as func_accepts_var_args, get_func_full_args as get_func_full_args, method_has_no_args as method_has_no_args
from django.views.generic import TemplateView as TemplateView

MODEL_METHODS_EXCLUDE: Incomplete

class BaseAdminDocsView(TemplateView):
    template_name: str
    def dispatch(self, request, *args, **kwargs): ...
    def get_context_data(self, **kwargs): ...

class BookmarkletsView(BaseAdminDocsView):
    template_name: str

class TemplateTagIndexView(BaseAdminDocsView):
    template_name: str
    def get_context_data(self, **kwargs): ...

class TemplateFilterIndexView(BaseAdminDocsView):
    template_name: str
    def get_context_data(self, **kwargs): ...

class ViewIndexView(BaseAdminDocsView):
    template_name: str
    def get_context_data(self, **kwargs): ...

class ViewDetailView(BaseAdminDocsView):
    template_name: str
    def get_context_data(self, **kwargs): ...

class ModelIndexView(BaseAdminDocsView):
    template_name: str
    def get_context_data(self, **kwargs): ...

class ModelDetailView(BaseAdminDocsView):
    template_name: str
    def get_context_data(self, **kwargs): ...

class TemplateDetailView(BaseAdminDocsView):
    template_name: str
    def get_context_data(self, **kwargs): ...

def get_return_data_type(func_name): ...
def get_readable_field_data_type(field): ...
def extract_views_from_urlpatterns(urlpatterns, base: str = '', namespace: Incomplete | None = None): ...
def simplify_regex(pattern): ...
