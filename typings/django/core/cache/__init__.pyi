from _typeshed import Incomplete
from django.core.cache.backends.base import BaseCache as BaseCache, CacheKeyWarning as CacheKeyWarning, InvalidCacheBackendError as InvalidCacheBackendError, InvalidCacheKey as InvalidCacheKey
from django.utils.connection import BaseConnectionHandler

__all__ = ['cache', 'caches', 'DEFAULT_CACHE_ALIAS', 'InvalidCacheBackendError', 'CacheKeyWarning', 'BaseCache', 'InvalidCacheKey']

DEFAULT_CACHE_ALIAS: str

class CacheHandler(BaseConnectionHandler):
    settings_name: str
    exception_class = InvalidCacheBackendError
    def create_connection(self, alias): ...

caches: Incomplete
cache: Incomplete
