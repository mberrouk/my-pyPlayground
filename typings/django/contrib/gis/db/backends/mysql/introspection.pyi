from _typeshed import Incomplete
from django.contrib.gis.gdal import OGRGeomType as OGRGeomType
from django.db.backends.mysql.introspection import DatabaseIntrospection as DatabaseIntrospection

class MySQLIntrospection(DatabaseIntrospection):
    data_types_reverse: Incomplete
    def get_geometry_type(self, table_name, description): ...
    def supports_spatial_index(self, cursor, table_name): ...
