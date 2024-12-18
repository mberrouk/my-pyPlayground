from django.core.management.base import AppCommand as AppCommand
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections

class Command(AppCommand):
    help: str
    output_transaction: bool
    def add_arguments(self, parser) -> None: ...
    def handle_app_config(self, app_config, **options): ...
