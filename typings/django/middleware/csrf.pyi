from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.exceptions import DisallowedHost as DisallowedHost, ImproperlyConfigured as ImproperlyConfigured
from django.http import HttpHeaders as HttpHeaders, UnreadablePostError as UnreadablePostError
from django.urls import get_callable as get_callable
from django.utils.cache import patch_vary_headers as patch_vary_headers
from django.utils.crypto import constant_time_compare as constant_time_compare, get_random_string as get_random_string
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin
from django.utils.functional import cached_property as cached_property
from django.utils.http import is_same_domain as is_same_domain
from django.utils.log import log_response as log_response

logger: Incomplete
invalid_token_chars_re: Incomplete
REASON_BAD_ORIGIN: str
REASON_NO_REFERER: str
REASON_BAD_REFERER: str
REASON_NO_CSRF_COOKIE: str
REASON_CSRF_TOKEN_MISSING: str
REASON_MALFORMED_REFERER: str
REASON_INSECURE_REFERER: str
REASON_INCORRECT_LENGTH: str
REASON_INVALID_CHARACTERS: str
CSRF_SECRET_LENGTH: int
CSRF_TOKEN_LENGTH: Incomplete
CSRF_ALLOWED_CHARS: Incomplete
CSRF_SESSION_KEY: str

def get_token(request): ...
def rotate_token(request) -> None: ...

class InvalidTokenFormat(Exception):
    reason: Incomplete
    def __init__(self, reason) -> None: ...

class RejectRequest(Exception):
    reason: Incomplete
    def __init__(self, reason) -> None: ...

class CsrfViewMiddleware(MiddlewareMixin):
    def csrf_trusted_origins_hosts(self): ...
    def allowed_origins_exact(self): ...
    def allowed_origin_subdomains(self): ...
    def process_request(self, request) -> None: ...
    def process_view(self, request, callback, callback_args, callback_kwargs): ...
    def process_response(self, request, response): ...
