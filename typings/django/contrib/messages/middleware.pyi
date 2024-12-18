from django.conf import settings as settings
from django.contrib.messages.storage import default_storage as default_storage
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin

class MessageMiddleware(MiddlewareMixin):
    def process_request(self, request) -> None: ...
    def process_response(self, request, response): ...
