from _typeshed import Incomplete
from django.apps import apps as apps
from django.conf import settings as settings
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError, no_translations as no_translations
from django.core.management.utils import run_formatters as run_formatters
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, OperationalError as OperationalError, connections as connections, router as router
from django.db.migrations import Migration as Migration
from django.db.migrations.autodetector import MigrationAutodetector as MigrationAutodetector
from django.db.migrations.loader import MigrationLoader as MigrationLoader
from django.db.migrations.migration import SwappableTuple as SwappableTuple
from django.db.migrations.optimizer import MigrationOptimizer as MigrationOptimizer
from django.db.migrations.questioner import InteractiveMigrationQuestioner as InteractiveMigrationQuestioner, MigrationQuestioner as MigrationQuestioner, NonInteractiveMigrationQuestioner as NonInteractiveMigrationQuestioner
from django.db.migrations.state import ProjectState as ProjectState
from django.db.migrations.utils import get_migration_name_timestamp as get_migration_name_timestamp
from django.db.migrations.writer import MigrationWriter as MigrationWriter

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    @property
    def log_output(self): ...
    def log(self, msg) -> None: ...
    written_files: Incomplete
    verbosity: Incomplete
    interactive: Incomplete
    dry_run: Incomplete
    merge: Incomplete
    empty: Incomplete
    migration_name: Incomplete
    include_header: Incomplete
    scriptable: Incomplete
    update: Incomplete
    def handle(self, *app_labels, **options): ...
    def write_to_last_migration_files(self, changes) -> None: ...
    def write_migration_files(self, changes, update_previous_migration_paths: Incomplete | None = None) -> None: ...
    @staticmethod
    def get_relative_path(path): ...
    def handle_merge(self, loader, conflicts): ...
