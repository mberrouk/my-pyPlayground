from .features import DatabaseFeatures as DatabaseFeatures
from .introspection import OracleIntrospection as OracleIntrospection
from .operations import OracleOperations as OracleOperations
from .schema import OracleGISSchemaEditor as OracleGISSchemaEditor
from django.db.backends.oracle.base import DatabaseWrapper as OracleDatabaseWrapper

class DatabaseWrapper(OracleDatabaseWrapper):
    SchemaEditorClass = OracleGISSchemaEditor
    features_class = DatabaseFeatures
    introspection_class = OracleIntrospection
    ops_class = OracleOperations
