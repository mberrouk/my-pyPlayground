"""
This type stub file was generated by pyright.
"""

from typing import Any
from django.db.backends.base.base import BaseDatabaseWrapper

TEST_DATABASE_PREFIX: str
class BaseDatabaseCreation:
    connection: BaseDatabaseWrapper
    def __init__(self, connection: BaseDatabaseWrapper) -> None:
        ...
    
    def log(self, msg: str) -> None:
        ...
    
    def create_test_db(self, verbosity: int = ..., autoclobber: bool = ..., serialize: bool = ..., keepdb: bool = ...) -> str:
        ...
    
    def set_as_test_mirror(self, primary_settings_dict: dict[str, dict[str, None] | int | str | None]) -> None:
        ...
    
    def serialize_db_to_string(self) -> str:
        ...
    
    def deserialize_db_from_string(self, data: str) -> None:
        ...
    
    def clone_test_db(self, suffix: Any, verbosity: int = ..., autoclobber: bool = ..., keepdb: bool = ...) -> None:
        ...
    
    def get_test_db_clone_settings(self, suffix: str) -> dict[str, Any]:
        ...
    
    def destroy_test_db(self, old_database_name: str | None = ..., verbosity: int = ..., keepdb: bool = ..., suffix: str | None = ...) -> None:
        ...
    
    def mark_expected_failures_and_skips(self) -> None:
        ...
    
    def sql_table_creation_suffix(self) -> str:
        ...
    
    def test_db_signature(self) -> tuple[str, str, str, str]:
        ...
    
    def setup_worker_connection(self, _worker_id: int) -> None:
        ...
    


