from django.conf import settings as settings
from django.contrib import auth as auth
from django.contrib.auth import REDIRECT_FIELD_NAME as REDIRECT_FIELD_NAME, load_backend as load_backend
from django.contrib.auth.backends import RemoteUserBackend as RemoteUserBackend
from django.contrib.auth.views import redirect_to_login as redirect_to_login
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.shortcuts import resolve_url as resolve_url
from django.utils.deprecation import MiddlewareMixin as MiddlewareMixin
from django.utils.functional import SimpleLazyObject as SimpleLazyObject

def get_user(request): ...
async def auser(request): ...

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request): ...

class LoginRequiredMiddleware(MiddlewareMixin):
    redirect_field_name = REDIRECT_FIELD_NAME
    def process_view(self, request, view_func, view_args, view_kwargs): ...
    def get_login_url(self, view_func): ...
    def get_redirect_field_name(self, view_func): ...
    def handle_no_permission(self, request, view_func): ...

class RemoteUserMiddleware(MiddlewareMixin):
    header: str
    force_logout_if_no_header: bool
    def process_request(self, request) -> None: ...
    def clean_username(self, username, request): ...

class PersistentRemoteUserMiddleware(RemoteUserMiddleware):
    force_logout_if_no_header: bool
