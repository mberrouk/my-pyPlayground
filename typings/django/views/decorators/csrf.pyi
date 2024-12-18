from _typeshed import Incomplete
from django.middleware.csrf import CsrfViewMiddleware as CsrfViewMiddleware, get_token as get_token
from django.utils.decorators import decorator_from_middleware as decorator_from_middleware

csrf_protect: Incomplete

class _EnsureCsrfToken(CsrfViewMiddleware): ...

requires_csrf_token: Incomplete

class _EnsureCsrfCookie(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs): ...

ensure_csrf_cookie: Incomplete

def csrf_exempt(view_func): ...
