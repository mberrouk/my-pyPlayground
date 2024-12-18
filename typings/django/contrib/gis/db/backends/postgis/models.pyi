from _typeshed import Incomplete
from django.contrib.gis.db.backends.base.models import SpatialRefSysMixin as SpatialRefSysMixin
from django.db import models as models

class PostGISGeometryColumns(models.Model):
    f_table_catalog: Incomplete
    f_table_schema: Incomplete
    f_table_name: Incomplete
    f_geometry_column: Incomplete
    coord_dimension: Incomplete
    srid: Incomplete
    type: Incomplete
    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @classmethod
    def table_name_col(cls): ...
    @classmethod
    def geom_col_name(cls): ...

class PostGISSpatialRefSys(models.Model, SpatialRefSysMixin):
    srid: Incomplete
    auth_name: Incomplete
    auth_srid: Incomplete
    srtext: Incomplete
    proj4text: Incomplete
    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @property
    def wkt(self): ...
