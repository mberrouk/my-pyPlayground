from _typeshed import Incomplete
from django.db.models.expressions import Func

__all__ = ['CumeDist', 'DenseRank', 'FirstValue', 'Lag', 'LastValue', 'Lead', 'NthValue', 'Ntile', 'PercentRank', 'Rank', 'RowNumber']

class CumeDist(Func):
    function: str
    output_field: Incomplete
    window_compatible: bool

class DenseRank(Func):
    function: str
    output_field: Incomplete
    window_compatible: bool

class FirstValue(Func):
    arity: int
    function: str
    window_compatible: bool

class LagLeadFunction(Func):
    window_compatible: bool
    def __init__(self, expression, offset: int = 1, default: Incomplete | None = None, **extra) -> None: ...

class Lag(LagLeadFunction):
    function: str

class LastValue(Func):
    arity: int
    function: str
    window_compatible: bool

class Lead(LagLeadFunction):
    function: str

class NthValue(Func):
    function: str
    window_compatible: bool
    def __init__(self, expression, nth: int = 1, **extra) -> None: ...

class Ntile(Func):
    function: str
    output_field: Incomplete
    window_compatible: bool
    def __init__(self, num_buckets: int = 1, **extra) -> None: ...

class PercentRank(Func):
    function: str
    output_field: Incomplete
    window_compatible: bool

class Rank(Func):
    function: str
    output_field: Incomplete
    window_compatible: bool

class RowNumber(Func):
    function: str
    output_field: Incomplete
    window_compatible: bool
