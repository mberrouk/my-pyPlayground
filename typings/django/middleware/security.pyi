from _typeshed import Incomplete
from django.conf import settings as settings
from django.http import HttpResponsePermanentRedirect as HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin

class SecurityMiddleware(MiddlewareMixin):
    sts_seconds: Incomplete
    sts_include_subdomains: Incomplete
    sts_preload: Incomplete
    content_type_nosniff: Incomplete
    redirect: Incomplete
    redirect_host: Incomplete
    redirect_exempt: Incomplete
    referrer_policy: Incomplete
    cross_origin_opener_policy: Incomplete
    def __init__(self, get_response) -> None: ...
    def process_request(self, request): ...
    def process_response(self, request, response): ...
