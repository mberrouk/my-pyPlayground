from _typeshed import Incomplete
from django import template as template
from django.contrib.admin.utils import quote as quote
from django.urls import Resolver404 as Resolver404, get_script_prefix as get_script_prefix, resolve as resolve
from django.utils.http import urlencode as urlencode

register: Incomplete

def admin_urlname(value, arg): ...
def admin_urlquote(value): ...
def add_preserved_filters(context, url, popup: bool = False, to_field: Incomplete | None = None): ...
