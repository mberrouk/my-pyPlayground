"""
This type stub file was generated by pyright.
"""

from contextlib import ContextDecorator
from decimal import Decimal, ROUND_UP
from django.utils.autoreload import autoreload_started, file_changed
from django.utils.functional import lazy
from django.utils.regex_helper import _lazy_re_compile

"""
Internationalization support.
"""
__all__ = ["activate", "deactivate", "override", "deactivate_all", "get_language", "get_language_from_request", "get_language_info", "get_language_bidi", "check_for_language", "to_language", "to_locale", "templatize", "gettext", "gettext_lazy", "gettext_noop", "ngettext", "ngettext_lazy", "pgettext", "pgettext_lazy", "npgettext", "npgettext_lazy"]
class TranslatorCommentWarning(SyntaxWarning):
    ...


class Trans:
    """
    The purpose of this class is to store the actual translation function upon
    receiving the first call to that function. After this is done, changes to
    USE_I18N will have no effect to which function is served upon request. If
    your tests rely on changing USE_I18N, you can delete all the functions
    from _trans.__dict__.

    Note that storing the function with setattr will have a noticeable
    performance effect, as access to the function goes the normal path,
    instead of using __getattr__.
    """
    def __getattr__(self, real_name): # -> Any:
        ...
    


_trans = ...
def gettext_noop(message): # -> Any:
    ...

def gettext(message): # -> Any:
    ...

def ngettext(singular, plural, number): # -> Any:
    ...

def pgettext(context, message): # -> Any:
    ...

def npgettext(context, singular, plural, number): # -> Any:
    ...

gettext_lazy = ...
pgettext_lazy = ...
def lazy_number(func, resultclass, number=..., **kwargs): # -> __proxy__:
    ...

def ngettext_lazy(singular, plural, number=...): # -> __proxy__:
    ...

def npgettext_lazy(context, singular, plural, number=...): # -> __proxy__:
    ...

def activate(language): # -> Any:
    ...

def deactivate(): # -> Any:
    ...

class override(ContextDecorator):
    def __init__(self, language, deactivate=...) -> None:
        ...
    
    def __enter__(self): # -> None:
        ...
    
    def __exit__(self, exc_type, exc_value, traceback): # -> None:
        ...
    


def get_language(): # -> Any:
    ...

def get_language_bidi(): # -> Any:
    ...

def check_for_language(lang_code): # -> Any:
    ...

def to_language(locale):
    """Turn a locale name (en_US) into a language name (en-us)."""
    ...

def to_locale(language):
    """Turn a language name (en-us) into a locale name (en_US)."""
    ...

def get_language_from_request(request, check_path=...): # -> Any:
    ...

def get_language_from_path(path): # -> Any:
    ...

def get_supported_language_variant(lang_code, *, strict=...): # -> Any:
    ...

def templatize(src, **kwargs):
    ...

def deactivate_all(): # -> Any:
    ...

def get_language_info(lang_code): # -> dict[str, Any]:
    ...

trim_whitespace_re = ...
def trim_whitespace(s): # -> Any:
    ...

def round_away_from_one(value): # -> int:
    ...

