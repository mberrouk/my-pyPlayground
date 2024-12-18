from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.core import serializers as serializers

class GISConfig(AppConfig):
    default_auto_field: str
    name: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
