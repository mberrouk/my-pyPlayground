"""
This type stub file was generated by pyright.
"""

from django.utils.functional import cached_property

PROXY_PARENTS = ...
EMPTY_RELATION_TREE = ...
IMMUTABLE_WARNING = ...
DEFAULT_NAMES = ...
def normalize_together(option_together): # -> tuple[()] | tuple[tuple[Any, ...], ...] | tuple[Any, ...] | list[Any] | tuple[tuple[Any, ...] | list[Any]]:
    """
    option_together can be either a tuple of tuples, or a single
    tuple of two strings. Normalize it to a tuple of tuples, so that
    calling code can uniformly expect that.
    """
    ...

def make_immutable_fields_list(name, data): # -> ImmutableList:
    ...

class Options:
    FORWARD_PROPERTIES = ...
    REVERSE_PROPERTIES = ...
    default_apps = ...
    def __init__(self, meta, app_label=...) -> None:
        ...
    
    @property
    def label(self): # -> str:
        ...
    
    @property
    def label_lower(self): # -> str:
        ...
    
    @property
    def app_config(self): # -> None:
        ...
    
    def contribute_to_class(self, cls, name): # -> None:
        ...
    
    def add_manager(self, manager): # -> None:
        ...
    
    def add_field(self, field, private=...): # -> None:
        ...
    
    def setup_pk(self, field): # -> None:
        ...
    
    def setup_proxy(self, target): # -> None:
        """
        Do the internal setup so that the current model is a proxy for
        "target".
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def can_migrate(self, connection): # -> bool:
        """
        Return True if the model can/should be migrated on the `connection`.
        `connection` can be either a real connection or a connection alias.
        """
        ...
    
    @cached_property
    def verbose_name_raw(self): # -> str:
        """Return the untranslated verbose name."""
        ...
    
    @cached_property
    def swapped(self): # -> Any | None:
        """
        Has this model been swapped out for another? If so, return the model
        name of the replacement; otherwise, return None.

        For historical reasons, model name lookups using get_model() are
        case insensitive, so we make sure we are case insensitive here.
        """
        ...
    
    def setting_changed(self, *, setting, **kwargs): # -> None:
        ...
    
    @cached_property
    def managers(self): # -> ImmutableList:
        ...
    
    @cached_property
    def managers_map(self): # -> dict[Any, Any]:
        ...
    
    @cached_property
    def base_manager(self): # -> Manager:
        ...
    
    @cached_property
    def default_manager(self): # -> None:
        ...
    
    @cached_property
    def fields(self): # -> ImmutableList:
        """
        Return a list of all forward fields on the model and its parents,
        excluding ManyToManyFields.

        Private API intended only to be used by Django itself; get_fields()
        combined with filtering of field properties is the public API for
        obtaining this field list.
        """
        ...
    
    @cached_property
    def concrete_fields(self): # -> ImmutableList:
        """
        Return a list of all concrete fields on the model and its parents.

        Private API intended only to be used by Django itself; get_fields()
        combined with filtering of field properties is the public API for
        obtaining this field list.
        """
        ...
    
    @cached_property
    def local_concrete_fields(self): # -> ImmutableList:
        """
        Return a list of all concrete fields on the model.

        Private API intended only to be used by Django itself; get_fields()
        combined with filtering of field properties is the public API for
        obtaining this field list.
        """
        ...
    
    @cached_property
    def many_to_many(self): # -> ImmutableList:
        """
        Return a list of all many to many fields on the model and its parents.

        Private API intended only to be used by Django itself; get_fields()
        combined with filtering of field properties is the public API for
        obtaining this list.
        """
        ...
    
    @cached_property
    def related_objects(self): # -> ImmutableList:
        """
        Return all related objects pointing to the current model. The related
        objects can come from a one-to-one, one-to-many, or many-to-many field
        relation type.

        Private API intended only to be used by Django itself; get_fields()
        combined with filtering of field properties is the public API for
        obtaining this field list.
        """
        ...
    
    @cached_property
    def fields_map(self): # -> dict[Any, Any]:
        ...
    
    def get_field(self, field_name):
        """
        Return a field instance given the name of a forward or reverse field.
        """
        ...
    
    def get_base_chain(self, model): # -> list[Any]:
        """
        Return a list of parent classes leading to `model` (ordered from
        closest to most distant ancestor). This has to handle the case where
        `model` is a grandparent or even more distant relation.
        """
        ...
    
    @cached_property
    def all_parents(self): # -> tuple[()]:
        """
        Return all the ancestors of this model as a tuple ordered by MRO.
        Useful for determining if something is an ancestor, regardless of lineage.
        """
        ...
    
    def get_parent_list(self): # -> list[Any]:
        """
        Return all the ancestors of this model as a list ordered by MRO.
        Backward compatibility method.
        """
        ...
    
    def get_ancestor_link(self, ancestor): # -> None:
        """
        Return the field on the current model which points to the given
        "ancestor". This is possible an indirect link (a pointer to a parent
        model, which points, eventually, to the ancestor). Used when
        constructing table joins for model inheritance.

        Return None if the model isn't an ancestor of this one.
        """
        ...
    
    def get_path_to_parent(self, parent): # -> list[Any]:
        """
        Return a list of PathInfos containing the path from the current
        model to the parent model, or an empty list if parent is not a
        parent of the current model.
        """
        ...
    
    def get_path_from_parent(self, parent): # -> list[Any]:
        """
        Return a list of PathInfos containing the path from the parent
        model to the current model, or an empty list if parent is not a
        parent of the current model.
        """
        ...
    
    def get_fields(self, include_parents=..., include_hidden=...): # -> ImmutableList:
        """
        Return a list of fields associated to the model. By default, include
        forward and reverse fields, fields derived from inheritance, but not
        hidden fields. The returned fields can be changed using the parameters:

        - include_parents: include fields derived from inheritance
        - include_hidden:  include fields that have a related_name that
                           starts with a "+"
        """
        ...
    
    @cached_property
    def total_unique_constraints(self): # -> list[UniqueConstraint]:
        """
        Return a list of total unique constraints. Useful for determining set
        of fields guaranteed to be unique for all rows.
        """
        ...
    
    @cached_property
    def db_returning_fields(self): # -> list[Any]:
        """
        Private API intended only to be used by Django itself.
        Fields to be returned after a database insert.
        """
        ...
    


