from .client import SpatiaLiteClient as SpatiaLiteClient
from .features import DatabaseFeatures as DatabaseFeatures
from .introspection import SpatiaLiteIntrospection as SpatiaLiteIntrospection
from .operations import SpatiaLiteOperations as SpatiaLiteOperations
from .schema import SpatialiteSchemaEditor as SpatialiteSchemaEditor
from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.db.backends.sqlite3.base import DatabaseWrapper as SQLiteDatabaseWrapper

class DatabaseWrapper(SQLiteDatabaseWrapper):
    SchemaEditorClass = SpatialiteSchemaEditor
    client_class = SpatiaLiteClient
    features_class = DatabaseFeatures
    introspection_class = SpatiaLiteIntrospection
    ops_class = SpatiaLiteOperations
    lib_spatialite_paths: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_new_connection(self, conn_params): ...
    def prepare_database(self) -> None: ...
