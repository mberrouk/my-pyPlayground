from django.apps import apps as apps
from django.conf import settings as settings
from django.contrib.redirects.models import Redirect as Redirect
from django.contrib.sites.shortcuts import get_current_site as get_current_site
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.http import HttpResponseGone as HttpResponseGone, HttpResponsePermanentRedirect as HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin

class RedirectFallbackMiddleware(MiddlewareMixin):
    response_gone_class = HttpResponseGone
    response_redirect_class = HttpResponsePermanentRedirect
    def __init__(self, get_response) -> None: ...
    def process_response(self, request, response): ...
