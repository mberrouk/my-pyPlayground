from _typeshed import Incomplete
from django.contrib.gis.db.backends.base.adapter import WKTAdapter as WKTAdapter
from django.contrib.gis.geos import GeometryCollection as GeometryCollection, Polygon as Polygon
from django.db.backends.oracle.oracledb_any import oracledb as oracledb

class OracleSpatialAdapter(WKTAdapter):
    input_size: Incomplete
    wkt: Incomplete
    srid: Incomplete
    def __init__(self, geom) -> None: ...
