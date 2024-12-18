from .converters import get_converters as get_converters
from .exceptions import NoReverseMatch as NoReverseMatch, Resolver404 as Resolver404
from .utils import get_callable as get_callable
from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.checks import Error as Error, Warning as Warning
from django.core.checks.urls import check_resolver as check_resolver
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.utils.datastructures import MultiValueDict as MultiValueDict
from django.utils.functional import cached_property as cached_property
from django.utils.http import RFC3986_SUBDELIMS as RFC3986_SUBDELIMS, escape_leading_slashes as escape_leading_slashes
from django.utils.regex_helper import normalize as normalize
from django.utils.translation import get_language as get_language

class ResolverMatch:
    func: Incomplete
    args: Incomplete
    kwargs: Incomplete
    url_name: Incomplete
    route: Incomplete
    tried: Incomplete
    captured_kwargs: Incomplete
    extra_kwargs: Incomplete
    app_names: Incomplete
    app_name: Incomplete
    namespaces: Incomplete
    namespace: Incomplete
    view_name: Incomplete
    def __init__(self, func, args, kwargs, url_name: Incomplete | None = None, app_names: Incomplete | None = None, namespaces: Incomplete | None = None, route: Incomplete | None = None, tried: Incomplete | None = None, captured_kwargs: Incomplete | None = None, extra_kwargs: Incomplete | None = None) -> None: ...
    def __getitem__(self, index): ...
    def __reduce_ex__(self, protocol) -> None: ...

def get_resolver(urlconf: Incomplete | None = None): ...
def get_ns_resolver(ns_pattern, resolver, converters): ...

class LocaleRegexDescriptor:
    def __get__(self, instance, cls: Incomplete | None = None): ...

class CheckURLMixin:
    def describe(self): ...

class RegexPattern(CheckURLMixin):
    regex: Incomplete
    name: Incomplete
    converters: Incomplete
    def __init__(self, regex, name: Incomplete | None = None, is_endpoint: bool = False) -> None: ...
    def match(self, path): ...
    def check(self): ...

whitespace_set: Incomplete

class LocaleRegexRouteDescriptor:
    def __get__(self, instance, cls: Incomplete | None = None): ...

class RoutePattern(CheckURLMixin):
    regex: Incomplete
    name: Incomplete
    def __init__(self, route, name: Incomplete | None = None, is_endpoint: bool = False) -> None: ...
    def match(self, path): ...
    def check(self): ...

class LocalePrefixPattern:
    prefix_default_language: Incomplete
    converters: Incomplete
    def __init__(self, prefix_default_language: bool = True) -> None: ...
    @property
    def regex(self): ...
    @property
    def language_prefix(self): ...
    def match(self, path): ...
    def check(self): ...
    def describe(self): ...

class URLPattern:
    pattern: Incomplete
    callback: Incomplete
    default_args: Incomplete
    name: Incomplete
    def __init__(self, pattern, callback, default_args: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def check(self): ...
    def resolve(self, path): ...
    def lookup_str(self): ...

class URLResolver:
    pattern: Incomplete
    urlconf_name: Incomplete
    callback: Incomplete
    default_kwargs: Incomplete
    namespace: Incomplete
    app_name: Incomplete
    def __init__(self, pattern, urlconf_name, default_kwargs: Incomplete | None = None, app_name: Incomplete | None = None, namespace: Incomplete | None = None) -> None: ...
    def check(self): ...
    @property
    def reverse_dict(self): ...
    @property
    def namespace_dict(self): ...
    @property
    def app_dict(self): ...
    def resolve(self, path): ...
    def urlconf_module(self): ...
    def url_patterns(self): ...
    def resolve_error_handler(self, view_type): ...
    def reverse(self, lookup_view, *args, **kwargs): ...
