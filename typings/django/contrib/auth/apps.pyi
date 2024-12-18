from . import get_user_model as get_user_model
from .checks import check_middleware as check_middleware, check_models_permissions as check_models_permissions, check_user_model as check_user_model
from .management import create_permissions as create_permissions
from .signals import user_logged_in as user_logged_in
from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.core import checks as checks
from django.db.models.query_utils import DeferredAttribute as DeferredAttribute
from django.db.models.signals import post_migrate as post_migrate

class AuthConfig(AppConfig):
    default_auto_field: str
    name: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
