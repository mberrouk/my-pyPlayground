from django.apps import apps as apps
from django.contrib.contenttypes.models import ContentType as ContentType
from django.core.management import BaseCommand as BaseCommand
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections, router as router
from django.db.models.deletion import Collector as Collector

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, **options): ...

class NoFastDeleteCollector(Collector):
    def can_fast_delete(self, *args, **kwargs): ...
