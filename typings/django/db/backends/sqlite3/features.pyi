from .base import Database as Database
from _typeshed import Incomplete
from django.db import transaction as transaction
from django.db.backends.base.features import BaseDatabaseFeatures as BaseDatabaseFeatures
from django.db.utils import OperationalError as OperationalError
from django.utils.functional import cached_property as cached_property

class DatabaseFeatures(BaseDatabaseFeatures):
    minimum_database_version: Incomplete
    test_db_allows_multiple_connections: bool
    supports_unspecified_pk: bool
    supports_timezones: bool
    max_query_params: int
    supports_transactions: bool
    atomic_transactions: bool
    can_rollback_ddl: bool
    can_create_inline_fk: bool
    requires_literal_defaults: bool
    can_clone_databases: bool
    supports_temporal_subtraction: bool
    ignores_table_name_case: bool
    supports_cast_with_precision: bool
    time_cast_precision: int
    can_release_savepoints: bool
    has_case_insensitive_like: bool
    can_alter_table_drop_column: Incomplete
    supports_parentheses_in_compound: bool
    can_defer_constraint_checks: bool
    supports_over_clause: bool
    supports_frame_range_fixed_distance: bool
    supports_frame_exclusion: bool
    supports_aggregate_filter_clause: bool
    order_by_nulls_first: bool
    supports_json_field_contains: bool
    supports_update_conflicts: bool
    supports_update_conflicts_with_target: bool
    supports_stored_generated_columns: bool
    supports_virtual_generated_columns: bool
    test_collations: Incomplete
    django_test_expected_failures: Incomplete
    create_test_table_with_composite_primary_key: str
    insert_test_table_with_defaults: str
    supports_default_keyword_in_insert: bool
    def django_test_skips(self): ...
    def introspected_field_types(self): ...
    def supports_json_field(self): ...
    can_introspect_json_field: Incomplete
    has_json_object_function: Incomplete
    def can_return_columns_from_insert(self): ...
    can_return_rows_from_bulk_insert: Incomplete
