from _typeshed import Incomplete
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    def add_arguments(self, parser) -> None: ...
    def handle(self, **options) -> None: ...
