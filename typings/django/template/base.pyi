from .exceptions import TemplateSyntaxError as TemplateSyntaxError
from _typeshed import Incomplete
from collections.abc import Generator
from django.template.context import BaseContext as BaseContext
from django.utils.formats import localize as localize
from django.utils.html import conditional_escape as conditional_escape, escape as escape
from django.utils.safestring import SafeData as SafeData, SafeString as SafeString, mark_safe as mark_safe
from django.utils.text import get_text_list as get_text_list, smart_split as smart_split, unescape_string_literal as unescape_string_literal
from django.utils.timezone import template_localtime as template_localtime
from django.utils.translation import gettext_lazy as gettext_lazy, pgettext_lazy as pgettext_lazy
from enum import Enum

FILTER_SEPARATOR: str
FILTER_ARGUMENT_SEPARATOR: str
VARIABLE_ATTRIBUTE_SEPARATOR: str
BLOCK_TAG_START: str
BLOCK_TAG_END: str
VARIABLE_TAG_START: str
VARIABLE_TAG_END: str
COMMENT_TAG_START: str
COMMENT_TAG_END: str
SINGLE_BRACE_START: str
SINGLE_BRACE_END: str
UNKNOWN_SOURCE: str
tag_re: Incomplete
logger: Incomplete

class TokenType(Enum):
    TEXT = 0
    VAR = 1
    BLOCK = 2
    COMMENT = 3

class VariableDoesNotExist(Exception):
    msg: Incomplete
    params: Incomplete
    def __init__(self, msg, params=()) -> None: ...

class Origin:
    name: Incomplete
    template_name: Incomplete
    loader: Incomplete
    def __init__(self, name, template_name: Incomplete | None = None, loader: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    @property
    def loader_name(self): ...

class Template:
    name: Incomplete
    origin: Incomplete
    engine: Incomplete
    source: Incomplete
    nodelist: Incomplete
    def __init__(self, template_string, origin: Incomplete | None = None, name: Incomplete | None = None, engine: Incomplete | None = None) -> None: ...
    def render(self, context): ...
    extra_data: Incomplete
    def compile_nodelist(self): ...
    def get_exception_info(self, exception, token): ...

def linebreak_iter(template_source) -> Generator[Incomplete]: ...

class Token:
    token_type: Incomplete
    contents: Incomplete
    lineno: Incomplete
    position: Incomplete
    def __init__(self, token_type, contents, position: Incomplete | None = None, lineno: Incomplete | None = None) -> None: ...
    def split_contents(self): ...

class Lexer:
    template_string: Incomplete
    verbatim: bool
    def __init__(self, template_string) -> None: ...
    def tokenize(self): ...
    def create_token(self, token_string, position, lineno, in_tag): ...

class DebugLexer(Lexer):
    def tokenize(self): ...

class Parser:
    tokens: Incomplete
    tags: Incomplete
    filters: Incomplete
    command_stack: Incomplete
    extra_data: Incomplete
    libraries: Incomplete
    origin: Incomplete
    def __init__(self, tokens, libraries: Incomplete | None = None, builtins: Incomplete | None = None, origin: Incomplete | None = None) -> None: ...
    def parse(self, parse_until: Incomplete | None = None): ...
    def skip_past(self, endtag) -> None: ...
    def extend_nodelist(self, nodelist, node, token) -> None: ...
    def error(self, token, e): ...
    def invalid_block_tag(self, token, command, parse_until: Incomplete | None = None) -> None: ...
    def unclosed_block_tag(self, parse_until) -> None: ...
    def next_token(self): ...
    def prepend_token(self, token) -> None: ...
    def delete_first_token(self) -> None: ...
    def add_library(self, lib) -> None: ...
    def compile_filter(self, token): ...
    def find_filter(self, filter_name): ...

constant_string: Incomplete
filter_raw_string: Incomplete
filter_re: Incomplete

class FilterExpression:
    token: Incomplete
    filters: Incomplete
    var: Incomplete
    is_var: Incomplete
    def __init__(self, token, parser) -> None: ...
    def resolve(self, context, ignore_failures: bool = False): ...
    def args_check(name, func, provided): ...
    args_check: Incomplete

class Variable:
    var: Incomplete
    literal: Incomplete
    lookups: Incomplete
    translate: bool
    message_context: Incomplete
    def __init__(self, var) -> None: ...
    def resolve(self, context): ...

class Node:
    must_be_first: bool
    child_nodelists: Incomplete
    token: Incomplete
    def render(self, context) -> None: ...
    def render_annotated(self, context): ...
    def get_nodes_by_type(self, nodetype): ...

class NodeList(list):
    contains_nontext: bool
    def render(self, context): ...
    def get_nodes_by_type(self, nodetype): ...

class TextNode(Node):
    child_nodelists: Incomplete
    s: Incomplete
    def __init__(self, s) -> None: ...
    def render(self, context): ...
    def render_annotated(self, context): ...

def render_value_in_context(value, context): ...

class VariableNode(Node):
    child_nodelists: Incomplete
    filter_expression: Incomplete
    def __init__(self, filter_expression) -> None: ...
    def render(self, context): ...

kwarg_re: Incomplete

def token_kwargs(bits, parser, support_legacy: bool = False): ...
