from django.apps import apps as apps
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.core.management.utils import run_formatters as run_formatters
from django.db import migrations as migrations
from django.db.migrations.exceptions import AmbiguityError as AmbiguityError
from django.db.migrations.loader import MigrationLoader as MigrationLoader
from django.db.migrations.optimizer import MigrationOptimizer as MigrationOptimizer
from django.db.migrations.writer import MigrationWriter as MigrationWriter
from django.utils.version import get_docs_version as get_docs_version

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
