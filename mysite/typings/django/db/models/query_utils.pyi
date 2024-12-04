"""
This type stub file was generated by pyright.
"""

import functools
from django.utils import tree
from django.utils.functional import cached_property

"""
Various data structures used in query construction.

Factored out from django.db.models.query to avoid making the main module very
large and/or so that they can be used by other modules without getting into
circular import difficulties.
"""
logger = ...
PathInfo = ...
def subclasses(cls): # -> Generator[Any, Any, None]:
    ...

class Q(tree.Node):
    """
    Encapsulate filters as objects that can then be combined logically (using
    `&` and `|`).
    """
    AND = ...
    OR = ...
    XOR = ...
    default = ...
    conditional = ...
    def __init__(self, *args, _connector=..., _negated=..., **kwargs) -> None:
        ...
    
    def __or__(self, other): # -> Node:
        ...
    
    def __and__(self, other): # -> Node:
        ...
    
    def __xor__(self, other): # -> Node:
        ...
    
    def __invert__(self): # -> Node:
        ...
    
    def resolve_expression(self, query=..., allow_joins=..., reuse=..., summarize=..., for_save=...):
        ...
    
    def flatten(self): # -> Generator[Self | Any, Any, None]:
        """
        Recursively yield this Q object and all subexpressions, in depth-first
        order.
        """
        ...
    
    def check(self, against, using=...): # -> bool:
        """
        Do a database query to check if the expressions of the Q instance
        matches against the expressions.
        """
        ...
    
    def deconstruct(self): # -> tuple[str, tuple[Any, ...], dict[Any, Any]]:
        ...
    
    @cached_property
    def identity(self): # -> tuple[Any, ...]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    @cached_property
    def referenced_base_fields(self): # -> set[Any]:
        """
        Retrieve all base fields referenced directly or through F expressions
        excluding any fields referenced through joins.
        """
        ...
    


class DeferredAttribute:
    """
    A wrapper for a deferred-loading field. When the value is read from this
    object the first time, the query is executed.
    """
    def __init__(self, field) -> None:
        ...
    
    def __get__(self, instance, cls=...): # -> Self:
        """
        Retrieve and caches the value from the datastore on the first lookup.
        Return the cached value.
        """
        ...
    


class class_or_instance_method:
    """
    Hook used in RegisterLookupMixin to return partial functions depending on
    the caller type (instance or class of models.Field).
    """
    def __init__(self, class_method, instance_method) -> None:
        ...
    
    def __get__(self, instance, owner): # -> partial[Any]:
        ...
    


class RegisterLookupMixin:
    @functools.cache
    def get_class_lookups(cls): # -> dict[Any, Any]:
        ...
    
    def get_instance_lookups(self): # -> dict[Any, Any]:
        ...
    
    get_lookups = ...
    get_class_lookups = ...
    def get_lookup(self, lookup_name): # -> type[Lookup] | None:
        ...
    
    def get_transform(self, lookup_name): # -> type[Transform] | None:
        ...
    
    @staticmethod
    def merge_dicts(dicts): # -> dict[Any, Any]:
        """
        Merge dicts in reverse to preference the order of the original list. e.g.,
        merge_dicts([a, b]) will preference the keys in 'a' over those in 'b'.
        """
        ...
    
    def register_class_lookup(cls, lookup, lookup_name=...):
        ...
    
    def register_instance_lookup(self, lookup, lookup_name=...):
        ...
    
    register_lookup = ...
    register_class_lookup = ...
    _unregister_lookup = ...
    _unregister_class_lookup = ...


def select_related_descend(field, restricted, requested, select_mask): # -> bool:
    """
    Return whether `field` should be used to descend deeper for
    `select_related()` purposes.

    Arguments:
     * `field` - the field to be checked. Can be either a `Field` or
       `ForeignObjectRel` instance.
     * `restricted` - a boolean field, indicating if the field list has been
       manually restricted using a select_related() clause.
     * `requested` - the select_related() dictionary.
     * `select_mask` - the dictionary of selected fields.
    """
    ...

def refs_expression(lookup_parts, annotations): # -> tuple[str, Any] | tuple[None, tuple[()]]:
    """
    Check if the lookup_parts contains references to the given annotations set.
    Because the LOOKUP_SEP is contained in the default annotation names, check
    each prefix of the lookup_parts for a match.
    """
    ...

def check_rel_lookup_compatibility(model, target_opts, field): # -> Any | bool:
    """
    Check that self.model is compatible with target_opts. Compatibility
    is OK if:
      1) model and opts match (where proxy inheritance is removed)
      2) model is parent of opts' model or the other way around
    """
    ...

class FilteredRelation:
    """Specify custom filtering in the ON clause of SQL joins."""
    def __init__(self, relation_name, *, condition=...) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def clone(self): # -> FilteredRelation:
        ...
    
    def relabeled_clone(self, change_map): # -> FilteredRelation:
        ...
    
    def resolve_expression(self, query, reuse, *args, **kwargs): # -> FilteredRelation:
        ...
    
    def as_sql(self, compiler, connection):
        ...
    


