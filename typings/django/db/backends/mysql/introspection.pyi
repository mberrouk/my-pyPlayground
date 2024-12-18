from _typeshed import Incomplete
from django.db.backends.base.introspection import BaseDatabaseIntrospection as BaseDatabaseIntrospection
from django.db.models import Index as Index
from django.utils.datastructures import OrderedSet as OrderedSet
from typing import NamedTuple

FieldInfo: Incomplete

class InfoLine(NamedTuple):
    col_name: Incomplete
    data_type: Incomplete
    max_len: Incomplete
    num_prec: Incomplete
    num_scale: Incomplete
    extra: Incomplete
    column_default: Incomplete
    collation: Incomplete
    is_unsigned: Incomplete
    comment: Incomplete

TableInfo: Incomplete

class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse: Incomplete
    def get_field_type(self, data_type, description): ...
    def get_table_list(self, cursor): ...
    def get_table_description(self, cursor, table_name): ...
    def get_sequences(self, cursor, table_name, table_fields=()): ...
    def get_relations(self, cursor, table_name): ...
    def get_storage_engine(self, cursor, table_name): ...
    def get_constraints(self, cursor, table_name): ...
