from _typeshed import Incomplete
from django.conf import STATICFILES_STORAGE_ALIAS as STATICFILES_STORAGE_ALIAS, settings as settings
from django.contrib.staticfiles.finders import get_finders as get_finders
from django.core.checks import Error as Error

E005: Incomplete

def check_finders(app_configs: Incomplete | None = None, **kwargs): ...
def check_storages(app_configs: Incomplete | None = None, **kwargs): ...
