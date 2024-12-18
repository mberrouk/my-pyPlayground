from _typeshed import Incomplete
from django.db.models import Prefetch as Prefetch
from django.db.models.query import ModelIterable as ModelIterable, RawQuerySet as RawQuerySet

class GenericPrefetch(Prefetch):
    querysets: Incomplete
    def __init__(self, lookup, querysets, to_attr: Incomplete | None = None) -> None: ...
    def get_current_querysets(self, level): ...
