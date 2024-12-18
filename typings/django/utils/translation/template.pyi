from . import TranslatorCommentWarning as TranslatorCommentWarning, trim_whitespace as trim_whitespace
from _typeshed import Incomplete
from django.template.base import Lexer as Lexer, TokenType as TokenType

TRANSLATOR_COMMENT_MARK: str
dot_re: Incomplete

def blankout(src, char): ...

context_re: Incomplete
inline_re: Incomplete
block_re: Incomplete
endblock_re: Incomplete
plural_re: Incomplete
constant_re: Incomplete

def templatize(src, origin: Incomplete | None = None): ...
