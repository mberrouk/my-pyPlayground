"""
This type stub file was generated by pyright.
"""

from django.db.models.query import QuerySet

class BaseManager:
    creation_counter = ...
    auto_created = ...
    use_in_migrations = ...
    def __new__(cls, *args, **kwargs): # -> Self:
        ...
    
    def __init__(self) -> None:
        ...
    
    def __str__(self) -> str:
        """Return "app_label.model_label.manager_name"."""
        ...
    
    def __class_getitem__(cls, *args, **kwargs): # -> type[Self]:
        ...
    
    def deconstruct(self): # -> tuple[Literal[True], None, LiteralString, None, None] | tuple[Literal[False], str, None, Any, Any]:
        """
        Return a 5-tuple of the form (as_manager (True), manager_class,
        queryset_class, args, kwargs).

        Raise a ValueError if the manager is dynamically generated.
        """
        ...
    
    def check(self, **kwargs): # -> list[Any]:
        ...
    
    @classmethod
    def from_queryset(cls, queryset_class, class_name=...): # -> Any:
        ...
    
    def contribute_to_class(self, cls, name): # -> None:
        ...
    
    def db_manager(self, using=..., hints=...): # -> Self:
        ...
    
    @property
    def db(self): # -> Any | Literal['default']:
        ...
    
    def get_queryset(self):
        """
        Return a new QuerySet object. Subclasses can override this method to
        customize the behavior of the Manager.
        """
        ...
    
    def all(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class Manager(BaseManager.from_queryset(QuerySet)):
    ...


class ManagerDescriptor:
    def __init__(self, manager) -> None:
        ...
    
    def __get__(self, instance, cls=...):
        ...
    


class EmptyManager(Manager):
    def __init__(self, model) -> None:
        ...
    
    def get_queryset(self):
        ...
    


