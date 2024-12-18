from .base import Database as Database
from .utils import BulkInsertMapper as BulkInsertMapper, InsertVar as InsertVar, Oracle_datetime as Oracle_datetime
from _typeshed import Incomplete
from django.conf import settings as settings
from django.db import DatabaseError as DatabaseError, NotSupportedError as NotSupportedError
from django.db.backends.base.operations import BaseDatabaseOperations as BaseDatabaseOperations
from django.db.backends.utils import split_tzname_delta as split_tzname_delta, strip_quotes as strip_quotes, truncate_name as truncate_name
from django.db.models import AutoField as AutoField, Exists as Exists, ExpressionWrapper as ExpressionWrapper, Lookup as Lookup
from django.db.models.expressions import RawSQL as RawSQL
from django.db.models.sql.where import WhereNode as WhereNode
from django.utils import timezone as timezone
from django.utils.encoding import force_bytes as force_bytes, force_str as force_str
from django.utils.functional import cached_property as cached_property

class DatabaseOperations(BaseDatabaseOperations):
    integer_field_ranges: Incomplete
    set_operators: Incomplete
    cast_char_field_without_max_length: str
    cast_data_types: Incomplete
    def cache_key_culling_sql(self): ...
    def date_extract_sql(self, lookup_type, sql, params): ...
    def date_trunc_sql(self, lookup_type, sql, params, tzname: Incomplete | None = None): ...
    def datetime_cast_date_sql(self, sql, params, tzname): ...
    def datetime_cast_time_sql(self, sql, params, tzname): ...
    def datetime_extract_sql(self, lookup_type, sql, params, tzname): ...
    def datetime_trunc_sql(self, lookup_type, sql, params, tzname): ...
    def time_extract_sql(self, lookup_type, sql, params): ...
    def time_trunc_sql(self, lookup_type, sql, params, tzname: Incomplete | None = None): ...
    def get_db_converters(self, expression): ...
    def convert_textfield_value(self, value, expression, connection): ...
    def convert_binaryfield_value(self, value, expression, connection): ...
    def convert_booleanfield_value(self, value, expression, connection): ...
    def convert_datetimefield_value(self, value, expression, connection): ...
    def convert_datefield_value(self, value, expression, connection): ...
    def convert_timefield_value(self, value, expression, connection): ...
    def convert_uuidfield_value(self, value, expression, connection): ...
    @staticmethod
    def convert_empty_string(value, expression, connection): ...
    @staticmethod
    def convert_empty_bytes(value, expression, connection): ...
    def deferrable_sql(self): ...
    def fetch_returned_insert_columns(self, cursor, returning_params): ...
    def no_limit_value(self) -> None: ...
    def limit_offset_sql(self, low_mark, high_mark): ...
    def last_executed_query(self, cursor, sql, params): ...
    def last_insert_id(self, cursor, table_name, pk_name): ...
    def lookup_cast(self, lookup_type, internal_type: Incomplete | None = None): ...
    def max_in_list_size(self): ...
    def max_name_length(self): ...
    def pk_default_value(self): ...
    def prep_for_iexact_query(self, x): ...
    def process_clob(self, value): ...
    def quote_name(self, name): ...
    def regex_lookup(self, lookup_type): ...
    def return_insert_columns(self, fields): ...
    def sql_flush(self, style, tables, *, reset_sequences: bool = False, allow_cascade: bool = False): ...
    def sequence_reset_by_name_sql(self, style, sequences): ...
    def sequence_reset_sql(self, style, model_list): ...
    def start_transaction_sql(self): ...
    def tablespace_sql(self, tablespace, inline: bool = False): ...
    def adapt_datefield_value(self, value): ...
    def adapt_datetimefield_value(self, value): ...
    def adapt_timefield_value(self, value): ...
    def adapt_decimalfield_value(self, value, max_digits: Incomplete | None = None, decimal_places: Incomplete | None = None): ...
    def combine_expression(self, connector, sub_expressions): ...
    def bulk_insert_sql(self, fields, placeholder_rows): ...
    def subtract_temporals(self, internal_type, lhs, rhs): ...
    def bulk_batch_size(self, fields, objs): ...
    def conditional_expression_supported_in_where_clause(self, expression): ...
