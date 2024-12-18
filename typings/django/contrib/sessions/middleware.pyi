from _typeshed import Incomplete
from django.conf import settings as settings
from django.contrib.sessions.backends.base import UpdateError as UpdateError
from django.contrib.sessions.exceptions import SessionInterrupted as SessionInterrupted
from django.utils.cache import patch_vary_headers as patch_vary_headers
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin
from django.utils.http import http_date as http_date

class SessionMiddleware(MiddlewareMixin):
    SessionStore: Incomplete
    def __init__(self, get_response) -> None: ...
    def process_request(self, request) -> None: ...
    def process_response(self, request, response): ...
