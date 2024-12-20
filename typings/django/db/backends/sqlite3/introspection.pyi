from _typeshed import Incomplete
from django.db import DatabaseError as DatabaseError
from django.db.backends.base.introspection import BaseDatabaseIntrospection as BaseDatabaseIntrospection, TableInfo as TableInfo
from django.db.models import Index as Index

FieldInfo: Incomplete
field_size_re: Incomplete

def get_field_size(name): ...

class FlexibleFieldLookupDict:
    base_data_types_reverse: Incomplete
    def __getitem__(self, key): ...

class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse: Incomplete
    def get_field_type(self, data_type, description): ...
    def get_table_list(self, cursor): ...
    def get_table_description(self, cursor, table_name): ...
    def get_sequences(self, cursor, table_name, table_fields=()): ...
    def get_relations(self, cursor, table_name): ...
    def get_primary_key_columns(self, cursor, table_name): ...
    def get_constraints(self, cursor, table_name): ...
