from _typeshed import Incomplete
from django.db.models import DecimalField as DecimalField, DurationField as DurationField, Func as Func

class IntervalToSeconds(Func):
    function: str
    template: str
    def __init__(self, expression, *, output_field: Incomplete | None = None, **extra) -> None: ...

class SecondsToInterval(Func):
    function: str
    template: str
    def __init__(self, expression, *, output_field: Incomplete | None = None, **extra) -> None: ...
