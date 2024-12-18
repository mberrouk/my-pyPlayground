from _typeshed import Incomplete
from django.conf import settings as settings
from django.db.models.expressions import Func as Func
from django.db.models.fields import DateField as DateField, DateTimeField as DateTimeField, DurationField as DurationField, Field as Field, IntegerField as IntegerField, TimeField as TimeField
from django.db.models.lookups import Transform as Transform, YearExact as YearExact, YearGt as YearGt, YearGte as YearGte, YearLt as YearLt, YearLte as YearLte
from django.utils import timezone as timezone

class TimezoneMixin:
    tzinfo: Incomplete
    def get_tzname(self): ...

class Extract(TimezoneMixin, Transform):
    lookup_name: Incomplete
    output_field: Incomplete
    tzinfo: Incomplete
    def __init__(self, expression, lookup_name: Incomplete | None = None, tzinfo: Incomplete | None = None, **extra) -> None: ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...

class ExtractYear(Extract):
    lookup_name: str

class ExtractIsoYear(Extract):
    lookup_name: str

class ExtractMonth(Extract):
    lookup_name: str

class ExtractDay(Extract):
    lookup_name: str

class ExtractWeek(Extract):
    lookup_name: str

class ExtractWeekDay(Extract):
    lookup_name: str

class ExtractIsoWeekDay(Extract):
    lookup_name: str

class ExtractQuarter(Extract):
    lookup_name: str

class ExtractHour(Extract):
    lookup_name: str

class ExtractMinute(Extract):
    lookup_name: str

class ExtractSecond(Extract):
    lookup_name: str

class Now(Func):
    template: str
    output_field: Incomplete
    def as_postgresql(self, compiler, connection, **extra_context): ...
    def as_mysql(self, compiler, connection, **extra_context): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...
    def as_oracle(self, compiler, connection, **extra_context): ...

class TruncBase(TimezoneMixin, Transform):
    kind: Incomplete
    tzinfo: Incomplete
    def __init__(self, expression, output_field: Incomplete | None = None, tzinfo: Incomplete | None = None, **extra) -> None: ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def convert_value(self, value, expression, connection): ...

class Trunc(TruncBase):
    kind: Incomplete
    def __init__(self, expression, kind, output_field: Incomplete | None = None, tzinfo: Incomplete | None = None, **extra) -> None: ...

class TruncYear(TruncBase):
    kind: str

class TruncQuarter(TruncBase):
    kind: str

class TruncMonth(TruncBase):
    kind: str

class TruncWeek(TruncBase):
    kind: str

class TruncDay(TruncBase):
    kind: str

class TruncDate(TruncBase):
    kind: str
    lookup_name: str
    output_field: Incomplete
    def as_sql(self, compiler, connection): ...

class TruncTime(TruncBase):
    kind: str
    lookup_name: str
    output_field: Incomplete
    def as_sql(self, compiler, connection): ...

class TruncHour(TruncBase):
    kind: str

class TruncMinute(TruncBase):
    kind: str

class TruncSecond(TruncBase):
    kind: str
