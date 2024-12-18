from django.apps import apps as apps
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections
from django.db.migrations.loader import AmbiguityError as AmbiguityError, MigrationLoader as MigrationLoader

class Command(BaseCommand):
    help: str
    output_transaction: bool
    def add_arguments(self, parser) -> None: ...
    def execute(self, *args, **options): ...
    def handle(self, *args, **options): ...
