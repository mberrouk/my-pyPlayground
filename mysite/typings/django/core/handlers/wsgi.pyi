"""
This type stub file was generated by pyright.
"""

from io import IOBase
from django.core.handlers import base
from django.http import HttpRequest
from django.utils.functional import cached_property

"""
This type stub file was generated by pyright.
"""
_slashes_re = ...
class LimitedStream(IOBase):
    """
    Wrap another stream to disallow reading it past a number of bytes.

    Based on the implementation from werkzeug.wsgi.LimitedStream
    See https://github.com/pallets/werkzeug/blob/dbf78f67/src/werkzeug/wsgi.py#L828
    """
    def __init__(self, stream, limit) -> None:
        ...
    
    def read(self, size=..., /):
        ...
    
    def readline(self, size=..., /):
        ...
    


class WSGIRequest(HttpRequest):
    def __init__(self, environ) -> None:
        ...
    
    @cached_property
    def GET(self):
        ...
    
    @cached_property
    def COOKIES(self):
        ...
    
    @property
    def FILES(self):
        ...
    
    POST = ...


class WSGIHandler(base.BaseHandler):
    request_class = WSGIRequest
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __call__(self, environ, start_response):
        ...
    


def get_path_info(environ):
    """Return the HTTP request's PATH_INFO as a string."""
    ...

def get_script_name(environ):
    """
    Return the equivalent of the HTTP request's SCRIPT_NAME environment
    variable. If Apache mod_rewrite is used, return what would have been
    the script name prior to any rewriting (so it's the script name as seen
    from the client's perspective), unless the FORCE_SCRIPT_NAME setting is
    set (to anything).
    """
    ...

def get_bytes_from_wsgi(environ, key, default):
    """
    Get a value from the WSGI environ dictionary as bytes.

    key and default should be strings.
    """
    ...

def get_str_from_wsgi(environ, key, default):
    """
    Get a value from the WSGI environ dictionary as str.

    key and default should be str objects.
    """
    ...
