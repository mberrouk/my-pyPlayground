from _typeshed import Incomplete
from django.conf import settings as settings
from django.urls import LocalePrefixPattern as LocalePrefixPattern, URLResolver as URLResolver, get_resolver as get_resolver, path as path
from django.views.i18n import set_language as set_language

def i18n_patterns(*urls, prefix_default_language: bool = True): ...
def is_language_prefix_patterns_used(urlconf): ...

urlpatterns: Incomplete
