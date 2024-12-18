from _typeshed import Incomplete
from django.db.models.expressions import Func as Func, Value as Value
from django.db.models.fields import FloatField as FloatField, IntegerField as IntegerField
from django.db.models.functions import Cast as Cast
from django.db.models.functions.mixins import FixDecimalInputMixin as FixDecimalInputMixin, NumericOutputFieldMixin as NumericOutputFieldMixin
from django.db.models.lookups import Transform as Transform

class Abs(Transform):
    function: str
    lookup_name: str

class ACos(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class ASin(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class ATan(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class ATan2(NumericOutputFieldMixin, Func):
    function: str
    arity: int
    def as_sqlite(self, compiler, connection, **extra_context): ...

class Ceil(Transform):
    function: str
    lookup_name: str
    def as_oracle(self, compiler, connection, **extra_context): ...

class Cos(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class Cot(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str
    def as_oracle(self, compiler, connection, **extra_context): ...

class Degrees(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str
    def as_oracle(self, compiler, connection, **extra_context): ...

class Exp(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class Floor(Transform):
    function: str
    lookup_name: str

class Ln(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class Log(FixDecimalInputMixin, NumericOutputFieldMixin, Func):
    function: str
    arity: int
    def as_sqlite(self, compiler, connection, **extra_context): ...

class Mod(FixDecimalInputMixin, NumericOutputFieldMixin, Func):
    function: str
    arity: int

class Pi(NumericOutputFieldMixin, Func):
    function: str
    arity: int
    def as_oracle(self, compiler, connection, **extra_context): ...

class Power(NumericOutputFieldMixin, Func):
    function: str
    arity: int

class Radians(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str
    def as_oracle(self, compiler, connection, **extra_context): ...

class Random(NumericOutputFieldMixin, Func):
    function: str
    arity: int
    def as_mysql(self, compiler, connection, **extra_context): ...
    def as_oracle(self, compiler, connection, **extra_context): ...
    def as_sqlite(self, compiler, connection, **extra_context): ...
    def get_group_by_cols(self): ...

class Round(FixDecimalInputMixin, Transform):
    function: str
    lookup_name: str
    arity: Incomplete
    def __init__(self, expression, precision: int = 0, **extra) -> None: ...
    def as_sqlite(self, compiler, connection, **extra_context): ...

class Sign(Transform):
    function: str
    lookup_name: str

class Sin(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class Sqrt(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str

class Tan(NumericOutputFieldMixin, Transform):
    function: str
    lookup_name: str
