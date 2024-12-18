from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.cache import DEFAULT_CACHE_ALIAS as DEFAULT_CACHE_ALIAS, caches as caches
from django.utils.cache import get_cache_key as get_cache_key, get_max_age as get_max_age, has_vary_header as has_vary_header, learn_cache_key as learn_cache_key, patch_response_headers as patch_response_headers
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin
from django.utils.http import parse_http_date_safe as parse_http_date_safe

class UpdateCacheMiddleware(MiddlewareMixin):
    cache_timeout: Incomplete
    page_timeout: Incomplete
    key_prefix: Incomplete
    cache_alias: Incomplete
    def __init__(self, get_response) -> None: ...
    @property
    def cache(self): ...
    def process_response(self, request, response): ...

class FetchFromCacheMiddleware(MiddlewareMixin):
    key_prefix: Incomplete
    cache_alias: Incomplete
    def __init__(self, get_response) -> None: ...
    @property
    def cache(self): ...
    def process_request(self, request): ...

class CacheMiddleware(UpdateCacheMiddleware, FetchFromCacheMiddleware):
    key_prefix: Incomplete
    cache_alias: Incomplete
    cache_timeout: Incomplete
    page_timeout: Incomplete
    def __init__(self, get_response, cache_timeout: Incomplete | None = None, page_timeout: Incomplete | None = None, **kwargs) -> None: ...
