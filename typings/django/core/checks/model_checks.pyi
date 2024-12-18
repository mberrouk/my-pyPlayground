from _typeshed import Incomplete
from django.apps import apps as apps
from django.conf import settings as settings
from django.core.checks import Error as Error, Tags as Tags, Warning as Warning, register as register

def check_all_models(app_configs: Incomplete | None = None, **kwargs): ...
def check_lazy_references(app_configs: Incomplete | None = None, **kwargs): ...
