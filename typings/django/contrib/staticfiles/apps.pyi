from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.contrib.staticfiles.checks import check_finders as check_finders, check_storages as check_storages
from django.core import checks as checks

class StaticFilesConfig(AppConfig):
    name: str
    verbose_name: Incomplete
    ignore_patterns: Incomplete
    def ready(self) -> None: ...
