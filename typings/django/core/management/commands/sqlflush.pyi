from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.sql import sql_flush as sql_flush
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections

class Command(BaseCommand):
    help: str
    output_transaction: bool
    def add_arguments(self, parser) -> None: ...
    def handle(self, **options): ...
