from django.contrib.gis.db.backends.base.features import BaseSpatialFeatures as BaseSpatialFeatures
from django.db.backends.sqlite3.features import DatabaseFeatures as SQLiteDatabaseFeatures
from django.utils.functional import cached_property as cached_property

class DatabaseFeatures(BaseSpatialFeatures, SQLiteDatabaseFeatures):
    can_alter_geometry_field: bool
    supports_3d_storage: bool
    def supports_area_geodetic(self): ...
    def django_test_skips(self): ...
