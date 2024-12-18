from _typeshed import Incomplete
from django.utils.cache import patch_vary_headers as patch_vary_headers
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin
from django.utils.text import compress_sequence as compress_sequence, compress_string as compress_string

re_accepts_gzip: Incomplete

class GZipMiddleware(MiddlewareMixin):
    max_random_bytes: int
    def process_response(self, request, response): ...
