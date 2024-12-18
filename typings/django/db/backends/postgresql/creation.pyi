from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.db.backends.base.creation import BaseDatabaseCreation as BaseDatabaseCreation
from django.db.backends.postgresql.psycopg_any import errors as errors
from django.db.backends.utils import strip_quotes as strip_quotes

class DatabaseCreation(BaseDatabaseCreation):
    def sql_table_creation_suffix(self): ...
