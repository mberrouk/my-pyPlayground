from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.cache import caches as caches
from django.core.cache.backends.db import BaseDatabaseCache as BaseDatabaseCache
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, DatabaseError as DatabaseError, connections as connections, models as models, router as router, transaction as transaction

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    def add_arguments(self, parser) -> None: ...
    verbosity: Incomplete
    def handle(self, *tablenames, **options) -> None: ...
    def create_table(self, database, tablename, dry_run) -> None: ...
