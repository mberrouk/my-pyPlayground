from _typeshed import Incomplete
from django.contrib.gis.gdal import OGRGeomType as OGRGeomType
from django.db.backends.sqlite3.introspection import DatabaseIntrospection as DatabaseIntrospection, FlexibleFieldLookupDict as FlexibleFieldLookupDict

class GeoFlexibleFieldLookupDict(FlexibleFieldLookupDict):
    base_data_types_reverse: Incomplete

class SpatiaLiteIntrospection(DatabaseIntrospection):
    data_types_reverse: Incomplete
    def get_geometry_type(self, table_name, description): ...
    def get_constraints(self, cursor, table_name): ...
