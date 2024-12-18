from _typeshed import Incomplete
from django.contrib.auth import REDIRECT_FIELD_NAME as REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test as user_passes_test

def staff_member_required(view_func: Incomplete | None = None, redirect_field_name=..., login_url: str = 'admin:login'): ...
