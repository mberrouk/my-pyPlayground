"""
This type stub file was generated by pyright.
"""

from . import Tags, register

@register(Tags.templates)
def check_templates(app_configs, **kwargs): # -> list[Any]:
    """Check all registered template engines."""
    ...
