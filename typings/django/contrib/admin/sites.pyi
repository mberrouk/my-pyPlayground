from _typeshed import Incomplete
from django.apps import apps as apps
from django.conf import settings as settings
from django.contrib.admin import ModelAdmin as ModelAdmin, actions as actions
from django.contrib.admin.exceptions import AlreadyRegistered as AlreadyRegistered, NotRegistered as NotRegistered
from django.contrib.admin.views.autocomplete import AutocompleteJsonView as AutocompleteJsonView
from django.contrib.auth import REDIRECT_FIELD_NAME as REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_not_required as login_not_required
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.db.models.base import ModelBase as ModelBase
from django.http import Http404 as Http404, HttpResponsePermanentRedirect as HttpResponsePermanentRedirect, HttpResponseRedirect as HttpResponseRedirect
from django.template.response import TemplateResponse as TemplateResponse
from django.urls import NoReverseMatch as NoReverseMatch, Resolver404 as Resolver404, resolve as resolve, reverse as reverse, reverse_lazy as reverse_lazy
from django.utils.decorators import method_decorator as method_decorator
from django.utils.functional import LazyObject as LazyObject
from django.utils.module_loading import import_string as import_string
from django.utils.text import capfirst as capfirst
from django.utils.translation import gettext_lazy as gettext_lazy
from django.views.decorators.cache import never_cache as never_cache
from django.views.decorators.common import no_append_slash as no_append_slash
from django.views.decorators.csrf import csrf_protect as csrf_protect
from django.views.i18n import JavaScriptCatalog as JavaScriptCatalog

all_sites: Incomplete

class AdminSite:
    site_title: Incomplete
    site_header: Incomplete
    index_title: Incomplete
    site_url: str
    enable_nav_sidebar: bool
    empty_value_display: str
    login_form: Incomplete
    index_template: Incomplete
    app_index_template: Incomplete
    login_template: Incomplete
    logout_template: Incomplete
    password_change_template: Incomplete
    password_change_done_template: Incomplete
    final_catch_all_view: bool
    name: Incomplete
    def __init__(self, name: str = 'admin') -> None: ...
    def check(self, app_configs): ...
    def register(self, model_or_iterable, admin_class: Incomplete | None = None, **options) -> None: ...
    def unregister(self, model_or_iterable) -> None: ...
    def is_registered(self, model): ...
    def get_model_admin(self, model): ...
    def add_action(self, action, name: Incomplete | None = None) -> None: ...
    def disable_action(self, name) -> None: ...
    def get_action(self, name): ...
    @property
    def actions(self): ...
    def has_permission(self, request): ...
    def admin_view(self, view, cacheable: bool = False): ...
    def get_urls(self): ...
    @property
    def urls(self): ...
    def each_context(self, request): ...
    def password_change(self, request, extra_context: Incomplete | None = None): ...
    def password_change_done(self, request, extra_context: Incomplete | None = None): ...
    def i18n_javascript(self, request, extra_context: Incomplete | None = None): ...
    def logout(self, request, extra_context: Incomplete | None = None): ...
    def login(self, request, extra_context: Incomplete | None = None): ...
    def autocomplete_view(self, request): ...
    def catch_all_view(self, request, url): ...
    def get_app_list(self, request, app_label: Incomplete | None = None): ...
    def index(self, request, extra_context: Incomplete | None = None): ...
    def app_index(self, request, app_label, extra_context: Incomplete | None = None): ...
    def get_log_entries(self, request): ...

class DefaultAdminSite(LazyObject): ...

site: Incomplete
