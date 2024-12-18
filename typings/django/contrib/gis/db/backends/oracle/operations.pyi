from _typeshed import Incomplete
from django.contrib.gis.db import models as models
from django.contrib.gis.db.backends.base.operations import BaseSpatialOperations as BaseSpatialOperations
from django.contrib.gis.db.backends.oracle.adapter import OracleSpatialAdapter as OracleSpatialAdapter
from django.contrib.gis.db.backends.utils import SpatialOperator as SpatialOperator
from django.contrib.gis.geos.geometry import GEOSGeometry as GEOSGeometry, GEOSGeometryBase as GEOSGeometryBase
from django.contrib.gis.geos.prototypes.io import wkb_r as wkb_r
from django.contrib.gis.measure import Distance as Distance
from django.db.backends.oracle.operations import DatabaseOperations as DatabaseOperations

DEFAULT_TOLERANCE: str

class SDOOperator(SpatialOperator):
    sql_template: str

class SDODWithin(SpatialOperator):
    sql_template: str

class SDODisjoint(SpatialOperator):
    sql_template: Incomplete

class SDORelate(SpatialOperator):
    sql_template: str
    def check_relate_argument(self, arg) -> None: ...
    def as_sql(self, connection, lookup, template_params, sql_params): ...

class OracleOperations(BaseSpatialOperations, DatabaseOperations):
    name: str
    oracle: bool
    disallowed_aggregates: Incomplete
    Adapter = OracleSpatialAdapter
    extent: str
    unionagg: str
    from_text: str
    function_names: Incomplete
    select: str
    gis_operators: Incomplete
    unsupported_functions: Incomplete
    def geo_quote_name(self, name): ...
    def convert_extent(self, clob): ...
    def geo_db_type(self, f): ...
    def get_distance(self, f, value, lookup_type): ...
    def get_geom_placeholder(self, f, value, compiler): ...
    def spatial_aggregate_name(self, agg_name): ...
    def geometry_columns(self): ...
    def spatial_ref_sys(self): ...
    def modify_insert_params(self, placeholder, params): ...
    def get_geometry_converter(self, expression): ...
    def get_area_att_for_field(self, field): ...
