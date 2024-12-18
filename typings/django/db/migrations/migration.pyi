from .exceptions import IrreversibleError as IrreversibleError
from _typeshed import Incomplete
from django.db.migrations.utils import get_migration_name_timestamp as get_migration_name_timestamp
from django.db.transaction import atomic as atomic

class Migration:
    operations: Incomplete
    dependencies: Incomplete
    run_before: Incomplete
    replaces: Incomplete
    initial: Incomplete
    atomic: bool
    name: Incomplete
    app_label: Incomplete
    def __init__(self, name, app_label) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def mutate_state(self, project_state, preserve: bool = True): ...
    def apply(self, project_state, schema_editor, collect_sql: bool = False): ...
    def unapply(self, project_state, schema_editor, collect_sql: bool = False): ...
    def suggest_name(self): ...

class SwappableTuple(tuple):
    setting: Incomplete
    def __new__(cls, value, setting): ...

def swappable_dependency(value): ...