"""
This type stub file was generated by pyright.
"""

from django.core.exceptions import ImproperlyConfigured

"Base Cache class."
class InvalidCacheBackendError(ImproperlyConfigured):
    ...


class CacheKeyWarning(RuntimeWarning):
    ...


class InvalidCacheKey(ValueError):
    ...


DEFAULT_TIMEOUT = ...
MEMCACHE_MAX_KEY_LENGTH = ...
def default_key_func(key, key_prefix, version): # -> LiteralString:
    """
    Default function to generate keys.

    Construct the key used by all other methods. By default, prepend
    the `key_prefix`. KEY_FUNCTION can be used to specify an alternate
    function with custom key making behavior.
    """
    ...

def get_key_func(key_func): # -> Callable[..., object] | Any | Callable[..., LiteralString]:
    """
    Function to decide which key function to use.

    Default to ``default_key_func``.
    """
    ...

class BaseCache:
    _missing_key = ...
    def __init__(self, params) -> None:
        ...
    
    def get_backend_timeout(self, timeout=...): # -> float | None:
        """
        Return the timeout value usable by this backend based upon the provided
        timeout.
        """
        ...
    
    def make_key(self, key, version=...): # -> LiteralString | object | Any:
        """
        Construct the key used by all other methods. By default, use the
        key_func to generate a key (which, by default, prepends the
        `key_prefix' and 'version'). A different key function can be provided
        at the time of cache construction; alternatively, you can subclass the
        cache backend to provide custom key making behavior.
        """
        ...
    
    def validate_key(self, key): # -> None:
        """
        Warn about keys that would not be portable to the memcached
        backend. This encourages (but does not force) writing backend-portable
        cache code.
        """
        ...
    
    def make_and_validate_key(self, key, version=...): # -> LiteralString | object | Any:
        """Helper to make and validate keys."""
        ...
    
    def add(self, key, value, timeout=..., version=...):
        """
        Set a value in the cache if the key does not already exist. If
        timeout is given, use that timeout for the key; otherwise use the
        default cache timeout.

        Return True if the value was stored, False otherwise.
        """
        ...
    
    async def aadd(self, key, value, timeout=..., version=...):
        ...
    
    def get(self, key, default=..., version=...):
        """
        Fetch a given key from the cache. If the key does not exist, return
        default, which itself defaults to None.
        """
        ...
    
    async def aget(self, key, default=..., version=...):
        ...
    
    def set(self, key, value, timeout=..., version=...):
        """
        Set a value in the cache. If timeout is given, use that timeout for the
        key; otherwise use the default cache timeout.
        """
        ...
    
    async def aset(self, key, value, timeout=..., version=...):
        ...
    
    def touch(self, key, timeout=..., version=...):
        """
        Update the key's expiry time using timeout. Return True if successful
        or False if the key does not exist.
        """
        ...
    
    async def atouch(self, key, timeout=..., version=...):
        ...
    
    def delete(self, key, version=...):
        """
        Delete a key from the cache and return whether it succeeded, failing
        silently.
        """
        ...
    
    async def adelete(self, key, version=...):
        ...
    
    def get_many(self, keys, version=...): # -> dict[Any, Any]:
        """
        Fetch a bunch of keys from the cache. For certain backends (memcached,
        pgsql) this can be *much* faster when fetching multiple values.

        Return a dict mapping each key in keys to its value. If the given
        key is missing, it will be missing from the response dict.
        """
        ...
    
    async def aget_many(self, keys, version=...): # -> dict[Any, Any]:
        """See get_many()."""
        ...
    
    def get_or_set(self, key, default, timeout=..., version=...):
        """
        Fetch a given key from the cache. If the key does not exist,
        add the key and set it to the default value. The default value can
        also be any callable. If timeout is given, use that timeout for the
        key; otherwise use the default cache timeout.

        Return the value of the key stored or retrieved.
        """
        ...
    
    async def aget_or_set(self, key, default, timeout=..., version=...):
        """See get_or_set()."""
        ...
    
    def has_key(self, key, version=...): # -> bool:
        """
        Return True if the key is in the cache and has not expired.
        """
        ...
    
    async def ahas_key(self, key, version=...): # -> bool:
        ...
    
    def incr(self, key, delta=..., version=...):
        """
        Add delta to value in the cache. If the key does not exist, raise a
        ValueError exception.
        """
        ...
    
    async def aincr(self, key, delta=..., version=...):
        """See incr()."""
        ...
    
    def decr(self, key, delta=..., version=...):
        """
        Subtract delta from value in the cache. If the key does not exist, raise
        a ValueError exception.
        """
        ...
    
    async def adecr(self, key, delta=..., version=...):
        ...
    
    def __contains__(self, key): # -> bool:
        """
        Return True if the key is in the cache and has not expired.
        """
        ...
    
    def set_many(self, data, timeout=..., version=...): # -> list[Any]:
        """
        Set a bunch of values in the cache at once from a dict of key/value
        pairs.  For certain backends (memcached), this is much more efficient
        than calling set() multiple times.

        If timeout is given, use that timeout for the key; otherwise use the
        default cache timeout.

        On backends that support it, return a list of keys that failed
        insertion, or an empty list if all keys were inserted successfully.
        """
        ...
    
    async def aset_many(self, data, timeout=..., version=...): # -> list[Any]:
        ...
    
    def delete_many(self, keys, version=...): # -> None:
        """
        Delete a bunch of values in the cache at once. For certain backends
        (memcached), this is much more efficient than calling delete() multiple
        times.
        """
        ...
    
    async def adelete_many(self, keys, version=...): # -> None:
        ...
    
    def clear(self):
        """Remove *all* values from the cache at once."""
        ...
    
    async def aclear(self):
        ...
    
    def incr_version(self, key, delta=..., version=...):
        """
        Add delta to the cache version for the supplied key. Return the new
        version.
        """
        ...
    
    async def aincr_version(self, key, delta=..., version=...):
        """See incr_version()."""
        ...
    
    def decr_version(self, key, delta=..., version=...):
        """
        Subtract delta from the cache version for the supplied key. Return the
        new version.
        """
        ...
    
    async def adecr_version(self, key, delta=..., version=...):
        ...
    
    def close(self, **kwargs): # -> None:
        """Close the cache connection"""
        ...
    
    async def aclose(self, **kwargs): # -> None:
        ...
    


memcached_error_chars_re = ...
def memcache_key_warnings(key): # -> Generator[str, Any, None]:
    ...

