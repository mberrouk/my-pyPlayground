from _typeshed import Incomplete

class Reference:
    def references_table(self, table): ...
    def references_column(self, table, column): ...
    def references_index(self, table, index): ...
    def rename_table_references(self, old_table, new_table) -> None: ...
    def rename_column_references(self, table, old_column, new_column) -> None: ...

class Table(Reference):
    table: Incomplete
    quote_name: Incomplete
    def __init__(self, table, quote_name) -> None: ...
    def references_table(self, table): ...
    def references_index(self, table, index): ...
    def rename_table_references(self, old_table, new_table) -> None: ...

class TableColumns(Table):
    table: Incomplete
    columns: Incomplete
    def __init__(self, table, columns) -> None: ...
    def references_column(self, table, column): ...
    def rename_column_references(self, table, old_column, new_column) -> None: ...

class Columns(TableColumns):
    quote_name: Incomplete
    col_suffixes: Incomplete
    def __init__(self, table, columns, quote_name, col_suffixes=()) -> None: ...

class IndexName(TableColumns):
    suffix: Incomplete
    create_index_name: Incomplete
    def __init__(self, table, columns, suffix, create_index_name) -> None: ...

class IndexColumns(Columns):
    opclasses: Incomplete
    def __init__(self, table, columns, quote_name, col_suffixes=(), opclasses=()) -> None: ...

class ForeignKeyName(TableColumns):
    to_reference: Incomplete
    suffix_template: Incomplete
    create_fk_name: Incomplete
    def __init__(self, from_table, from_columns, to_table, to_columns, suffix_template, create_fk_name) -> None: ...
    def references_table(self, table): ...
    def references_column(self, table, column): ...
    def rename_table_references(self, old_table, new_table) -> None: ...
    def rename_column_references(self, table, old_column, new_column) -> None: ...

class Statement(Reference):
    template: Incomplete
    parts: Incomplete
    def __init__(self, template, **parts) -> None: ...
    def references_table(self, table): ...
    def references_column(self, table, column): ...
    def references_index(self, table, index): ...
    def rename_table_references(self, old_table, new_table) -> None: ...
    def rename_column_references(self, table, old_column, new_column) -> None: ...

class Expressions(TableColumns):
    compiler: Incomplete
    expressions: Incomplete
    quote_value: Incomplete
    def __init__(self, table, expressions, compiler, quote_value) -> None: ...
    def rename_table_references(self, old_table, new_table) -> None: ...
    columns: Incomplete
    def rename_column_references(self, table, old_column, new_column) -> None: ...
