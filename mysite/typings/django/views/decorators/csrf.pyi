"""
This type stub file was generated by pyright.
"""

from django.middleware.csrf import CsrfViewMiddleware

csrf_protect = ...
class _EnsureCsrfToken(CsrfViewMiddleware):
    ...


requires_csrf_token = ...
class _EnsureCsrfCookie(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs): # -> object | None:
        ...
    


ensure_csrf_cookie = ...
def csrf_exempt(view_func): # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Coroutine[Any, Any, Any]]:
    """Mark a view function as being exempt from the CSRF view protection."""
    ...
