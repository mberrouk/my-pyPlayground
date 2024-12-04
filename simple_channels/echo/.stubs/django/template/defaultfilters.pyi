"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable
from datetime import date as _date, datetime, time as _time
from typing import Any
from django.utils.safestring import SafeString

register: Any
def stringfilter(func: Callable) -> Callable:
    ...

def addslashes(value: str) -> str:
    ...

def capfirst(value: str) -> str:
    ...

def escapejs_filter(value: str) -> SafeString:
    ...

def json_script(value: dict[str, str], element_id: SafeString) -> SafeString:
    ...

def floatformat(text: Any | None, arg: int | str = ...) -> str:
    ...

def iriencode(value: str) -> str:
    ...

def linenumbers(value: str, autoescape: bool = ...) -> SafeString:
    ...

def lower(value: str) -> str:
    ...

def make_list(value: str) -> list[str]:
    ...

def slugify(value: str) -> SafeString:
    ...

def stringformat(value: Any, arg: str) -> str:
    ...

def title(value: str) -> str:
    ...

def truncatechars(value: str, arg: SafeString | int) -> str:
    ...

def truncatechars_html(value: str, arg: int | str) -> str:
    ...

def truncatewords(value: str, arg: int | str) -> str:
    ...

def truncatewords_html(value: str, arg: int | str) -> str:
    ...

def upper(value: str) -> str:
    ...

def urlencode(value: str, safe: SafeString | None = ...) -> str:
    ...

def urlize(value: str, autoescape: bool = ...) -> SafeString:
    ...

def urlizetrunc(value: str, limit: SafeString | int, autoescape: bool = ...) -> SafeString:
    ...

def wordcount(value: str) -> int:
    ...

def wordwrap(value: str, arg: SafeString | int) -> str:
    ...

def ljust(value: str, arg: SafeString | int) -> str:
    ...

def rjust(value: str, arg: SafeString | int) -> str:
    ...

def center(value: str, arg: SafeString | int) -> str:
    ...

def cut(value: str, arg: str) -> str:
    ...

def escape_filter(value: str) -> SafeString:
    ...

def escapeseq(value: list[str]) -> list[SafeString]:
    ...

def force_escape(value: str) -> SafeString:
    ...

def linebreaks_filter(value: str, autoescape: bool = ...) -> SafeString:
    ...

def linebreaksbr(value: str, autoescape: bool = ...) -> SafeString:
    ...

def safe(value: str) -> SafeString:
    ...

def safeseq(value: list[str]) -> list[SafeString]:
    ...

def striptags(value: str) -> str:
    ...

def dictsort(value: Any, arg: int | str) -> Any:
    ...

def dictsortreversed(value: Any, arg: int | str) -> Any:
    ...

def first(value: Any) -> Any:
    ...

def join(value: Any, arg: str, autoescape: bool = ...) -> Any:
    ...

def last(value: list[str]) -> str:
    ...

def length(value: Any) -> int:
    ...

def length_is(value: Any | None, arg: SafeString | int) -> bool | str:
    ...

def random(value: list[str]) -> str:
    ...

def slice_filter(value: Any, arg: str | int) -> Any:
    ...

def unordered_list(value: Any, autoescape: bool = ...) -> Any:
    ...

def add(value: Any, arg: Any) -> Any:
    ...

def get_digit(value: Any, arg: int) -> Any:
    ...

def date(value: _date | datetime | str | None, arg: str | None = ...) -> str:
    ...

def time(value: datetime | _time | str | None, arg: str | None = ...) -> str:
    ...

def timesince_filter(value: _date | None, arg: _date | None = ...) -> str:
    ...

def timeuntil_filter(value: _date | None, arg: _date | None = ...) -> str:
    ...

def default(value: int | str | None, arg: int | str) -> int | str:
    ...

def default_if_none(value: str | None, arg: int | str) -> int | str:
    ...

def divisibleby(value: int, arg: int) -> bool:
    ...

def yesno(value: int | None, arg: str | None = ...) -> bool | str | None:
    ...

def filesizeformat(bytes_: complex | int | str) -> str:
    ...

def pluralize(value: Any, arg: str = ...) -> str:
    ...

def phone2numeric_filter(value: str) -> str:
    ...

def pprint(value: Any) -> str:
    ...

