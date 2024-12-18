from . import Error as Error, Tags as Tags, register as register
from _typeshed import Incomplete
from django.conf import settings as settings
from django.utils.translation import get_supported_language_variant as get_supported_language_variant
from django.utils.translation.trans_real import language_code_re as language_code_re

E001: Incomplete
E002: Incomplete
E003: Incomplete
E004: Incomplete

def check_setting_language_code(app_configs, **kwargs): ...
def check_setting_languages(app_configs, **kwargs): ...
def check_setting_languages_bidi(app_configs, **kwargs): ...
def check_language_settings_consistent(app_configs, **kwargs): ...
