"""
This type stub file was generated by pyright.
"""

from django.core.cache import caches
from . import Tags, register

E001 = ...
@register(Tags.caches)
def check_default_cache_is_configured(app_configs, **kwargs): # -> list[Error] | list[Any]:
    ...

@register(Tags.caches, deploy=True)
def check_cache_location_not_exposed(app_configs, **kwargs): # -> list[Any]:
    ...

@register(Tags.caches)
def check_file_based_cache_is_absolute(app_configs, **kwargs): # -> list[Any]:
    ...
