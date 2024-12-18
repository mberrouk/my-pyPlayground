from django.conf import settings as settings
from django.conf.urls.i18n import is_language_prefix_patterns_used as is_language_prefix_patterns_used
from django.http import HttpResponseRedirect as HttpResponseRedirect
from django.urls import get_script_prefix as get_script_prefix, is_valid_path as is_valid_path
from django.utils import translation as translation
from django.utils.cache import patch_vary_headers as patch_vary_headers
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin

class LocaleMiddleware(MiddlewareMixin):
    response_redirect_class = HttpResponseRedirect
    def process_request(self, request) -> None: ...
    def process_response(self, request, response): ...
