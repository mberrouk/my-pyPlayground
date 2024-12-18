from django.apps import apps as apps
from django.core import serializers as serializers
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.core.management.utils import parse_apps_and_model_labels as parse_apps_and_model_labels
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections, router as router

has_bz2: bool
has_lzma: bool

class ProxyModelWarning(Warning): ...

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *app_labels, **options) -> None: ...
