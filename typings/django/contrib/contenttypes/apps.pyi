from .management import create_contenttypes as create_contenttypes, inject_rename_contenttypes_operations as inject_rename_contenttypes_operations
from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.contrib.contenttypes.checks import check_generic_foreign_keys as check_generic_foreign_keys, check_model_name_lengths as check_model_name_lengths
from django.core import checks as checks
from django.db.models.signals import post_migrate as post_migrate, pre_migrate as pre_migrate

class ContentTypesConfig(AppConfig):
    default_auto_field: str
    name: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
