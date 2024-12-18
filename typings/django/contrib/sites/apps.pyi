from .management import create_default_site as create_default_site
from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.contrib.sites.checks import check_site_id as check_site_id
from django.core import checks as checks
from django.db.models.signals import post_migrate as post_migrate

class SitesConfig(AppConfig):
    default_auto_field: str
    name: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
