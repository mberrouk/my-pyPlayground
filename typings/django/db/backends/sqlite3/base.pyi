from .client import DatabaseClient as DatabaseClient
from .creation import DatabaseCreation as DatabaseCreation
from .features import DatabaseFeatures as DatabaseFeatures
from .introspection import DatabaseIntrospection as DatabaseIntrospection
from .operations import DatabaseOperations as DatabaseOperations
from .schema import DatabaseSchemaEditor as DatabaseSchemaEditor
from _typeshed import Incomplete
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.db import IntegrityError as IntegrityError
from django.db.backends.base.base import BaseDatabaseWrapper as BaseDatabaseWrapper
from django.utils.asyncio import async_unsafe as async_unsafe
from django.utils.dateparse import parse_date as parse_date, parse_datetime as parse_datetime, parse_time as parse_time
from sqlite3 import dbapi2 as Database

def decoder(conv_func): ...
def adapt_date(val): ...
def adapt_datetime(val): ...

class DatabaseWrapper(BaseDatabaseWrapper):
    vendor: str
    display_name: str
    data_types: Incomplete
    data_type_check_constraints: Incomplete
    data_types_suffix: Incomplete
    operators: Incomplete
    pattern_esc: str
    pattern_ops: Incomplete
    transaction_modes: Incomplete
    Database = Database
    SchemaEditorClass = DatabaseSchemaEditor
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations
    transaction_mode: Incomplete
    init_commands: Incomplete
    def get_connection_params(self): ...
    def get_database_version(self): ...
    def get_new_connection(self, conn_params): ...
    def create_cursor(self, name: Incomplete | None = None): ...
    def close(self) -> None: ...
    def disable_constraint_checking(self): ...
    def enable_constraint_checking(self) -> None: ...
    def check_constraints(self, table_names: Incomplete | None = None) -> None: ...
    def is_usable(self): ...
    def is_in_memory_db(self): ...

FORMAT_QMARK_REGEX: Incomplete

class SQLiteCursorWrapper(Database.Cursor):
    def execute(self, query, params: Incomplete | None = None): ...
    def executemany(self, query, param_list): ...
    def convert_query(self, query, *, param_names: Incomplete | None = None): ...
