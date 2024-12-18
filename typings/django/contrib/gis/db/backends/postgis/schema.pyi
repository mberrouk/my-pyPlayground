from django.db.backends.postgresql.schema import DatabaseSchemaEditor as DatabaseSchemaEditor
from django.db.models.expressions import Col as Col, Func as Func

class PostGISSchemaEditor(DatabaseSchemaEditor):
    geom_index_type: str
    geom_index_ops_nd: str
    rast_index_template: str
    sql_alter_column_to_3d: str
    sql_alter_column_to_2d: str
    def geo_quote_name(self, name): ...
