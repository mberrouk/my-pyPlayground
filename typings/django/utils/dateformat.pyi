from _typeshed import Incomplete
from django.utils.dates import MONTHS as MONTHS, MONTHS_3 as MONTHS_3, MONTHS_ALT as MONTHS_ALT, MONTHS_AP as MONTHS_AP, WEEKDAYS as WEEKDAYS, WEEKDAYS_ABBR as WEEKDAYS_ABBR
from django.utils.timezone import get_default_timezone as get_default_timezone, is_naive as is_naive, make_aware as make_aware

re_formatchars: Incomplete
re_escaped: Incomplete

class Formatter:
    def format(self, formatstr): ...

class TimeFormat(Formatter):
    data: Incomplete
    timezone: Incomplete
    def __init__(self, obj) -> None: ...
    def a(self): ...
    def A(self): ...
    def e(self): ...
    def f(self): ...
    def g(self): ...
    def G(self): ...
    def h(self): ...
    def H(self): ...
    def i(self): ...
    def O(self): ...
    def P(self): ...
    def s(self): ...
    def T(self): ...
    def u(self): ...
    def Z(self): ...

class DateFormat(TimeFormat):
    def b(self): ...
    def c(self): ...
    def d(self): ...
    def D(self): ...
    def E(self): ...
    def F(self): ...
    def I(self): ...
    def j(self): ...
    def l(self): ...
    def L(self): ...
    def m(self): ...
    def M(self): ...
    def n(self): ...
    def N(self): ...
    def o(self): ...
    def r(self): ...
    def S(self): ...
    def t(self): ...
    def U(self): ...
    def w(self): ...
    def W(self): ...
    def y(self): ...
    def Y(self): ...
    def z(self): ...

def format(value, format_string): ...
def time_format(value, format_string): ...
