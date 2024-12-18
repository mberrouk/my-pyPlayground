from _typeshed import Incomplete

class TokenBase:
    id: Incomplete
    value: Incomplete
    first: Incomplete
    second: Incomplete
    def nud(self, parser) -> None: ...
    def led(self, left, parser) -> None: ...
    def display(self): ...

def infix(bp, func): ...
def prefix(bp, func): ...

OPERATORS: Incomplete

class Literal(TokenBase):
    id: str
    lbp: int
    value: Incomplete
    def __init__(self, value) -> None: ...
    def display(self): ...
    def nud(self, parser): ...
    def eval(self, context): ...

class EndToken(TokenBase):
    lbp: int
    def nud(self, parser) -> None: ...

class IfParser:
    error_class = ValueError
    tokens: Incomplete
    pos: int
    current_token: Incomplete
    def __init__(self, tokens) -> None: ...
    def translate_token(self, token): ...
    def next_token(self): ...
    def parse(self): ...
    def expression(self, rbp: int = 0): ...
    def create_var(self, value): ...