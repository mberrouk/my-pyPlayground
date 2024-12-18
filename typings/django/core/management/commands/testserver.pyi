from _typeshed import Incomplete
from django.core.management import call_command as call_command
from django.core.management.base import BaseCommand as BaseCommand
from django.db import connection as connection

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    def add_arguments(self, parser) -> None: ...
    def handle(self, *fixture_labels, **options) -> None: ...
