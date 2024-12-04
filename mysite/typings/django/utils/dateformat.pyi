"""
This type stub file was generated by pyright.
"""

"""
PHP date() style date formatting
See https://www.php.net/date for format strings

Usage:
>>> from datetime import datetime
>>> d = datetime.now()
>>> df = DateFormat(d)
>>> print(df.format('jS F Y H:i'))
7th October 2003 11:39
>>>
"""
re_formatchars = ...
re_escaped = ...
class Formatter:
    def format(self, formatstr): # -> LiteralString:
        ...
    


class TimeFormat(Formatter):
    def __init__(self, obj) -> None:
        ...
    
    def a(self): # -> Any:
        "'a.m.' or 'p.m.'"
        ...
    
    def A(self): # -> Any:
        "'AM' or 'PM'"
        ...
    
    def e(self): # -> Literal['']:
        """
        Timezone name.

        If timezone information is not available, return an empty string.
        """
        ...
    
    def f(self): # -> str | Literal[12]:
        """
        Time, in 12-hour hours and minutes, with minutes left off if they're
        zero.
        Examples: '1', '1:30', '2:05', '2'
        Proprietary extension.
        """
        ...
    
    def g(self): # -> Literal[12]:
        "Hour, 12-hour format without leading zeros; i.e. '1' to '12'"
        ...
    
    def G(self):
        "Hour, 24-hour format without leading zeros; i.e. '0' to '23'"
        ...
    
    def h(self): # -> str:
        "Hour, 12-hour format; i.e. '01' to '12'"
        ...
    
    def H(self):
        "Hour, 24-hour format; i.e. '00' to '23'"
        ...
    
    def i(self):
        "Minutes; i.e. '00' to '59'"
        ...
    
    def O(self): # -> str:
        """
        Difference to Greenwich time in hours; e.g. '+0200', '-0430'.

        If timezone information is not available, return an empty string.
        """
        ...
    
    def P(self): # -> Any | str:
        """
        Time, in 12-hour hours, minutes and 'a.m.'/'p.m.', with minutes left off
        if they're zero and the strings 'midnight' and 'noon' if appropriate.
        Examples: '1 a.m.', '1:30 p.m.', 'midnight', 'noon', '12:30 p.m.'
        Proprietary extension.
        """
        ...
    
    def s(self):
        "Seconds; i.e. '00' to '59'"
        ...
    
    def T(self): # -> str:
        """
        Time zone of this machine; e.g. 'EST' or 'MDT'.

        If timezone information is not available, return an empty string.
        """
        ...
    
    def u(self):
        "Microseconds; i.e. '000000' to '999999'"
        ...
    
    def Z(self): # -> int | Literal['']:
        """
        Time zone offset in seconds (i.e. '-43200' to '43200'). The offset for
        timezones west of UTC is always negative, and for those east of UTC is
        always positive.

        If timezone information is not available, return an empty string.
        """
        ...
    


class DateFormat(TimeFormat):
    def b(self): # -> __proxy__:
        "Month, textual, 3 letters, lowercase; e.g. 'jan'"
        ...
    
    def c(self):
        """
        ISO 8601 Format
        Example : '2008-01-02T10:30:00.000123'
        """
        ...
    
    def d(self):
        "Day of the month, 2 digits with leading zeros; i.e. '01' to '31'"
        ...
    
    def D(self): # -> __proxy__:
        "Day of the week, textual, 3 letters; e.g. 'Fri'"
        ...
    
    def E(self): # -> __proxy__:
        "Alternative month names as required by some locales. Proprietary extension."
        ...
    
    def F(self): # -> __proxy__:
        "Month, textual, long; e.g. 'January'"
        ...
    
    def I(self): # -> Literal['', '1', '0']:
        "'1' if daylight saving time, '0' otherwise."
        ...
    
    def j(self):
        "Day of the month without leading zeros; i.e. '1' to '31'"
        ...
    
    def l(self): # -> __proxy__:
        "Day of the week, textual, long; e.g. 'Friday'"
        ...
    
    def L(self): # -> bool:
        "Boolean for whether it is a leap year; i.e. True or False"
        ...
    
    def m(self):
        "Month; i.e. '01' to '12'"
        ...
    
    def M(self):
        "Month, textual, 3 letters; e.g. 'Jan'"
        ...
    
    def n(self):
        "Month without leading zeros; i.e. '1' to '12'"
        ...
    
    def N(self): # -> __proxy__:
        "Month abbreviation in Associated Press style. Proprietary extension."
        ...
    
    def o(self):
        "ISO 8601 year number matching the ISO week number (W)"
        ...
    
    def r(self): # -> str:
        "RFC 5322 formatted date; e.g. 'Thu, 21 Dec 2000 16:01:07 +0200'"
        ...
    
    def S(self): # -> Literal['th', 'st', 'nd', 'rd']:
        """
        English ordinal suffix for the day of the month, 2 characters; i.e.
        'st', 'nd', 'rd' or 'th'.
        """
        ...
    
    def t(self): # -> int:
        "Number of days in the given month; i.e. '28' to '31'"
        ...
    
    def U(self): # -> int:
        "Seconds since the Unix epoch (January 1 1970 00:00:00 GMT)"
        ...
    
    def w(self):
        "Day of the week, numeric, i.e. '0' (Sunday) to '6' (Saturday)"
        ...
    
    def W(self):
        "ISO-8601 week number of year, weeks starting on Monday"
        ...
    
    def y(self):
        """Year, 2 digits with leading zeros; e.g. '99'."""
        ...
    
    def Y(self):
        """Year, 4 digits with leading zeros; e.g. '1999'."""
        ...
    
    def z(self):
        """Day of the year, i.e. 1 to 366."""
        ...
    


def format(value, format_string): # -> LiteralString:
    "Convenience function"
    ...

def time_format(value, format_string): # -> LiteralString:
    "Convenience function"
    ...

