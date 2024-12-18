from django.utils.cache import cc_delim_re as cc_delim_re, get_conditional_response as get_conditional_response, set_response_etag as set_response_etag
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin
from django.utils.http import parse_http_date_safe as parse_http_date_safe

class ConditionalGetMiddleware(MiddlewareMixin):
    def process_response(self, request, response): ...
    def needs_etag(self, response): ...
