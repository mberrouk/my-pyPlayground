from _typeshed import Incomplete
from collections.abc import Generator
from django.core.exceptions import SuspiciousFileOperation as SuspiciousFileOperation
from django.utils.functional import SimpleLazyObject as SimpleLazyObject, cached_property as cached_property, keep_lazy_text as keep_lazy_text, lazy as lazy
from django.utils.translation import gettext_lazy as gettext_lazy, pgettext as pgettext
from html.parser import HTMLParser
from io import BytesIO

def capfirst(x): ...

re_newlines: Incomplete
re_camel_case: Incomplete

def wrap(text, width): ...
def add_truncation_text(text, truncate: Incomplete | None = None): ...
def calculate_truncate_chars_length(length, replacement): ...

class TruncateHTMLParser(HTMLParser):
    class TruncationCompleted(Exception): ...
    tags: Incomplete
    output: str
    remaining: Incomplete
    replacement: Incomplete
    def __init__(self, *, length, replacement, convert_charrefs: bool = True) -> None: ...
    def void_elements(self): ...
    def handle_startendtag(self, tag, attrs) -> None: ...
    def handle_starttag(self, tag, attrs) -> None: ...
    def handle_endtag(self, tag) -> None: ...
    def handle_data(self, data) -> None: ...
    def feed(self, data) -> None: ...

class TruncateCharsHTMLParser(TruncateHTMLParser):
    length: Incomplete
    processed_chars: int
    def __init__(self, *, length, replacement, convert_charrefs: bool = True) -> None: ...
    def process(self, data): ...

class TruncateWordsHTMLParser(TruncateHTMLParser):
    def process(self, data): ...

class Truncator(SimpleLazyObject):
    MAX_LENGTH_HTML: int
    def __init__(self, text) -> None: ...
    def chars(self, num, truncate: Incomplete | None = None, html: bool = False): ...
    def words(self, num, truncate: Incomplete | None = None, html: bool = False): ...

def get_valid_filename(name): ...
def get_text_list(list_, last_word=...): ...
def normalize_newlines(text): ...
def phone2numeric(phone): ...
def compress_string(s, *, max_random_bytes: Incomplete | None = None): ...

class StreamingBuffer(BytesIO):
    def read(self): ...

def compress_sequence(sequence, *, max_random_bytes: Incomplete | None = None) -> Generator[Incomplete]: ...

smart_split_re: Incomplete

def smart_split(text) -> Generator[Incomplete]: ...
def unescape_string_literal(s): ...
def slugify(value, allow_unicode: bool = False): ...
def camel_case_to_spaces(value): ...

format_lazy: Incomplete