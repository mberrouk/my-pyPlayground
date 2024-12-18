from _typeshed import Incomplete
from django.contrib.gis.db.models import GeometryField as GeometryField
from django.contrib.gis.db.models.functions import Distance as Distance
from django.db import NotSupportedError as NotSupportedError
from django.utils.functional import cached_property as cached_property

class BaseSpatialOperations:
    postgis: bool
    spatialite: bool
    mariadb: bool
    mysql: bool
    oracle: bool
    spatial_version: Incomplete
    select: str
    def select_extent(self): ...
    disallowed_aggregates: Incomplete
    geom_func_prefix: str
    function_names: Incomplete
    unsupported_functions: Incomplete
    from_text: bool
    def convert_extent(self, box, srid) -> None: ...
    def convert_extent3d(self, box, srid) -> None: ...
    def geo_quote_name(self, name): ...
    def geo_db_type(self, f) -> None: ...
    def get_distance(self, f, value, lookup_type) -> None: ...
    def get_geom_placeholder(self, f, value, compiler): ...
    def check_expression_support(self, expression) -> None: ...
    def spatial_aggregate_name(self, agg_name) -> None: ...
    def spatial_function_name(self, func_name): ...
    def geometry_columns(self) -> None: ...
    def spatial_ref_sys(self) -> None: ...
    distance_expr_for_lookup: Incomplete
    def get_db_converters(self, expression): ...
    def get_geometry_converter(self, expression) -> None: ...
    def get_area_att_for_field(self, field): ...
    def get_distance_att_for_field(self, field): ...