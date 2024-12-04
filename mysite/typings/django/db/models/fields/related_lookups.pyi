"""
This type stub file was generated by pyright.
"""

from django.db.models.lookups import Exact, GreaterThan, GreaterThanOrEqual, In, IsNull, LessThan, LessThanOrEqual

class MultiColSource:
    contains_aggregate = ...
    contains_over_clause = ...
    def __init__(self, alias, targets, sources, field) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def relabeled_clone(self, relabels): # -> Self:
        ...
    
    def get_lookup(self, lookup):
        ...
    
    def resolve_expression(self, *args, **kwargs): # -> Self:
        ...
    


def get_normalized_value(value, lhs): # -> tuple[Any] | tuple[Any, ...]:
    ...

class RelatedIn(In):
    def get_prep_lookup(self): # -> list[Any]:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[str | Any, list[Any]] | tuple[str, list[Any]] | tuple[LiteralString, list[Any]]:
        ...
    


class RelatedLookupMixin:
    def get_prep_lookup(self):
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[str | Any, list[Any]]:
        ...
    


class RelatedExact(RelatedLookupMixin, Exact):
    ...


class RelatedLessThan(RelatedLookupMixin, LessThan):
    ...


class RelatedGreaterThan(RelatedLookupMixin, GreaterThan):
    ...


class RelatedGreaterThanOrEqual(RelatedLookupMixin, GreaterThanOrEqual):
    ...


class RelatedLessThanOrEqual(RelatedLookupMixin, LessThanOrEqual):
    ...


class RelatedIsNull(RelatedLookupMixin, IsNull):
    ...

