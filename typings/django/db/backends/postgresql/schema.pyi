from django.db.backends.base.schema import BaseDatabaseSchemaEditor as BaseDatabaseSchemaEditor
from django.db.backends.ddl_references import IndexColumns as IndexColumns
from django.db.backends.postgresql.psycopg_any import sql as sql
from django.db.backends.utils import strip_quotes as strip_quotes

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_update_with_default: str
    sql_alter_sequence_type: str
    sql_delete_sequence: str
    sql_create_index: str
    sql_create_index_concurrently: str
    sql_delete_index: str
    sql_delete_index_concurrently: str
    sql_create_column_inline_fk: str
    sql_delete_fk: str
    sql_delete_procedure: str
    def execute(self, sql, params=()): ...
    sql_add_identity: str
    sql_drop_indentity: str
    def quote_value(self, value): ...
    def add_index(self, model, index, concurrently: bool = False) -> None: ...
    def remove_index(self, model, index, concurrently: bool = False) -> None: ...
