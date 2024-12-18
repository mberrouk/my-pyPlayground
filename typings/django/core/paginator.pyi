import collections.abc
from _typeshed import Incomplete
from collections.abc import Generator
from django.utils.functional import cached_property as cached_property
from django.utils.inspect import method_has_no_args as method_has_no_args

class UnorderedObjectListWarning(RuntimeWarning): ...
class InvalidPage(Exception): ...
class PageNotAnInteger(InvalidPage): ...
class EmptyPage(InvalidPage): ...

class Paginator:
    ELLIPSIS: Incomplete
    default_error_messages: Incomplete
    object_list: Incomplete
    per_page: Incomplete
    orphans: Incomplete
    allow_empty_first_page: Incomplete
    error_messages: Incomplete
    def __init__(self, object_list, per_page, orphans: int = 0, allow_empty_first_page: bool = True, error_messages: Incomplete | None = None) -> None: ...
    def __iter__(self): ...
    def validate_number(self, number): ...
    def get_page(self, number): ...
    def page(self, number): ...
    def count(self): ...
    def num_pages(self): ...
    @property
    def page_range(self): ...
    def get_elided_page_range(self, number: int = 1, *, on_each_side: int = 3, on_ends: int = 2) -> Generator[Incomplete, Incomplete]: ...

class Page(collections.abc.Sequence):
    object_list: Incomplete
    number: Incomplete
    paginator: Incomplete
    def __init__(self, object_list, number, paginator) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def has_next(self): ...
    def has_previous(self): ...
    def has_other_pages(self): ...
    def next_page_number(self): ...
    def previous_page_number(self): ...
    def start_index(self): ...
    def end_index(self): ...