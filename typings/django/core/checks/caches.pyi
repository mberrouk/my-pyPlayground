from . import Error as Error, Tags as Tags, Warning as Warning, register as register
from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.cache import DEFAULT_CACHE_ALIAS as DEFAULT_CACHE_ALIAS, caches as caches
from django.core.cache.backends.filebased import FileBasedCache as FileBasedCache

E001: Incomplete

def check_default_cache_is_configured(app_configs, **kwargs): ...
def check_cache_location_not_exposed(app_configs, **kwargs): ...
def check_file_based_cache_is_absolute(app_configs, **kwargs): ...
