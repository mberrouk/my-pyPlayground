from _typeshed import Incomplete
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.db.backends.base.base import BaseDatabaseWrapper as BaseDatabaseWrapper
from django.db.backends.base.client import BaseDatabaseClient as BaseDatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation as BaseDatabaseCreation
from django.db.backends.base.introspection import BaseDatabaseIntrospection as BaseDatabaseIntrospection
from django.db.backends.base.operations import BaseDatabaseOperations as BaseDatabaseOperations
from django.db.backends.dummy.features import DummyDatabaseFeatures as DummyDatabaseFeatures

def complain(*args, **kwargs) -> None: ...
def ignore(*args, **kwargs) -> None: ...

class DatabaseOperations(BaseDatabaseOperations):
    quote_name = complain

class DatabaseClient(BaseDatabaseClient):
    runshell = complain

class DatabaseCreation(BaseDatabaseCreation):
    create_test_db = ignore
    destroy_test_db = ignore

class DatabaseIntrospection(BaseDatabaseIntrospection):
    get_table_list = complain
    get_table_description = complain
    get_relations = complain
    get_indexes = complain

class DatabaseWrapper(BaseDatabaseWrapper):
    operators: Incomplete
    ensure_connection = complain
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DummyDatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations
    def is_usable(self): ...
