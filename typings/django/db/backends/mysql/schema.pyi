from _typeshed import Incomplete
from django.db.backends.base.schema import BaseDatabaseSchemaEditor as BaseDatabaseSchemaEditor
from django.db.models import F as F, NOT_PROVIDED as NOT_PROVIDED, UniqueConstraint as UniqueConstraint
from django.db.models.constants import LOOKUP_SEP as LOOKUP_SEP

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_rename_table: str
    sql_alter_column_null: str
    sql_alter_column_not_null: str
    sql_alter_column_type: str
    sql_alter_column_no_default_null: str
    sql_delete_column: str
    sql_delete_unique: str
    sql_create_column_inline_fk: str
    sql_delete_fk: str
    sql_delete_index: str
    sql_rename_index: str
    sql_create_pk: str
    sql_delete_pk: str
    sql_create_index: str
    sql_alter_table_comment: str
    sql_alter_column_comment: Incomplete
    @property
    def sql_delete_check(self): ...
    @property
    def sql_rename_column(self): ...
    def quote_value(self, value): ...
    def skip_default(self, field): ...
    def skip_default_on_alter(self, field): ...
    def add_field(self, model, field) -> None: ...
    def remove_constraint(self, model, constraint) -> None: ...
    def remove_index(self, model, index) -> None: ...
