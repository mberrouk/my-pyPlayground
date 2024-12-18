from _typeshed import Incomplete
from django.apps import apps as apps
from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.core.management.color import no_style as no_style
from django.core.management.sql import emit_post_migrate_signal as emit_post_migrate_signal, sql_flush as sql_flush
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections

class Command(BaseCommand):
    help: str
    stealth_options: Incomplete
    def add_arguments(self, parser) -> None: ...
    style: Incomplete
    def handle(self, **options) -> None: ...
