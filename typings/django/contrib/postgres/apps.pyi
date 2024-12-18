from .indexes import OpClass as OpClass
from .lookups import SearchLookup as SearchLookup, TrigramSimilar as TrigramSimilar, TrigramStrictWordSimilar as TrigramStrictWordSimilar, TrigramWordSimilar as TrigramWordSimilar, Unaccent as Unaccent
from .serializers import RangeSerializer as RangeSerializer
from .signals import register_type_handlers as register_type_handlers
from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.core.signals import setting_changed as setting_changed
from django.db import connections as connections
from django.db.backends.postgresql.psycopg_any import RANGE_TYPES as RANGE_TYPES
from django.db.backends.signals import connection_created as connection_created
from django.db.migrations.writer import MigrationWriter as MigrationWriter
from django.db.models import CharField as CharField, OrderBy as OrderBy, TextField as TextField
from django.db.models.functions import Collate as Collate
from django.db.models.indexes import IndexExpression as IndexExpression

def uninstall_if_needed(setting, value, enter, **kwargs) -> None: ...

class PostgresConfig(AppConfig):
    name: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
