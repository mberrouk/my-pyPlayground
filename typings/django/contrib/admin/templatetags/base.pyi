from _typeshed import Incomplete
from django.template.library import InclusionNode as InclusionNode, parse_bits as parse_bits

class InclusionAdminNode(InclusionNode):
    template_name: Incomplete
    def __init__(self, parser, token, func, template_name, takes_context: bool = True) -> None: ...
    def render(self, context): ...
