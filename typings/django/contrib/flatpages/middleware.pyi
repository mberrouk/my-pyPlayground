from django.conf import settings as settings
from django.contrib.flatpages.views import flatpage as flatpage
from django.http import Http404 as Http404
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin

class FlatpageFallbackMiddleware(MiddlewareMixin):
    def process_response(self, request, response): ...
