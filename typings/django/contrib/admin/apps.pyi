from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.contrib.admin.checks import check_admin_app as check_admin_app, check_dependencies as check_dependencies
from django.core import checks as checks

class SimpleAdminConfig(AppConfig):
    default_auto_field: str
    default_site: str
    name: str
    verbose_name: Incomplete
    def ready(self) -> None: ...

class AdminConfig(SimpleAdminConfig):
    default: bool
    def ready(self) -> None: ...
