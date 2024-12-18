from _typeshed import Incomplete
from django.contrib.gis.db.backends.base.features import BaseSpatialFeatures as BaseSpatialFeatures
from django.db.backends.mysql.features import DatabaseFeatures as MySQLDatabaseFeatures
from django.utils.functional import cached_property as cached_property

class DatabaseFeatures(BaseSpatialFeatures, MySQLDatabaseFeatures):
    empty_intersection_returns_none: bool
    has_spatialrefsys_table: bool
    supports_add_srs_entry: bool
    supports_distance_geodetic: bool
    supports_length_geodetic: bool
    supports_area_geodetic: bool
    supports_transform: bool
    supports_null_geometries: bool
    supports_num_points_poly: bool
    unsupported_geojson_options: Incomplete
    def supports_geometry_field_unique_index(self): ...
