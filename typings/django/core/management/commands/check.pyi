from _typeshed import Incomplete
from django.apps import apps as apps
from django.core import checks as checks
from django.core.checks.registry import registry as registry
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.db import connections as connections

class Command(BaseCommand):
    help: str
    requires_system_checks: Incomplete
    def add_arguments(self, parser) -> None: ...
    def handle(self, *app_labels, **options) -> None: ...
