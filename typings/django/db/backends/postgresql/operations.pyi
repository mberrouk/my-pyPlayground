from _typeshed import Incomplete
from django.conf import settings as settings
from django.db.backends.base.operations import BaseDatabaseOperations as BaseDatabaseOperations
from django.db.backends.postgresql.psycopg_any import Inet as Inet, Jsonb as Jsonb, errors as errors, is_psycopg3 as is_psycopg3, mogrify as mogrify
from django.db.backends.utils import split_tzname_delta as split_tzname_delta
from django.db.models.constants import OnConflict as OnConflict
from django.db.models.functions import Cast as Cast

def get_json_dumps(encoder): ...

class DatabaseOperations(BaseDatabaseOperations):
    cast_char_field_without_max_length: str
    explain_prefix: str
    explain_options: Incomplete
    cast_data_types: Incomplete
    integerfield_type_map: Incomplete
    def unification_cast_sql(self, output_field): ...
    def date_extract_sql(self, lookup_type, sql, params): ...
    def date_trunc_sql(self, lookup_type, sql, params, tzname: Incomplete | None = None): ...
    def datetime_cast_date_sql(self, sql, params, tzname): ...
    def datetime_cast_time_sql(self, sql, params, tzname): ...
    def datetime_extract_sql(self, lookup_type, sql, params, tzname): ...
    def datetime_trunc_sql(self, lookup_type, sql, params, tzname): ...
    def time_extract_sql(self, lookup_type, sql, params): ...
    def time_trunc_sql(self, lookup_type, sql, params, tzname: Incomplete | None = None): ...
    def deferrable_sql(self): ...
    def fetch_returned_insert_rows(self, cursor): ...
    def lookup_cast(self, lookup_type, internal_type: Incomplete | None = None): ...
    def no_limit_value(self) -> None: ...
    def prepare_sql_script(self, sql): ...
    def quote_name(self, name): ...
    def compose_sql(self, sql, params): ...
    def set_time_zone_sql(self): ...
    def sql_flush(self, style, tables, *, reset_sequences: bool = False, allow_cascade: bool = False): ...
    def sequence_reset_by_name_sql(self, style, sequences): ...
    def tablespace_sql(self, tablespace, inline: bool = False): ...
    def sequence_reset_sql(self, style, model_list): ...
    def prep_for_iexact_query(self, x): ...
    def max_name_length(self): ...
    def distinct_sql(self, fields, params): ...
    def last_executed_query(self, cursor, sql, params): ...
    def last_executed_query(self, cursor, sql, params): ...
    def return_insert_columns(self, fields): ...
    def adapt_integerfield_value(self, value, internal_type): ...
    def adapt_datefield_value(self, value): ...
    def adapt_datetimefield_value(self, value): ...
    def adapt_timefield_value(self, value): ...
    def adapt_decimalfield_value(self, value, max_digits: Incomplete | None = None, decimal_places: Incomplete | None = None): ...
    def adapt_ipaddressfield_value(self, value): ...
    def adapt_json_value(self, value, encoder): ...
    def subtract_temporals(self, internal_type, lhs, rhs): ...
    def explain_query_prefix(self, format: Incomplete | None = None, **options): ...
    def on_conflict_suffix_sql(self, fields, on_conflict, update_fields, unique_fields): ...
    def prepare_join_on_clause(self, lhs_table, lhs_field, rhs_table, rhs_field): ...
