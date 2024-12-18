from .shortcuts import get_current_site as get_current_site
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin

class CurrentSiteMiddleware(MiddlewareMixin):
    def process_request(self, request) -> None: ...
