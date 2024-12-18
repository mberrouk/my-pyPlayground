from _typeshed import Incomplete
from django.apps import apps as apps
from django.conf import settings as settings
from django.core import serializers as serializers
from django.db import router as router
from django.db.transaction import atomic as atomic
from django.utils.module_loading import import_string as import_string

TEST_DATABASE_PREFIX: str

class BaseDatabaseCreation:
    connection: Incomplete
    def __init__(self, connection) -> None: ...
    def log(self, msg) -> None: ...
    def create_test_db(self, verbosity: int = 1, autoclobber: bool = False, serialize: bool = True, keepdb: bool = False): ...
    def set_as_test_mirror(self, primary_settings_dict) -> None: ...
    def serialize_db_to_string(self): ...
    def deserialize_db_from_string(self, data) -> None: ...
    def clone_test_db(self, suffix, verbosity: int = 1, autoclobber: bool = False, keepdb: bool = False) -> None: ...
    def get_test_db_clone_settings(self, suffix): ...
    def destroy_test_db(self, old_database_name: Incomplete | None = None, verbosity: int = 1, keepdb: bool = False, suffix: Incomplete | None = None) -> None: ...
    def mark_expected_failures_and_skips(self) -> None: ...
    def sql_table_creation_suffix(self): ...
    def test_db_signature(self): ...
    def setup_worker_connection(self, _worker_id) -> None: ...