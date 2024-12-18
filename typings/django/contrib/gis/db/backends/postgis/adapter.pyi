from _typeshed import Incomplete
from django.contrib.gis.db.backends.postgis.pgraster import to_pgraster as to_pgraster
from django.contrib.gis.geos import GEOSGeometry as GEOSGeometry
from django.db.backends.postgresql.psycopg_any import sql as sql

class PostGISAdapter:
    is_geometry: Incomplete
    ewkb: Incomplete
    srid: Incomplete
    geography: Incomplete
    def __init__(self, obj, geography: bool = False) -> None: ...
    def __conform__(self, proto): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def getquoted(self): ...