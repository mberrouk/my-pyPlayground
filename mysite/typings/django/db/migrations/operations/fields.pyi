"""
This type stub file was generated by pyright.
"""

from django.utils.functional import cached_property
from .base import Operation

class FieldOperation(Operation):
    def __init__(self, model_name, name, field=...) -> None:
        ...
    
    @cached_property
    def model_name_lower(self):
        ...
    
    @cached_property
    def name_lower(self):
        ...
    
    def is_same_model_operation(self, operation):
        ...
    
    def is_same_field_operation(self, operation):
        ...
    
    def references_model(self, name, app_label): # -> bool:
        ...
    
    def references_field(self, model_name, name, app_label): # -> bool:
        ...
    
    def reduce(self, operation, app_label): # -> list[Any] | bool | list[Self]:
        ...
    


class AddField(FieldOperation):
    """Add a field to a model."""
    category = ...
    def __init__(self, model_name, name, field, preserve_default=...) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Any], dict[str, Any]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    
    def reduce(self, operation, app_label): # -> list[AddField] | list[Any] | bool | list[Self]:
        ...
    


class RemoveField(FieldOperation):
    """Remove a field from a model."""
    category = ...
    def deconstruct(self): # -> tuple[str, list[Any], dict[str, Any]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    
    def reduce(self, operation, app_label): # -> list[DeleteModel] | list[Any] | bool | list[Self]:
        ...
    


class AlterField(FieldOperation):
    """
    Alter a field's database column (e.g. null, max_length) to the provided
    new field.
    """
    category = ...
    def __init__(self, model_name, name, field, preserve_default=...) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Any], dict[str, Any]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    
    def reduce(self, operation, app_label): # -> list[AlterField | RemoveField] | list[Any] | bool | list[Self]:
        ...
    


class RenameField(FieldOperation):
    """Rename a field on the model. Might affect db_column too."""
    category = ...
    def __init__(self, model_name, old_name, new_name) -> None:
        ...
    
    @cached_property
    def old_name_lower(self):
        ...
    
    @cached_property
    def new_name_lower(self):
        ...
    
    def deconstruct(self): # -> tuple[str, list[Any], dict[str, Any]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> LiteralString:
        ...
    
    @property
    def migration_name_fragment(self): # -> str:
        ...
    
    def references_field(self, model_name, name, app_label): # -> Literal[False]:
        ...
    
    def reduce(self, operation, app_label): # -> list[RenameField] | list[Any] | bool | list[Self]:
        ...
    


