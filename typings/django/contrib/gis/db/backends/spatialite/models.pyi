from _typeshed import Incomplete
from django.contrib.gis.db.backends.base.models import SpatialRefSysMixin as SpatialRefSysMixin
from django.db import models as models

class SpatialiteGeometryColumns(models.Model):
    f_table_name: Incomplete
    f_geometry_column: Incomplete
    coord_dimension: Incomplete
    srid: Incomplete
    spatial_index_enabled: Incomplete
    type: Incomplete
    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @classmethod
    def table_name_col(cls): ...
    @classmethod
    def geom_col_name(cls): ...

class SpatialiteSpatialRefSys(models.Model, SpatialRefSysMixin):
    srid: Incomplete
    auth_name: Incomplete
    auth_srid: Incomplete
    ref_sys_name: Incomplete
    proj4text: Incomplete
    srtext: Incomplete
    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @property
    def wkt(self): ...
