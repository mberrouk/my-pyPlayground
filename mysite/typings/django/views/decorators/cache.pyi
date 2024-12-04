"""
This type stub file was generated by pyright.
"""

def cache_page(timeout, *, cache=..., key_prefix=...): # -> Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Coroutine[Any, Any, Any]]]:
    """
    Decorator for views that tries getting the page from the cache and
    populates the cache if the page isn't in the cache yet.

    The cache is keyed by the URL and some data from the headers.
    Additionally there is the key prefix that is used to distinguish different
    cache areas in a multi-site setup. You could use the
    get_current_site().domain, for example, as that is unique across a Django
    project.

    Additionally, all headers from the response's Vary header will be taken
    into account on caching -- just like the middleware does.
    """
    ...

def cache_control(**kwargs): # -> Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Coroutine[Any, Any, Any]]]:
    ...

def never_cache(view_func): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Coroutine[Any, Any, Any]]:
    """
    Decorator that adds headers to a response so that it will never be cached.
    """
    ...

