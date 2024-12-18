from _typeshed import Incomplete
from django.db import models as models

class BaseSessionManager(models.Manager):
    def encode(self, session_dict): ...
    def save(self, session_key, session_dict, expire_date): ...

class AbstractBaseSession(models.Model):
    session_key: Incomplete
    session_data: Incomplete
    expire_date: Incomplete
    objects: Incomplete
    class Meta:
        abstract: bool
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
    @classmethod
    def get_session_store_class(cls) -> None: ...
    def get_decoded(self): ...
