from django.conf import settings as settings
from django.db import DatabaseError as DatabaseError
from django.db.backends.base.creation import BaseDatabaseCreation as BaseDatabaseCreation
from django.utils.crypto import get_random_string as get_random_string
from django.utils.functional import cached_property as cached_property

TEST_DATABASE_PREFIX: str

class DatabaseCreation(BaseDatabaseCreation):
    def set_as_test_mirror(self, primary_settings_dict) -> None: ...
    def test_db_signature(self): ...
