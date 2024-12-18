from _typeshed import Incomplete
from django.contrib.gis.db import models as models
from django.contrib.gis.db.backends.base.models import SpatialRefSysMixin as SpatialRefSysMixin

class OracleGeometryColumns(models.Model):
    table_name: Incomplete
    column_name: Incomplete
    srid: Incomplete
    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @classmethod
    def table_name_col(cls): ...
    @classmethod
    def geom_col_name(cls): ...

class OracleSpatialRefSys(models.Model, SpatialRefSysMixin):
    cs_name: Incomplete
    srid: Incomplete
    auth_srid: Incomplete
    auth_name: Incomplete
    wktext: Incomplete
    cs_bounds: Incomplete
    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @property
    def wkt(self): ...
