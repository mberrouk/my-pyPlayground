from _typeshed import Incomplete
from django.contrib.gis.gdal import OGRGeomType as OGRGeomType
from django.db.backends.postgresql.introspection import DatabaseIntrospection as DatabaseIntrospection

class PostGISIntrospection(DatabaseIntrospection):
    postgis_oid_lookup: Incomplete
    ignored_tables: Incomplete
    def get_field_type(self, data_type, description): ...
    def get_geometry_type(self, table_name, description): ...
