from django.db.backends.oracle.introspection import DatabaseIntrospection as DatabaseIntrospection
from django.db.backends.oracle.oracledb_any import oracledb as oracledb
from django.utils.functional import cached_property as cached_property

class OracleIntrospection(DatabaseIntrospection):
    def data_types_reverse(self): ...
    def get_geometry_type(self, table_name, description): ...
