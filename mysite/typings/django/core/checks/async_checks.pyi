"""
This type stub file was generated by pyright.
"""

from . import Tags, register

E001 = ...
@register(Tags.async_support, deploy=True)
def check_async_unsafe(app_configs, **kwargs): # -> list[Error] | list[Any]:
    ...

