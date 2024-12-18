from _typeshed import Incomplete
from django.utils.timezone import get_fixed_timezone as get_fixed_timezone

date_re: Incomplete
time_re: Incomplete
datetime_re: Incomplete
standard_duration_re: Incomplete
iso8601_duration_re: Incomplete
postgres_interval_re: Incomplete

def parse_date(value): ...
def parse_time(value): ...
def parse_datetime(value): ...
def parse_duration(value): ...
