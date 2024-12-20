"""
This type stub file was generated by pyright.
"""

from . import Tags, register

E001 = ...
E002 = ...
E003 = ...
E004 = ...
@register(Tags.translation)
def check_setting_language_code(app_configs, **kwargs): # -> list[Error] | list[Any]:
    """Error if LANGUAGE_CODE setting is invalid."""
    ...

@register(Tags.translation)
def check_setting_languages(app_configs, **kwargs): # -> list[Error]:
    """Error if LANGUAGES setting is invalid."""
    ...

@register(Tags.translation)
def check_setting_languages_bidi(app_configs, **kwargs): # -> list[Error]:
    """Error if LANGUAGES_BIDI setting is invalid."""
    ...

@register(Tags.translation)
def check_language_settings_consistent(app_configs, **kwargs): # -> list[Any] | list[Error]:
    """Error if language settings are not consistent with each other."""
    ...

