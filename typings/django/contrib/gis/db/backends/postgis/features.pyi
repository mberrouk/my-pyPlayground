from django.contrib.gis.db.backends.base.features import BaseSpatialFeatures as BaseSpatialFeatures
from django.db.backends.postgresql.features import DatabaseFeatures as PsycopgDatabaseFeatures

class DatabaseFeatures(BaseSpatialFeatures, PsycopgDatabaseFeatures):
    supports_geography: bool
    supports_3d_storage: bool
    supports_3d_functions: bool
    supports_raster: bool
    supports_empty_geometries: bool
    empty_intersection_returns_none: bool
