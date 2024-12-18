from django.db import DatabaseError as DatabaseError
from django.db.backends.base.schema import BaseDatabaseSchemaEditor as BaseDatabaseSchemaEditor
from django.utils.duration import duration_iso_string as duration_iso_string

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_create_column: str
    sql_alter_column_type: str
    sql_alter_column_null: str
    sql_alter_column_not_null: str
    sql_alter_column_default: str
    sql_alter_column_no_default: str
    sql_alter_column_no_default_null = sql_alter_column_no_default
    sql_delete_column: str
    sql_create_column_inline_fk: str
    sql_delete_table: str
    sql_create_index: str
    def quote_value(self, value): ...
    def remove_field(self, model, field) -> None: ...
    def delete_model(self, model) -> None: ...
    def alter_field(self, model, old_field, new_field, strict: bool = False) -> None: ...
    def normalize_name(self, name): ...
    def prepare_default(self, value): ...
