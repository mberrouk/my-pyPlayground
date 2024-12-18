from .utils import get_view_name as get_view_name
from django.conf import settings as settings
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.http import HttpResponse as HttpResponse
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin

class XViewMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs): ...
