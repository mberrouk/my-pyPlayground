from _typeshed import Incomplete
from django.db import DataError as DataError, InterfaceError as InterfaceError
from django.db.backends.base.features import BaseDatabaseFeatures as BaseDatabaseFeatures
from django.db.backends.postgresql.psycopg_any import is_psycopg3 as is_psycopg3
from django.utils.functional import cached_property as cached_property

class DatabaseFeatures(BaseDatabaseFeatures):
    minimum_database_version: Incomplete
    allows_group_by_selected_pks: bool
    can_return_columns_from_insert: bool
    can_return_rows_from_bulk_insert: bool
    has_real_datatype: bool
    has_native_uuid_field: bool
    has_native_duration_field: bool
    has_native_json_field: bool
    can_defer_constraint_checks: bool
    has_select_for_update: bool
    has_select_for_update_nowait: bool
    has_select_for_update_of: bool
    has_select_for_update_skip_locked: bool
    has_select_for_no_key_update: bool
    can_release_savepoints: bool
    supports_comments: bool
    supports_tablespaces: bool
    supports_transactions: bool
    can_introspect_materialized_views: bool
    can_distinct_on_fields: bool
    can_rollback_ddl: bool
    schema_editor_uses_clientside_param_binding: bool
    supports_combined_alters: bool
    nulls_order_largest: bool
    closed_cursor_error_class = InterfaceError
    greatest_least_ignores_nulls: bool
    can_clone_databases: bool
    supports_temporal_subtraction: bool
    supports_slicing_ordering_in_compound: bool
    create_test_procedure_without_params_sql: str
    create_test_procedure_with_int_param_sql: str
    create_test_table_with_composite_primary_key: str
    requires_casted_case_in_updates: bool
    supports_over_clause: bool
    supports_frame_exclusion: bool
    only_supports_unbounded_with_preceding_and_following: bool
    supports_aggregate_filter_clause: bool
    supported_explain_formats: Incomplete
    supports_deferrable_unique_constraints: bool
    has_json_operators: bool
    json_key_contains_list_matching_requires_list: bool
    supports_update_conflicts: bool
    supports_update_conflicts_with_target: bool
    supports_covering_indexes: bool
    supports_stored_generated_columns: bool
    supports_virtual_generated_columns: bool
    can_rename_index: bool
    test_collations: Incomplete
    test_now_utc_template: str
    insert_test_table_with_defaults: str
    def django_test_skips(self): ...
    def django_test_expected_failures(self): ...
    def uses_server_side_binding(self): ...
    def prohibits_null_characters_in_text_exception(self): ...
    def introspected_field_types(self): ...
    def is_postgresql_14(self): ...
    def is_postgresql_15(self): ...
    def is_postgresql_16(self): ...
    has_bit_xor: Incomplete
    supports_covering_spgist_indexes: Incomplete
    supports_unlimited_charfield: bool
    supports_nulls_distinct_unique_constraints: Incomplete
