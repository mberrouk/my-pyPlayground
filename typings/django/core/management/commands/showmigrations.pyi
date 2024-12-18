from _typeshed import Incomplete
from django.apps import apps as apps
from django.core.management.base import BaseCommand as BaseCommand
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections
from django.db.migrations.loader import MigrationLoader as MigrationLoader
from django.db.migrations.recorder import MigrationRecorder as MigrationRecorder

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    verbosity: Incomplete
    def handle(self, *args, **options): ...
    def show_list(self, connection, app_names: Incomplete | None = None) -> None: ...
    def show_plan(self, connection, app_names: Incomplete | None = None): ...
