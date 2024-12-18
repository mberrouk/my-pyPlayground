from _typeshed import Incomplete
from django.db.models.lookups import Exact as Exact, GreaterThan as GreaterThan, GreaterThanOrEqual as GreaterThanOrEqual, In as In, IsNull as IsNull, LessThan as LessThan, LessThanOrEqual as LessThanOrEqual

class MultiColSource:
    contains_aggregate: bool
    contains_over_clause: bool
    output_field: Incomplete
    def __init__(self, alias, targets, sources, field) -> None: ...
    def relabeled_clone(self, relabels): ...
    def get_lookup(self, lookup): ...
    def resolve_expression(self, *args, **kwargs): ...

def get_normalized_value(value, lhs): ...

class RelatedIn(In):
    rhs: Incomplete
    def get_prep_lookup(self): ...
    def as_sql(self, compiler, connection): ...

class RelatedLookupMixin:
    rhs: Incomplete
    def get_prep_lookup(self): ...
    def as_sql(self, compiler, connection): ...

class RelatedExact(RelatedLookupMixin, Exact): ...
class RelatedLessThan(RelatedLookupMixin, LessThan): ...
class RelatedGreaterThan(RelatedLookupMixin, GreaterThan): ...
class RelatedGreaterThanOrEqual(RelatedLookupMixin, GreaterThanOrEqual): ...
class RelatedLessThanOrEqual(RelatedLookupMixin, LessThanOrEqual): ...
class RelatedIsNull(RelatedLookupMixin, IsNull): ...
