"""
This type stub file was generated by pyright.
"""

class BaseDatabaseOperations:
    """
    Encapsulate backend-specific differences, such as the way a backend
    performs ordering or calculates the ID of a recently-inserted row.
    """
    compiler_module = ...
    integer_field_ranges = ...
    set_operators = ...
    cast_data_types = ...
    cast_char_field_without_max_length = ...
    PRECEDING = ...
    FOLLOWING = ...
    UNBOUNDED_PRECEDING = ...
    UNBOUNDED_FOLLOWING = ...
    CURRENT_ROW = ...
    explain_prefix = ...
    def __init__(self, connection) -> None:
        ...
    
    def autoinc_sql(self, table, column): # -> None:
        """
        Return any SQL needed to support auto-incrementing primary keys, or
        None if no SQL is necessary.

        This SQL is executed when a table is created.
        """
        ...
    
    def bulk_batch_size(self, fields, objs): # -> int:
        """
        Return the maximum allowed batch size for the backend. The fields
        are the fields going to be inserted in the batch, the objs contains
        all the objects to be inserted.
        """
        ...
    
    def format_for_duration_arithmetic(self, sql):
        ...
    
    def cache_key_culling_sql(self): # -> str:
        """
        Return an SQL query that retrieves the first cache key greater than the
        n smallest.

        This is used by the 'db' cache backend to determine where to start
        culling.
        """
        ...
    
    def unification_cast_sql(self, output_field): # -> Literal['%s']:
        """
        Given a field instance, return the SQL that casts the result of a union
        to that type. The resulting string should contain a '%s' placeholder
        for the expression being cast.
        """
        ...
    
    def date_extract_sql(self, lookup_type, sql, params):
        """
        Given a lookup_type of 'year', 'month', or 'day', return the SQL that
        extracts a value from the given date field field_name.
        """
        ...
    
    def date_trunc_sql(self, lookup_type, sql, params, tzname=...):
        """
        Given a lookup_type of 'year', 'month', or 'day', return the SQL that
        truncates the given date or datetime field field_name to a date object
        with only the given specificity.

        If `tzname` is provided, the given value is truncated in a specific
        timezone.
        """
        ...
    
    def datetime_cast_date_sql(self, sql, params, tzname):
        """
        Return the SQL to cast a datetime value to date value.
        """
        ...
    
    def datetime_cast_time_sql(self, sql, params, tzname):
        """
        Return the SQL to cast a datetime value to time value.
        """
        ...
    
    def datetime_extract_sql(self, lookup_type, sql, params, tzname):
        """
        Given a lookup_type of 'year', 'month', 'day', 'hour', 'minute', or
        'second', return the SQL that extracts a value from the given
        datetime field field_name.
        """
        ...
    
    def datetime_trunc_sql(self, lookup_type, sql, params, tzname):
        """
        Given a lookup_type of 'year', 'month', 'day', 'hour', 'minute', or
        'second', return the SQL that truncates the given datetime field
        field_name to a datetime object with only the given specificity.
        """
        ...
    
    def time_trunc_sql(self, lookup_type, sql, params, tzname=...):
        """
        Given a lookup_type of 'hour', 'minute' or 'second', return the SQL
        that truncates the given time or datetime field field_name to a time
        object with only the given specificity.

        If `tzname` is provided, the given value is truncated in a specific
        timezone.
        """
        ...
    
    def time_extract_sql(self, lookup_type, sql, params):
        """
        Given a lookup_type of 'hour', 'minute', or 'second', return the SQL
        that extracts a value from the given time field field_name.
        """
        ...
    
    def deferrable_sql(self): # -> Literal['']:
        """
        Return the SQL to make a constraint "initially deferred" during a
        CREATE TABLE statement.
        """
        ...
    
    def distinct_sql(self, fields, params): # -> tuple[list[str], list[Any]]:
        """
        Return an SQL DISTINCT clause which removes duplicate rows from the
        result set. If any fields are given, only check the given fields for
        duplicates.
        """
        ...
    
    def fetch_returned_insert_columns(self, cursor, returning_params):
        """
        Given a cursor object that has just performed an INSERT...RETURNING
        statement into a table, return the newly created data.
        """
        ...
    
    def field_cast_sql(self, db_type, internal_type): # -> Literal['%s']:
        """
        Given a column type (e.g. 'BLOB', 'VARCHAR') and an internal type
        (e.g. 'GenericIPAddressField'), return the SQL to cast it before using
        it in a WHERE statement. The resulting string should contain a '%s'
        placeholder for the column being searched against.
        """
        ...
    
    def force_group_by(self): # -> list[Any]:
        """
        Return a GROUP BY clause to use with a HAVING clause when no grouping
        is specified.
        """
        ...
    
    def force_no_ordering(self): # -> list[Any]:
        """
        Return a list used in the "ORDER BY" clause to force no ordering at
        all. Return an empty list to include nothing in the ordering.
        """
        ...
    
    def for_update_sql(self, nowait=..., skip_locked=..., of=..., no_key=...): # -> str:
        """
        Return the FOR UPDATE SQL clause to lock rows for an update operation.
        """
        ...
    
    def limit_offset_sql(self, low_mark, high_mark): # -> LiteralString:
        """Return LIMIT/OFFSET SQL clause."""
        ...
    
    def bulk_insert_sql(self, fields, placeholder_rows): # -> str:
        ...
    
    def last_executed_query(self, cursor, sql, params): # -> str:
        """
        Return a string of the query last executed by the given cursor, with
        placeholders replaced with actual values.

        `sql` is the raw query containing placeholders and `params` is the
        sequence of parameters. These are used by default, but this method
        exists for database backends to provide a better implementation
        according to their own quoting schemes.
        """
        ...
    
    def last_insert_id(self, cursor, table_name, pk_name):
        """
        Given a cursor object that has just performed an INSERT statement into
        a table that has an auto-incrementing ID, return the newly created ID.

        `pk_name` is the name of the primary-key column.
        """
        ...
    
    def lookup_cast(self, lookup_type, internal_type=...): # -> Literal['%s']:
        """
        Return the string to use in a query when performing lookups
        ("contains", "like", etc.). It should contain a '%s' placeholder for
        the column being searched against.
        """
        ...
    
    def max_in_list_size(self): # -> None:
        """
        Return the maximum number of items that can be passed in a single 'IN'
        list condition, or None if the backend does not impose a limit.
        """
        ...
    
    def max_name_length(self): # -> None:
        """
        Return the maximum length of table and column names, or None if there
        is no limit.
        """
        ...
    
    def no_limit_value(self):
        """
        Return the value to use for the LIMIT when we are wanting "LIMIT
        infinity". Return None if the limit clause can be omitted in this case.
        """
        ...
    
    def pk_default_value(self): # -> Literal['DEFAULT']:
        """
        Return the value to use during an INSERT statement to specify that
        the field should use its default value.
        """
        ...
    
    def prepare_sql_script(self, sql): # -> list[str]:
        """
        Take an SQL script that may contain multiple lines and return a list
        of statements to feed to successive cursor.execute() calls.

        Since few databases are able to process raw SQL scripts in a single
        cursor.execute() call and PEP 249 doesn't talk about this use case,
        the default implementation is conservative.
        """
        ...
    
    def process_clob(self, value):
        """
        Return the value of a CLOB column, for backends that return a locator
        object that requires additional processing.
        """
        ...
    
    def return_insert_columns(self, fields): # -> None:
        """
        For backends that support returning columns as part of an insert query,
        return the SQL and params to append to the INSERT query. The returned
        fragment should contain a format string to hold the appropriate column.
        """
        ...
    
    def compiler(self, compiler_name): # -> Any:
        """
        Return the SQLCompiler class corresponding to the given name,
        in the namespace corresponding to the `compiler_module` attribute
        on this backend.
        """
        ...
    
    def quote_name(self, name):
        """
        Return a quoted version of the given table, index, or column name. Do
        not quote the given name if it's already been quoted.
        """
        ...
    
    def regex_lookup(self, lookup_type):
        """
        Return the string to use in a query when performing regular expression
        lookups (using "regex" or "iregex"). It should contain a '%s'
        placeholder for the column being searched against.

        If the feature is not supported (or part of it is not supported), raise
        NotImplementedError.
        """
        ...
    
    def savepoint_create_sql(self, sid):
        """
        Return the SQL for starting a new savepoint. Only required if the
        "uses_savepoints" feature is True. The "sid" parameter is a string
        for the savepoint id.
        """
        ...
    
    def savepoint_commit_sql(self, sid):
        """
        Return the SQL for committing the given savepoint.
        """
        ...
    
    def savepoint_rollback_sql(self, sid):
        """
        Return the SQL for rolling back the given savepoint.
        """
        ...
    
    def set_time_zone_sql(self): # -> Literal['']:
        """
        Return the SQL that will set the connection's time zone.

        Return '' if the backend doesn't support time zones.
        """
        ...
    
    def sql_flush(self, style, tables, *, reset_sequences=..., allow_cascade=...):
        """
        Return a list of SQL statements required to remove all data from
        the given database tables (without actually removing the tables
        themselves).

        The `style` argument is a Style object as returned by either
        color_style() or no_style() in django.core.management.color.

        If `reset_sequences` is True, the list includes SQL statements required
        to reset the sequences.

        The `allow_cascade` argument determines whether truncation may cascade
        to tables with foreign keys pointing the tables being truncated.
        PostgreSQL requires a cascade even if these tables are empty.
        """
        ...
    
    def execute_sql_flush(self, sql_list): # -> None:
        """Execute a list of SQL statements to flush the database."""
        ...
    
    def sequence_reset_by_name_sql(self, style, sequences): # -> list[Any]:
        """
        Return a list of the SQL statements required to reset sequences
        passed in `sequences`.

        The `style` argument is a Style object as returned by either
        color_style() or no_style() in django.core.management.color.
        """
        ...
    
    def sequence_reset_sql(self, style, model_list): # -> list[Any]:
        """
        Return a list of the SQL statements required to reset sequences for
        the given models.

        The `style` argument is a Style object as returned by either
        color_style() or no_style() in django.core.management.color.
        """
        ...
    
    def start_transaction_sql(self): # -> Literal['BEGIN;']:
        """Return the SQL statement required to start a transaction."""
        ...
    
    def end_transaction_sql(self, success=...): # -> Literal['ROLLBACK;', 'COMMIT;']:
        """Return the SQL statement required to end a transaction."""
        ...
    
    def tablespace_sql(self, tablespace, inline=...): # -> Literal['']:
        """
        Return the SQL that will be used in a query to define the tablespace.

        Return '' if the backend doesn't support tablespaces.

        If `inline` is True, append the SQL to a row; otherwise append it to
        the entire CREATE TABLE or CREATE INDEX statement.
        """
        ...
    
    def prep_for_like_query(self, x): # -> str:
        """Prepare a value for use in a LIKE query."""
        ...
    
    prep_for_iexact_query = ...
    def validate_autopk_value(self, value):
        """
        Certain backends do not accept some values for "serial" fields
        (for example zero in MySQL). Raise a ValueError if the value is
        invalid, otherwise return the validated value.
        """
        ...
    
    def adapt_unknown_value(self, value): # -> str | None:
        """
        Transform a value to something compatible with the backend driver.

        This method only depends on the type of the value. It's designed for
        cases where the target type isn't known, such as .raw() SQL queries.
        As a consequence it may not work perfectly in all circumstances.
        """
        ...
    
    def adapt_integerfield_value(self, value, internal_type):
        ...
    
    def adapt_datefield_value(self, value): # -> str | None:
        """
        Transform a date value to an object compatible with what is expected
        by the backend driver for date columns.
        """
        ...
    
    def adapt_datetimefield_value(self, value): # -> str | None:
        """
        Transform a datetime value to an object compatible with what is expected
        by the backend driver for datetime columns.
        """
        ...
    
    def adapt_timefield_value(self, value): # -> str | None:
        """
        Transform a time value to an object compatible with what is expected
        by the backend driver for time columns.
        """
        ...
    
    def adapt_decimalfield_value(self, value, max_digits=..., decimal_places=...): # -> str | None:
        """
        Transform a decimal.Decimal value to an object compatible with what is
        expected by the backend driver for decimal (numeric) columns.
        """
        ...
    
    def adapt_ipaddressfield_value(self, value): # -> None:
        """
        Transform a string representation of an IP address into the expected
        type for the backend driver.
        """
        ...
    
    def adapt_json_value(self, value, encoder): # -> str:
        ...
    
    def year_lookup_bounds_for_date_field(self, value, iso_year=...): # -> list[str | None]:
        """
        Return a two-elements list with the lower and upper bound to be used
        with a BETWEEN operator to query a DateField value using a year
        lookup.

        `value` is an int, containing the looked-up year.
        If `iso_year` is True, return bounds for ISO-8601 week-numbering years.
        """
        ...
    
    def year_lookup_bounds_for_datetime_field(self, value, iso_year=...): # -> list[str | None]:
        """
        Return a two-elements list with the lower and upper bound to be used
        with a BETWEEN operator to query a DateTimeField value using a year
        lookup.

        `value` is an int, containing the looked-up year.
        If `iso_year` is True, return bounds for ISO-8601 week-numbering years.
        """
        ...
    
    def get_db_converters(self, expression): # -> list[Any]:
        """
        Return a list of functions needed to convert field data.

        Some field types on some backends do not provide data in the correct
        format, this is the hook for converter functions.
        """
        ...
    
    def convert_durationfield_value(self, value, expression, connection): # -> timedelta | None:
        ...
    
    def check_expression_support(self, expression): # -> None:
        """
        Check that the backend supports the provided expression.

        This is used on specific backends to rule out known expressions
        that have problematic or nonexistent implementations. If the
        expression has a known problem, the backend should raise
        NotSupportedError.
        """
        ...
    
    def conditional_expression_supported_in_where_clause(self, expression): # -> Literal[True]:
        """
        Return True, if the conditional expression is supported in the WHERE
        clause.
        """
        ...
    
    def combine_expression(self, connector, sub_expressions):
        """
        Combine a list of subexpressions into a single expression, using
        the provided connecting operator. This is required because operators
        can vary between backends (e.g., Oracle with %% and &) and between
        subexpression types (e.g., date expressions).
        """
        ...
    
    def combine_duration_expression(self, connector, sub_expressions):
        ...
    
    def binary_placeholder_sql(self, value): # -> Literal['%s']:
        """
        Some backends require special syntax to insert binary content (MySQL
        for example uses '_binary %s').
        """
        ...
    
    def modify_insert_params(self, placeholder, params):
        """
        Allow modification of insert parameters. Needed for Oracle Spatial
        backend due to #10888.
        """
        ...
    
    def integer_field_range(self, internal_type): # -> tuple[int, int]:
        """
        Given an integer field internal type (e.g. 'PositiveIntegerField'),
        return a tuple of the (min_value, max_value) form representing the
        range of the column type bound to the field.
        """
        ...
    
    def subtract_temporals(self, internal_type, lhs, rhs): # -> tuple[LiteralString, tuple[Any, ...]]:
        ...
    
    def window_frame_value(self, value): # -> str | None:
        ...
    
    def window_frame_rows_start_end(self, start=..., end=...): # -> tuple[str, str]:
        """
        Return SQL for start and end points in an OVER clause window frame.
        """
        ...
    
    def window_frame_range_start_end(self, start=..., end=...): # -> tuple[str, str]:
        ...
    
    def explain_query_prefix(self, format=..., **options): # -> None:
        ...
    
    def insert_statement(self, on_conflict=...): # -> Literal['INSERT INTO']:
        ...
    
    def on_conflict_suffix_sql(self, fields, on_conflict, update_fields, unique_fields): # -> Literal['']:
        ...
    
    def prepare_join_on_clause(self, lhs_table, lhs_field, rhs_table, rhs_field): # -> tuple[Col, Col]:
        ...
    


