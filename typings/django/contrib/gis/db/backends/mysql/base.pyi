from .features import DatabaseFeatures as DatabaseFeatures
from .introspection import MySQLIntrospection as MySQLIntrospection
from .operations import MySQLOperations as MySQLOperations
from .schema import MySQLGISSchemaEditor as MySQLGISSchemaEditor
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper

class DatabaseWrapper(MySQLDatabaseWrapper):
    SchemaEditorClass = MySQLGISSchemaEditor
    features_class = DatabaseFeatures
    introspection_class = MySQLIntrospection
    ops_class = MySQLOperations
