from _typeshed import Incomplete
from django.conf import settings as settings
from django.core import checks as checks
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.db import models as models

class CurrentSiteManager(models.Manager):
    use_in_migrations: bool
    def __init__(self, field_name: Incomplete | None = None) -> None: ...
    def check(self, **kwargs): ...
    def get_queryset(self): ...
