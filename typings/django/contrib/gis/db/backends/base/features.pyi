from _typeshed import Incomplete
from django.contrib.gis.db import models as models

class BaseSpatialFeatures:
    gis_enabled: bool
    has_spatialrefsys_table: bool
    supports_add_srs_entry: bool
    supports_geometry_field_introspection: bool
    supports_geography: bool
    supports_3d_storage: bool
    supports_3d_functions: bool
    supports_transform: bool
    supports_null_geometries: bool
    supports_empty_geometries: bool
    supports_distance_geodetic: bool
    supports_length_geodetic: bool
    supports_perimeter_geodetic: bool
    supports_area_geodetic: bool
    supports_num_points_poly: bool
    supports_dwithin_distance_expr: bool
    supports_raster: bool
    supports_geometry_field_unique_index: bool
    can_alter_geometry_field: bool
    supports_tolerance_parameter: bool
    unsupported_geojson_options: Incomplete
    empty_intersection_returns_none: bool
    @property
    def supports_bbcontains_lookup(self): ...
    @property
    def supports_contained_lookup(self): ...
    @property
    def supports_crosses_lookup(self): ...
    @property
    def supports_distances_lookups(self): ...
    @property
    def supports_dwithin_lookup(self): ...
    @property
    def supports_relate_lookup(self): ...
    @property
    def supports_isvalid_lookup(self): ...
    @property
    def supports_collect_aggr(self): ...
    @property
    def supports_extent_aggr(self): ...
    @property
    def supports_make_line_aggr(self): ...
    @property
    def supports_union_aggr(self): ...
    def __getattr__(self, name): ...
