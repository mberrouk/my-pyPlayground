from _typeshed import Incomplete
from django.conf import settings as settings
from django.template import Library as Library, Node as Node, TemplateSyntaxError as TemplateSyntaxError, Variable as Variable
from django.template.base import TokenType as TokenType, render_value_in_context as render_value_in_context
from django.template.defaulttags import token_kwargs as token_kwargs
from django.utils import translation as translation
from django.utils.safestring import SafeData as SafeData, SafeString as SafeString, mark_safe as mark_safe

register: Incomplete

class GetAvailableLanguagesNode(Node):
    variable: Incomplete
    def __init__(self, variable) -> None: ...
    def render(self, context): ...

class GetLanguageInfoNode(Node):
    lang_code: Incomplete
    variable: Incomplete
    def __init__(self, lang_code, variable) -> None: ...
    def render(self, context): ...

class GetLanguageInfoListNode(Node):
    languages: Incomplete
    variable: Incomplete
    def __init__(self, languages, variable) -> None: ...
    def get_language_info(self, language): ...
    def render(self, context): ...

class GetCurrentLanguageNode(Node):
    variable: Incomplete
    def __init__(self, variable) -> None: ...
    def render(self, context): ...

class GetCurrentLanguageBidiNode(Node):
    variable: Incomplete
    def __init__(self, variable) -> None: ...
    def render(self, context): ...

class TranslateNode(Node):
    child_nodelists: Incomplete
    noop: Incomplete
    asvar: Incomplete
    message_context: Incomplete
    filter_expression: Incomplete
    def __init__(self, filter_expression, noop, asvar: Incomplete | None = None, message_context: Incomplete | None = None) -> None: ...
    def render(self, context): ...

class BlockTranslateNode(Node):
    extra_context: Incomplete
    singular: Incomplete
    plural: Incomplete
    countervar: Incomplete
    counter: Incomplete
    message_context: Incomplete
    trimmed: Incomplete
    asvar: Incomplete
    tag_name: Incomplete
    def __init__(self, extra_context, singular, plural: Incomplete | None = None, countervar: Incomplete | None = None, counter: Incomplete | None = None, message_context: Incomplete | None = None, trimmed: bool = False, asvar: Incomplete | None = None, tag_name: str = 'blocktranslate') -> None: ...
    def render_token_list(self, tokens): ...
    def render(self, context, nested: bool = False): ...

class LanguageNode(Node):
    nodelist: Incomplete
    language: Incomplete
    def __init__(self, nodelist, language) -> None: ...
    def render(self, context): ...

def do_get_available_languages(parser, token): ...
def do_get_language_info(parser, token): ...
def do_get_language_info_list(parser, token): ...
def language_name(lang_code): ...
def language_name_translated(lang_code): ...
def language_name_local(lang_code): ...
def language_bidi(lang_code): ...
def do_get_current_language(parser, token): ...
def do_get_current_language_bidi(parser, token): ...
def do_translate(parser, token): ...
def do_block_translate(parser, token): ...
def language(parser, token): ...