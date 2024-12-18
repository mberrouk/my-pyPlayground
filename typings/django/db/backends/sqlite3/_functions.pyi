import statistics
from _typeshed import Incomplete
from django.db.backends.utils import split_tzname_delta as split_tzname_delta, typecast_time as typecast_time, typecast_timestamp as typecast_timestamp
from django.utils import timezone as timezone
from django.utils.duration import duration_microseconds as duration_microseconds

def register(connection) -> None: ...

class ListAggregate(list):
    step: Incomplete

class StdDevPop(ListAggregate):
    finalize = statistics.pstdev

class StdDevSamp(ListAggregate):
    finalize = statistics.stdev

class VarPop(ListAggregate):
    finalize = statistics.pvariance

class VarSamp(ListAggregate):
    finalize = statistics.variance
