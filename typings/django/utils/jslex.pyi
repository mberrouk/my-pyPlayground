from _typeshed import Incomplete
from collections.abc import Generator

class Tok:
    num: int
    id: Incomplete
    name: Incomplete
    regex: Incomplete
    next: Incomplete
    def __init__(self, name, regex, next: Incomplete | None = None) -> None: ...

def literals(choices, prefix: str = '', suffix: str = ''): ...

class Lexer:
    regexes: Incomplete
    toks: Incomplete
    state: Incomplete
    def __init__(self, states, first) -> None: ...
    def lex(self, text) -> Generator[Incomplete]: ...

class JsLexer(Lexer):
    both_before: Incomplete
    both_after: Incomplete
    states: Incomplete
    def __init__(self) -> None: ...

def prepare_js_for_gettext(js): ...
