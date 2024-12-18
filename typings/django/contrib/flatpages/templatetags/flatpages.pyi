from _typeshed import Incomplete
from django import template as template
from django.conf import settings as settings
from django.contrib.flatpages.models import FlatPage as FlatPage
from django.contrib.sites.shortcuts import get_current_site as get_current_site

register: Incomplete

class FlatpageNode(template.Node):
    context_name: Incomplete
    starts_with: Incomplete
    user: Incomplete
    def __init__(self, context_name, starts_with: Incomplete | None = None, user: Incomplete | None = None) -> None: ...
    def render(self, context): ...

def get_flatpages(parser, token): ...
