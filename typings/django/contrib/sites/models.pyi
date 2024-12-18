from _typeshed import Incomplete
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured, ValidationError as ValidationError
from django.db import models as models
from django.db.models.signals import pre_delete as pre_delete, pre_save as pre_save
from django.http.request import split_domain_port as split_domain_port

SITE_CACHE: Incomplete

class SiteManager(models.Manager):
    use_in_migrations: bool
    def get_current(self, request: Incomplete | None = None): ...
    def clear_cache(self) -> None: ...
    def get_by_natural_key(self, domain): ...

class Site(models.Model):
    domain: Incomplete
    name: Incomplete
    objects: Incomplete
    class Meta:
        db_table: str
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
        ordering: Incomplete
    def natural_key(self): ...

def clear_site_cache(sender, **kwargs) -> None: ...
