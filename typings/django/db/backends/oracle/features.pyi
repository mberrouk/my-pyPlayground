from _typeshed import Incomplete
from django.db import DatabaseError as DatabaseError, InterfaceError as InterfaceError
from django.db.backends.base.features import BaseDatabaseFeatures as BaseDatabaseFeatures
from django.db.backends.oracle.oracledb_any import is_oracledb as is_oracledb
from django.utils.functional import cached_property as cached_property

class DatabaseFeatures(BaseDatabaseFeatures):
    minimum_database_version: Incomplete
    allows_group_by_lob: bool
    allows_group_by_select_index: bool
    interprets_empty_strings_as_nulls: bool
    has_select_for_update: bool
    has_select_for_update_nowait: bool
    has_select_for_update_skip_locked: bool
    has_select_for_update_of: bool
    select_for_update_of_column: bool
    can_return_columns_from_insert: bool
    supports_subqueries_in_group_by: bool
    ignores_unnecessary_order_by_in_subqueries: bool
    supports_transactions: bool
    supports_timezones: bool
    has_native_duration_field: bool
    can_defer_constraint_checks: bool
    supports_partially_nullable_unique_constraints: bool
    supports_deferrable_unique_constraints: bool
    truncates_names: bool
    supports_comments: bool
    supports_tablespaces: bool
    supports_sequence_reset: bool
    can_introspect_materialized_views: bool
    atomic_transactions: bool
    nulls_order_largest: bool
    requires_literal_defaults: bool
    supports_default_keyword_in_bulk_insert: bool
    closed_cursor_error_class = InterfaceError
    supports_select_for_update_with_limit: bool
    supports_temporal_subtraction: bool
    ignores_table_name_case: bool
    supports_index_on_text_field: bool
    create_test_procedure_without_params_sql: str
    create_test_procedure_with_int_param_sql: str
    create_test_table_with_composite_primary_key: str
    supports_callproc_kwargs: bool
    supports_over_clause: bool
    supports_frame_range_fixed_distance: bool
    supports_ignore_conflicts: bool
    max_query_params: Incomplete
    supports_partial_indexes: bool
    supports_stored_generated_columns: bool
    supports_virtual_generated_columns: bool
    can_rename_index: bool
    supports_slicing_ordering_in_compound: bool
    requires_compound_order_by_subquery: bool
    allows_multiple_constraints_on_same_fields: bool
    supports_json_field_contains: bool
    supports_collation_on_textfield: bool
    test_now_utc_template: str
    django_test_expected_failures: Incomplete
    insert_test_table_with_defaults: str
    def django_test_skips(self): ...
    def introspected_field_types(self): ...
    def test_collations(self): ...
    def supports_collation_on_charfield(self): ...
    def supports_primitives_in_json_field(self): ...
    def supports_frame_exclusion(self): ...
    def supports_boolean_expr_in_select_clause(self): ...
    def supports_comparing_boolean_expr(self): ...
    def supports_aggregation_over_interval_types(self): ...
    def bare_select_suffix(self): ...
