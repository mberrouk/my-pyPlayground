from django.contrib.postgres.fields import ArrayField as ArrayField
from django.db.models import Subquery as Subquery
from django.utils.functional import cached_property as cached_property

class ArraySubquery(Subquery):
    template: str
    def __init__(self, queryset, **kwargs) -> None: ...
    def output_field(self): ...
