from _typeshed import Incomplete
from django.template import Library as Library, Node as Node, TemplateSyntaxError as TemplateSyntaxError
from django.utils import formats as formats

register: Incomplete

def localize(value): ...
def unlocalize(value): ...

class LocalizeNode(Node):
    nodelist: Incomplete
    use_l10n: Incomplete
    def __init__(self, nodelist, use_l10n) -> None: ...
    def render(self, context): ...

def localize_tag(parser, token): ...