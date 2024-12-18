from _typeshed import Incomplete
from django.conf import settings as settings
from django.contrib.auth import REDIRECT_FIELD_NAME as REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied as PermissionDenied
from django.shortcuts import resolve_url as resolve_url

def user_passes_test(test_func, login_url: Incomplete | None = None, redirect_field_name=...): ...
def login_required(function: Incomplete | None = None, redirect_field_name=..., login_url: Incomplete | None = None): ...
def login_not_required(view_func): ...
def permission_required(perm, login_url: Incomplete | None = None, raise_exception: bool = False): ...