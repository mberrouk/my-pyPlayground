from _typeshed import Incomplete
from django.contrib.sites.models import Site as Site
from django.db import models as models

class Redirect(models.Model):
    site: Incomplete
    old_path: Incomplete
    new_path: Incomplete
    class Meta:
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
        db_table: str
        unique_together: Incomplete
        ordering: Incomplete
